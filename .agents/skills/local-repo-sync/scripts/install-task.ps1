param(
    [Parameter(Mandatory = $true)]
    [string]$Manifest,
    [ValidateRange(0, 23)]
    [int]$Hour = 8,
    [string]$TaskName = 'LocalRepoSyncDaily'
)
$ErrorActionPreference = 'Stop'
$manifestPath = (Resolve-Path -LiteralPath $Manifest).Path
$existingTask = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existingTask) { throw "任务已存在，未覆盖：$TaskName" }
$scriptPath = Join-Path $PSScriptRoot 'sync-repos.ps1'
$logDir = Join-Path $env:LOCALAPPDATA 'local-repo-sync'
$logPath = Join-Path $logDir 'sync.log'
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoLogo -NoProfile -ExecutionPolicy Bypass -File `"$scriptPath`" -Manifest `"$manifestPath`"" -WorkingDirectory $PSScriptRoot
$trigger = New-ScheduledTaskTrigger -Daily -At ([datetime]::Today.AddHours($Hour))
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Hours 2) -MultipleInstances IgnoreNew
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Limited
$task = New-ScheduledTask -Action $action -Trigger $trigger -Settings $settings -Principal $principal
Register-ScheduledTask -TaskName $TaskName -InputObject $task -Description "Fetch and rebase registered local Git repositories; never push." | Out-Null
Write-Output "已注册任务：$TaskName，每天本机时间 $Hour`:00"
Write-Output "清单：$manifestPath"
Write-Output "日志：$logPath"
Write-Output '注意：任务在用户登录时运行；Git 凭据需对该用户可用。'
