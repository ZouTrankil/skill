param([string]$Manifest)
$ErrorActionPreference = 'Stop'
$manifest = if ($Manifest) { $Manifest } elseif ($env:SYNC_REPOS_FILE) { $env:SYNC_REPOS_FILE } else { Join-Path $PSScriptRoot '..\repos.tsv' }
$logFile = if ($env:SYNC_REPOS_LOG) { $env:SYNC_REPOS_LOG } else { Join-Path $env:LOCALAPPDATA 'local-repo-sync\sync.log' }

if (-not (Test-Path -LiteralPath $manifest -PathType Leaf)) {
    Write-Error "清单不存在：$manifest"
    exit 2
}
$logDir = Split-Path -Parent $logFile
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
Start-Transcript -Path $logFile -Append | Out-Null
$failed = $false
try {
    Write-Output "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] 同步开始"
    foreach ($line in Get-Content -LiteralPath $manifest) {
        if ([string]::IsNullOrWhiteSpace($line) -or $line.StartsWith('#')) { continue }
        $fields = $line.Split("`t")
        if ($fields.Length -lt 3 -or $fields.Length -gt 4 -or
            [string]::IsNullOrWhiteSpace($fields[0]) -or
            [string]::IsNullOrWhiteSpace($fields[1]) -or
            [string]::IsNullOrWhiteSpace($fields[2])) {
            Write-Output "跳过：清单行格式错误：$line"
            $failed = $true
            continue
        }
        $repo, $remote, $base = $fields[0..2]
        $description = if ($fields.Length -eq 4) { $fields[3] } else { '' }
        Write-Output "`n仓库：$repo（$remote/$base） $description"
        if (-not (Test-Path -LiteralPath $repo -PathType Container)) {
            Write-Output '跳过：仓库目录不存在'
            $failed = $true
            continue
        }
        $root = (& git -C $repo rev-parse --show-toplevel 2>$null)
        if ($LASTEXITCODE -ne 0) {
            Write-Output '跳过：不是可访问的 Git 仓库'
            $failed = $true
            continue
        }
        $repoPath = [IO.Path]::GetFullPath($repo).TrimEnd('\', '/')
        if ([IO.Path]::GetFullPath($root).TrimEnd('\', '/') -ine $repoPath) {
            Write-Output '跳过：清单路径必须是仓库根目录'
            $failed = $true
            continue
        }
        $status = (& git -C $repo status --porcelain 2>&1 | Out-String).Trim()
        if ($LASTEXITCODE -ne 0 -or $status) {
            Write-Output '跳过：工作区或暂存区不干净'
            $failed = $true
            continue
        }
        $branch = (& git -C $repo branch --show-current 2>$null).Trim()
        if ($LASTEXITCODE -ne 0 -or -not $branch) {
            Write-Output '跳过：当前为 detached HEAD 或分支无效'
            $failed = $true
            continue
        }
        $operation = (& git -C $repo rev-parse --git-path rebase-merge 2>$null).Trim()
        $rebaseApply = (& git -C $repo rev-parse --git-path rebase-apply 2>$null).Trim()
        $mergeHead = (& git -C $repo rev-parse --git-path MERGE_HEAD 2>$null).Trim()
        if ((Test-Path (Join-Path $repo $operation)) -or (Test-Path (Join-Path $repo $rebaseApply)) -or (Test-Path (Join-Path $repo $mergeHead))) {
            Write-Output '跳过：存在进行中的 Git 操作'
            $failed = $true
            continue
        }
        & git -C $repo remote get-url $remote *> $null
        if ($LASTEXITCODE -ne 0) {
            Write-Output "跳过：remote 不存在：$remote"
            $failed = $true
            continue
        }
        & git -C $repo fetch $remote --prune
        if ($LASTEXITCODE -ne 0) {
            Write-Output '失败：fetch 未完成'
            $failed = $true
            continue
        }
        & git -C $repo show-ref --verify --quiet "refs/remotes/$remote/$base"
        if ($LASTEXITCODE -ne 0) {
            Write-Output "跳过：fetch 后找不到远程分支 $remote/$base"
            $failed = $true
            continue
        }
        & git -C $repo rebase "$remote/$base"
        if ($LASTEXITCODE -eq 0) {
            Write-Output "完成：当前分支 $branch 已基于 $remote/$base"
        } else {
            Write-Output '冲突或 rebase 失败：尝试 abort，需人工检查'
            & git -C $repo rebase --abort
            if ($LASTEXITCODE -eq 0) { Write-Output '已 abort，工作区回到 rebase 前状态' }
            else { Write-Output '严重：rebase --abort 失败，请立即检查仓库状态' }
            $failed = $true
        }
    }
} finally {
    Write-Output "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] 同步结束（failed=$failed）"
    Stop-Transcript | Out-Null
}
if ($failed) { exit 1 } else { exit 0 }
