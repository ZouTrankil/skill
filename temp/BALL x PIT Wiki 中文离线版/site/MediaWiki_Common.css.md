# 站点代码 · Common.css

[原文](https://ballxpit.wiki.gg/wiki/MediaWiki:Common.css) · [修订 3577](https://ballxpit.wiki.gg/index.php?oldid=3577)

```css
/* CSS placed here will be applied to all skins */
@import url(https://fonts.googleapis.com/css?family=Press+Start+2P);
@import url('https://fonts.googleapis.com/css2?family=Forum&family=Jersey+10&display=swap');

/******************************************************************************************
********************************* Start user-edit variables *******************************
******************************************************************************************/

/*****************************************
****** START BASIC DESIGN VARIABLES ******
----------------------------------------*/
:root {
    --wiki-content-heading-font-family: 'Jersey 10', sans-serif;
	--wiki-sidebar-heading-font-family: sans-serif;
	
	--wiki-content-border-radius: 0px;
	--wiki-sidebar-border-radius: 0px;
}
/*----------------------------------------
******* END BASIC DESIGN VARIABLES *******
*****************************************/

/*****************************************
****** START BASIC COLOR VARIABLES *******
----------------------------------------*/
:root,
/* Begin dark styles, delete from here to "end dark styles" if you don't want your wiki to support any dark themes (remove it from [[Mediawiki:Theme-definitions]] too, or ask wiki.gg staff for help doing this) */
/* FYI: .view- will affect any theme marked |kind=dark, */
/* individual themes are prefixed with .theme- instead   */
.view-dark {
	/**********************
	* Probably edit these * [ DARK VIEW ]
	***********************/
	--wiki-body-background-color: #1e1819;
	--wiki-body-background-image: url(filepath://Background_pattern.png);

	--wiki-content-background-color: #281818;
	--wiki-content-background-opacity: 90%;
	--wiki-content-border-color: #825d26;

	--wiki-content-link-color: #b18f70; /* if changing this, remember to change --wiki-icon-to-link-filter as well!!! */
	/* [ DARK VIEW ] */
	--wiki-accent-color: #a27c5a;
	--wiki-accent-label-color: #000;
	--wiki-accent-link-color: #43210d;

	--wiki-icon-to-link-filter: invert(61%) sepia(12%) saturate(935%) hue-rotate(347deg) brightness(93%) contrast(93%); /* put your --wiki-content-link-color into https://mrpie5.gitlab.io/css-filter-generator/ */
	/**/
}

/* End dark styles */

/*----------------------------------------
******* END BASIC COLOR VARIABLES ********
*****************************************/

/*****************************************
**** START ADVANCED COLOR VARIABLES ******
----------------------------------------*/

:root,
.view-light {
	/*******************
	* Maybe edit these * [ LIGHT VIEW ]
	********************/
	--wiki-body-background-position: top center;
	--wiki-body-background-size: cover;
	--wiki-body-background-repeat: no-repeat;
	--wiki-body-background-attachment: fixed;

	--wiki-content-background-color--secondary: color-mix(in srgb, var(--wiki-content-background-color) 96%, var(--wiki-content-dynamic-color));
	--wiki-content-text-color: #111111;
	--wiki-content-link-color--visited: var(--wiki-content-link-color);
	--wiki-content-link-color--hover: var(--wiki-content-link-color);
	--wiki-content-redlink-color: #ba0000;

	--wiki-content-heading-color: var(--wiki-content-text-color);
	--wiki-content-heading-border-color: var(--wiki-content-border-color);

	/* [ LIGHT VIEW ] */
	--wiki-navigation-background-color: var(--wiki-content-background-color--secondary);
	--wiki-navigation-border-color: var(--wiki-navigation-selected-border-color);
	--wiki-navigation-text-color: var(--wiki-content-link-color);
	--wiki-navigation-selected-background-color: var(--wiki-content-background-color);
	--wiki-navigation-selected-border-color: var(--wiki-content-border-color);
	--wiki-navigation-selected-text-color: var(--wiki-content-text-color);

	/* [ LIGHT VIEW ] */
	--wiki-neutral-color: var(--wiki-content-text-mix-color);
	--wiki-alert-color: #bf0017;
	--wiki-warning-color: #b05f30;
	--wiki-success-color: #0c742f;
	/**/

	/***********************************
	* Likely do not need to edit these *  [ LIGHT VIEW ]
	************************************/
	--wiki-body-dynamic-color: #000000;
	--wiki-body-dynamic-color--inverted: #ffffff;
	--wiki-body-dynamic-color--secondary: #333333;
	--wiki-body-dynamic-color--secondary--inverted: #cccccc;

	--wiki-content-border-color--secondary: color-mix(in srgb, var(--wiki-content-border-color) 50%, transparent);
	--wiki-content-border-color--accent: color-mix(in srgb, var(--wiki-accent-color) 50%, transparent);
	--wiki-content-link-label-color: #ffffff;
	--wiki-content-dynamic-color: #000000;
	--wiki-content-dynamic-color--inverted: #ffffff;
	--wiki-content-dynamic-color--secondary: #333333;
	--wiki-content-dynamic-color--secondary--inverted: #cccccc;
	/* [ LIGHT VIEW ] */
	--wiki-alert-label-color: #ffffff;
	--wiki-warning-label-color: #ffffff;
	--wiki-success-label-color: #ffffff;

	--wiki-icon-general-filter: ; /* do not set this to none, ignore the "unexpected token" error */
	/**/
}

.view-dark {
	/*******************
	* Maybe edit these * [ DARK VIEW ]
	********************/
	--wiki-body-background-position: top left;
	--wiki-body-background-size: auto;
	--wiki-body-background-repeat: repeat;
	--wiki-body-background-attachment: scroll;

	--wiki-content-background-color--secondary: color-mix(in srgb, var(--wiki-content-background-color) 96%, var(--wiki-content-dynamic-color));
	--wiki-content-text-color: #ededed;
	--wiki-content-link-color--visited: var(--wiki-content-link-color);
	--wiki-content-link-color--hover: var(--wiki-content-link-color);
	--wiki-content-redlink-color: #FC5B4F;

	--wiki-content-heading-color: var(--wiki-content-text-color);
	--wiki-content-heading-border-color: var(--wiki-content-border-color);

	/* [ DARK VIEW ] */
	--wiki-navigation-background-color: var(--wiki-content-background-color--secondary);
	--wiki-navigation-border-color: var(--wiki-navigation-selected-border-color);
	--wiki-navigation-text-color: var(--wiki-content-link-color);
	--wiki-navigation-selected-background-color: var(--wiki-content-background-color);
	--wiki-navigation-selected-border-color: var(--wiki-content-border-color);
	--wiki-navigation-selected-text-color: var(--wiki-content-text-color);

	/* [ DARK VIEW ] */
	--wiki-neutral-color: var(--wiki-content-text-mix-color);
	--wiki-alert-color: #ff576a;
	--wiki-warning-color: #cf721c;
	--wiki-success-color: #13aa45;
	/**/

	/***********************************
	* Likely do not need to edit these * [ DARK VIEW ]
	************************************/
	--wiki-body-dynamic-color: #ffffff;
	--wiki-body-dynamic-color--inverted: #000000;
	--wiki-body-dynamic-color--secondary: #cccccc;
	--wiki-body-dynamic-color--secondary--inverted: #333333;

	--wiki-content-border-color--secondary: color-mix(in srgb, var(--wiki-content-border-color) 50%, transparent);
	--wiki-content-border-color--accent: color-mix(in srgb, var(--wiki-accent-color) 50%, transparent);
	--wiki-content-link-label-color: #000;
	--wiki-content-dynamic-color: #ffffff;
	--wiki-content-dynamic-color--inverted: #000000;
	--wiki-content-dynamic-color--secondary: #cccccc;
	--wiki-content-dynamic-color--secondary--inverted: #333333;
	/* [ DARK VIEW ] */
	--wiki-alert-label-color: #000000;
	--wiki-warning-label-color: #000000;
	--wiki-success-label-color: #000000;

	--wiki-icon-general-filter: invert(100%);
}

/*----------------------------------------
***** END ADVANCED COLOR VARIABLES *******
*****************************************/

/*****************************************
**** START ADVANCED DESIGN VARIABLES *****
----------------------------------------*/

:root {
	/***********************
	  start logo position 
	----------------------*/
	--wiki-is-top-logo: 0; /* 1 = center logo at the top of the page; 0 = logo at the top left of the page */
	
	--wiki-logo-file-width: 160; /* Width of the image file in px. Put a number without the letters `px`. */
	--wiki-logo-file-height: 160; /* Height of the image file in px. Put a number without the letters `px`. */	
	--wiki-logo-height: calc(var(--wiki-logo-file-height)*1px); /* Valid only when --wiki-is-top-logo is 1. The height the logo should be shown */
	--wiki-logo-margin: 15px; /* the width of margin below the logo. When --wiki-is-top-logo is 1, this is also the default value of --wiki-top-spacing */
	/*-----------------------
	   end logo position 
	***********************/
	
	--wiki-is-navigation-inside-content: 0; /* 0 = default navigation tabs layout; 1 = navigation tabs inside content box */

	--wiki-body-font-family: sans-serif;
	--wiki-content-firstheading-font-family: var(--wiki-content-heading-font-family); /* only apply to the main title of article */

	/****** the following length variables must have units specified even if 0, ignore the warning *****/
	
	--wiki-content-border-width: 1px;
	--wiki-sidebar-width: 10em; /* width of sidebar(#mw-panel) */
	--wiki-sidebar-portal-spacing: 1em;
	--wiki-sidebar-border-width: var(--wiki-content-border-width);
	--wiki-navigation-border-radius: 0px; /* border radius of tabs */

	/*******************
	* Maybe edit these * [ DESIGN ]
	********************/
	
	--wiki-logo-filter: none;
	
	/****** the following length variables must have units specified even if 0, ignore the warning *****/
	
	--wiki-content-border-top-radius: var(--wiki-content-border-radius);
	--wiki-content-border-style: solid;
	--wiki-content-border-image: url(filepath://Border_frame.png) 72 / 20px / 4px;
	--wiki-content-backdrop-filter: none;
	
	--wiki-page-content-max-width: 9999px; /* max width of sidebar+gap+content, must be a length value. A huge value can be used to indicate no limit, e.g. 99999px */
	--wiki-gap-between-sidebar-and-content: 1em; /* gap between sidebar(#mw-panel) and content(#content) */
	
	--wiki-sidebar-font-size: 0.75em; /* please use em or rem for this */
	--wiki-sidebar-line-height: 1.125;
	--wiki-sidebar-heading-font-size: 0.75em; /* please use em or rem for this */
	--wiki-sidebar-margin: 0em;
	--wiki-sidebar-list-item-padding: 0.25em 0.25rem;
	--wiki-sidebar-list-padding: 0.25rem;
	--wiki-sidebar-list-item-background--hover: none; /* background of hover item */

	--wiki-navigation-font-size: 0.8125em; /* please use em or rem for this */
	--wiki-navigation-font-weight: normal; 
	--wiki-navigation-selected-font-weight: var(--wiki-navigation-font-weight);
	--wiki-navigation-text-transform: none;
	--wiki-navigation-height: 2.75rem; /* height of navigation area,include spacing above tabs */
	--wiki-navigation-left-spacing: calc( (1 - var(--wiki-is-navigation-inside-content))*var(--wiki-content-border-radius) + var(--wiki-is-navigation-inside-content) * 0.5rem );
	--wiki-navigation-right-spacing: calc( var(--wiki-is-navigation-inside-content) * 0.5rem );
	--wiki-navigation-box-background-color: var(--wiki-content-background-color);
	--wiki-navigation-box-background-opacity: calc(var(--wiki-content-background-opacity)*0.8*var(--wiki-is-navigation-inside-content));
	--wiki-navigation-box-background: color-mix(in srgb, var(--wiki-navigation-box-background-color) var(--wiki-navigation-box-background-opacity), transparent); /* usually only needed when --wiki-is-navigation-inside-content is 1 */
	--wiki-navigation-box-border-image: url(filepath://Border_frame.png) 72 / 20px / 4px; /* usually only needed when --wiki-is-navigation-inside-content is 1 */
	--wiki-navigation-box-backdrop-filter: none; /* usually only needed when --wiki-is-navigation-inside-content is 1 */
	--wiki-navigation-selected-backdrop-filter: var(--wiki-content-backdrop-filter);  /* usually only needed when --wiki-is-navigation-inside-content is 0 */
	--wiki-navigation-backdrop-filter: var(--wiki-navigation-selected-backdrop-filter);  /* usually only needed when --wiki-is-navigation-inside-content is 0 */
	
	/* nav tabs style. The vector gradient is default. 
	 * If you want to customize the style of tabs, it's easier to start with the following settings:
	 *    --wiki-navigation-background-image: none;
	 *    --wiki-navigation-selected-background-image: none;
	 *    --wiki-navigation-selected-border-width: calc( (1 - var(--wiki-is-navigation-inside-content))*var(--wiki-content-border-width) + var(--wiki-is-navigation-inside-content) * 1px );
	 *    --wiki-navigation-selected-border-bottom-background: none;
	 *    --wiki-navigation-tab-spacing: 0.25em;
	 *    --wiki-navigation-tab-padding-top: 0.5em;
	 *    --wiki-navigation-tab-padding-bottom: 0.5em;
	 */
	--wiki-navigation-tab-spacing: 1em;
	--wiki-navigation-tab-padding-top: .5em;
	--wiki-navigation-tab-padding-x: 1em;
	--wiki-navigation-tab-padding-bottom: .5em;
 	--wiki-navigation-selected-border-width: 0px; /* border width of selected tabs */
	--wiki-navigation-border-width: var(--wiki-navigation-selected-border-width); /* border width of normal tabs */
	--wiki-navigation-border-image: url(filepath://Border_frame.png) 128 / 20px / 4px;
	--wiki-navigation-selected-border-image: var(--wiki-navigation-border-image);
	--wiki-navigation-background-image: linear-gradient(to bottom,transparent 0,var(--wiki-content-border-color) 100%), linear-gradient(to bottom,transparent 0,var(--wiki-content-border-color) 100%), linear-gradient(to top,var(--wiki-navigation-background-color) 0,var(--wiki-navigation-selected-background-color) 100%);
	--wiki-navigation-background-repeat: no-repeat, no-repeat, repeat-x;
	--wiki-navigation-background-position: left bottom, right bottom, left bottom;
	--wiki-navigation-background-size:  1px 100%, 1px 100%, 100%;
	--wiki-navigation-selected-background-image: linear-gradient(to bottom,transparent 0,var(--wiki-content-border-color) 100%), linear-gradient(to bottom,transparent 0,var(--wiki-content-border-color) 100%);
	--wiki-navigation-selected-background-repeat: no-repeat, no-repeat;
	--wiki-navigation-selected-background-position: left bottom, right bottom;
	--wiki-navigation-selected-background-size:  1px 100%, 1px 100%;
	--wiki-navigation-selected-border-bottom-background: linear-gradient(to right, var(--wiki-content-border-color) 0, var(--wiki-content-border-color) 1px, transparent 1px), linear-gradient(to left, var(--wiki-content-border-color) 0, var(--wiki-content-border-color) 1px, transparent 1px);
	
	/* affects the dropdown menu under More */
	--wiki-navigation-dropdown-text-color: var(--wiki-navigation-text-color);
	--wiki-navigation-dropdown-text-color--hover: var(--wiki-navigation-dropdown-text-color);
	--wiki-navigation-dropdown-font-size: var(--wiki-navigation-font-size); /* please use em or rem for this */
	--wiki-navigation-dropdown-border-width: 1px;
	--wiki-navigation-dropdown-border-radius: var(--wiki-navigation-border-radius);
	--wiki-navigation-dropdown-padding: 0.25em; /* padding of the dropdown menu box */
	--wiki-navigation-dropdown-item-padding: 0.625em; /* padding of each dropdown menu items */
	--wiki-navigation-dropdown-item-background--hover: none; /* background of hover item */
	--wiki-navigation-dropdown-border-image: none;
	--wiki-navigation-dropdown-backdrop-filter: none;
	--wiki-navigation-dropdown-box-shadow: none; /* box shadow */
	
	/* styles of the footer */
	--wiki-spacing-before-footer: 1em;
	--wiki-footer-border-image: url(filepath://Border_frame.png) 72 / 20px / 4px;

	/* padding on body element */
	--wiki-top-spacing: calc(var(--wiki-is-top-logo)*var(--wiki-logo-margin) + (1 - var(--wiki-is-top-logo))*1em); /* extra spacing below wiki.gg netbar */
	--wiki-left-spacing: 1em;
	--wiki-right-spacing: 1em;
	--wiki-bottom-spacing: 2em;

	/* pading on content-element */
	--wiki-content-top-spacing:1.25em;
	--wiki-content-left-spacing:1.5em;
	--wiki-content-right-spacing:1.5em;
	--wiki-content-bottom-spacing:1.5em;

	/* end design variables */
}

/*----------------------------------------
***** END ADVANCED DESIGN VARIABLES ******
*****************************************/


/*******************************
**** START SHARED VARIABLES ****
**** tl;dr: don't edit this ****
********************************/
/*
	These variables are rarely touched, usually inherit other variables, and are shared on all themes.
	In 99% of cases none of these are ever edited, and you should only be doing so if you have a very clear vision,
	understand what you are doing, and *know* that what you are trying to do is not accomplished by changing
	another variable in the above sections.
	Since these are by default shared across all themes, if you support multiple themes you'll probably want to
	separate the variables you want to modify here into .view-x blocks like above. If you don't understand
	what that means or how to do that then you probably shouldn't be modifying this section.
*/
:root {
	--wiki-content-border-bottom-width: var(--wiki-content-border-width);
	--wiki-content-border-bottom-style: var(--wiki-content-border-style);
	--wiki-content-border-bottom-color: var(--wiki-content-border-color);
	--wiki-content-text-mix-color: color-mix(in srgb, var(--wiki-content-background-color), var(--wiki-content-text-color) 62%);
	--wiki-content-text-mix-color-95: color-mix(in srgb, var(--wiki-content-background-color) 95%, var(--wiki-content-text-color));
	--wiki-content-text-color--hover: var(--wiki-content-text-color);

	/* heading */
	--wiki-content-heading-border-bottom-width: 1px;
	--wiki-content-heading-border-style: solid;
	--wiki-content-heading-font-weight: normal;
	--wiki-content-heading-font-style: normal;
	--wiki-content-heading-text-transform: none;
	--wiki-content-heading-line-height: normal;
	--wiki-content-heading-text-shadow: none;
	/* first heading (h1) */
	--wiki-content-firstheading-border-bottom-width: var(--wiki-content-heading-border-bottom-width);
	--wiki-content-firstheading-border-style: var(--wiki-content-heading-border-style);
	--wiki-content-firstheading-border-color: var(--wiki-content-heading-border-color);
	--wiki-content-firstheading-font-weight: var(--wiki-content-heading-font-weight);
	--wiki-content-firstheading-font-style: var(--wiki-content-heading-font-style);
	--wiki-content-firstheading-text-transform: var(--wiki-content-heading-text-transform);
	--wiki-content-firstheading-line-height: var(--wiki-content-heading-line-height);
	--wiki-content-firstheading-color: var(--wiki-content-heading-color);
	--wiki-content-firstheading-text-shadow: none;
	/* sub-heading (h3, h4, h5, h6) */
	--wiki-content-subheading-border-bottom-width: 0px;
	--wiki-content-subheading-border-style: var(--wiki-content-heading-border-style);
	--wiki-content-subheading-border-color: var(--wiki-content-heading-border-color);
	--wiki-content-subheading-font-family: var(--wiki-body-font-family);
	--wiki-content-subheading-font-weight: bold;
	--wiki-content-subheading-font-style: normal;
	--wiki-content-subheading-text-transform: none;
	--wiki-content-subheading-line-height: var(--wiki-content-heading-line-height);
	--wiki-content-subheading-color: var(--wiki-content-heading-color);
	--wiki-content-subheading-text-shadow: none;
	/* heading size */
	--wiki-content-firstheading-font-size: 2.5em;
	--wiki-content-heading-h2-font-size: 2em;
	--wiki-content-heading-h3-font-size: 1.2em;
	--wiki-content-heading-h4-font-size: 114%;
	--wiki-content-heading-h5-font-size: 108%;
	--wiki-content-heading-h6-font-size: 100%;

	--wiki-content-toc-background: var(--wiki-content-background-color--secondary);
	--wiki-content-toc-border-width: 1px;
	--wiki-content-toc-border-style: solid;
	--wiki-content-toc-border-color: var(--wiki-content-border-color);
	--wiki-content-toc-border-radius: 0px;
	--wiki-content-toc-border-image: none;
	--wiki-content-toc-box-shadow: 0 0.1em 0.2em #000000;

	--wiki-content-catlinks-background: var(--wiki-content-background-color--secondary);
	--wiki-content-catlinks-border-width: 1px;
	--wiki-content-catlinks-border-style: solid;
	--wiki-content-catlinks-border-color: var(--wiki-content-border-color);
	--wiki-content-catlinks-border-radius: 0px;
	--wiki-content-catlinks-border-image: none;
	--wiki-content-catlinks-box-shadow: none;

	--wiki-content-filetoc-background: var(--wiki-content-background-color--secondary);
	--wiki-content-filetoc-border-width: 1px;
	--wiki-content-filetoc-border-style: solid;
	--wiki-content-filetoc-border-color: var(--wiki-content-border-color);
	--wiki-content-filetoc-border-radius: 0px;
	--wiki-content-filetoc-border-image: none;
	--wiki-content-filetoc-box-shadow: none;

	--wiki-logo-offset-x: 0px;
	--wiki-logo-offset-y: 0px;
	
	--wiki-sidebar-padding: 0px;
	--wiki-sidebar-background-color: var(--wiki-content-background-color);
	--wiki-sidebar-background-opacity: var(--wiki-content-background-opacity);
	--wiki-sidebar-background-image: none;
	--wiki-sidebar-background-position: center;
	--wiki-sidebar-background-repeat: repeat;
	--wiki-sidebar-background-size: auto;
	--wiki-sidebar-box-shadow: none;
	--wiki-sidebar-filter: none;
	--wiki-sidebar-backdrop-filter: var(--wiki-content-backdrop-filter);
	--wiki-sidebar-border-color: var(--wiki-content-border-color);
	--wiki-sidebar-border-style: solid;
	--wiki-sidebar-border-image: url(filepath://Border_frame.png) 72 / 20px / 4px;
	--wiki-sidebar-link-color: var(--wiki-content-link-color);
	--wiki-sidebar-link-color--hover: var(--wiki-content-link-color--hover);
	--wiki-sidebar-heading-color: var(--wiki-content-heading-color);
	--wiki-sidebar-heading-font-weight: normal;
	--wiki-sidebar-heading-font-style: normal;
	--wiki-sidebar-heading-text-transform: none;
	--wiki-sidebar-heading-line-height: normal;
	--wiki-sidebar-heading-padding: 0.5rem 0.25rem 0.5rem 0.5rem;
	--wiki-sidebar-heading-margin: 0px 0px -0.5rem 0px;
	--wiki-sidebar-heading-background: none;
	--wiki-sidebar-heading-border-image: none;
	--wiki-sidebar-heading-text-shadow: none;
	--wiki-sidebar-list-background: none;
	--wiki-sidebar-list-border-image: url(filepath://Border_frame.png);
	--wiki-sidebar-list-margin: 0px;
	--wiki-sidebar-list-item-background: none;
	--wiki-sidebar-list-item-border-image: none;
	--wiki-sidebar-list-item-background--hover: none;
	--wiki-sidebar-list-item-border-image--hover: none;
	--wiki-sidebar-list-item-spacing: 0px;
	--wiki-sidebar-icon-to-link-filter: var(--wiki-icon-to-link-filter);
	--wiki-sidebar-offset: 1em; /* Vertical offset */
	--wiki-sidebar-box-padding: 0px;
	--wiki-sidebar-box-background: none;
	--wiki-sidebar-box-border: 0px;
	--wiki-sidebar-box-border-radius: 0px;
	--wiki-sidebar-box-border-image: none;
	
	--wiki-accent-color--hover: color-mix(in srgb, var(--wiki-accent-color) 90%, var(--wiki-accent-label-color));

	--wiki-footer-border-width: var(--wiki-content-border-width);
	--wiki-footer-border-style: var(--wiki-content-border-style);
	--wiki-footer-border-color: var(--wiki-content-border-color);
	--wiki-footer-background-color: var(--wiki-content-background-color);
	--wiki-footer-background-opacity: var(--wiki-content-background-opacity);
	--wiki-footer-backdrop-filter: var(--wiki-content-backdrop-filter);
	--wiki-footer-text-color: var(--wiki-content-text-color);
	--wiki-footer-link-color: var(--wiki-content-link-color);
	--wiki-footer-link-color--hover: var(--wiki-content-link-color--hover);
	--wiki-footer-border-radius: var(--wiki-content-border-radius);

	--wiki-navigation-background-opacity: var(--wiki-navigation-selected-background-opacity);
	--wiki-navigation-background-color--hover: var(--wiki-navigation-background-color);
	--wiki-navigation-background-opacity--hover: var(--wiki-navigation-background-opacity);
	--wiki-navigation-background-image--hover: var(--wiki-navigation-background-image);
	--wiki-navigation-background-position--hover: var(--wiki-navigation-background-position);
	--wiki-navigation-background-repeat--hover: var(--wiki-navigation-background-repeat);
	--wiki-navigation-background-size--hover: var(--wiki-navigation-background-size);
	--wiki-navigation-text-color--hover: var(--wiki-content-link-color--hover);
	--wiki-navigation-transform--hover: none;
	--wiki-navigation-selected-border-style: solid;
	--wiki-navigation-selected-background-opacity: var(--wiki-content-background-opacity);
	--wiki-navigation-border-style: solid;
	--wiki-navigation-border-color--hover: var(--wiki-navigation-border-color);
	--wiki-navigation-border-image--hover: var(--wiki-navigation-border-image);
	--wiki-navigation-border-bottom-color: transparent;
	--wiki-navigation-border-bottom-color--hover: var(--wiki-navigation-border-color--hover); /* change this color to transparent to make it behave like a selected tab */
	--wiki-navigation-border-bottom-style: var(--wiki-navigation-selected-border-style);
	--wiki-navigation-border-bottom-width: calc(var(--wiki-is-navigation-inside-content, 0) * var(--wiki-navigation-selected-border-width, 1px) + (1 - var(--wiki-is-navigation-inside-content, 0)) * var(--wiki-content-border-width, 1px));
	--wiki-navigation-icon-size: 1em;
	--wiki-navigation-tab-padding-x--icon: var(--wiki-navigation-tab-padding-x);
	--wiki-navigation-bottom-spacing: 0px; /* If you change this to greater than 0px, you should usually change the value of --wiki-navigation-selected-border-bottom-background to var(--wiki-navigation-border-bottom-color) */

	--wiki-navigation-dropdown-background-color: var(--wiki-content-background-color);
	--wiki-navigation-dropdown-background-opacity: var(--wiki-content-background-opacity);
	--wiki-navigation-dropdown-border-color: var(--wiki-navigation-border-color);
	--wiki-navigation-dropdown-offset: 0px; /* vertical offset */

	--wiki-navigation-search-background-color: var(--wiki-content-background-color--secondary);
	--wiki-navigation-search-background-image: none;
	--wiki-navigation-search-background-position: 0;
	--wiki-navigation-search-background-size: auto;
	--wiki-navigation-search-background-repeat: repeat;
	--wiki-navigation-search-backdrop-filter: none;
	--wiki-navigation-search-border-color: var(--wiki-navigation-border-color);
	--wiki-navigation-search-border-color--hover: var(--wiki-accent-color);
	--wiki-navigation-search-border-style: solid;
	--wiki-navigation-search-border-width: 1px;
	--wiki-navigation-search-border-radius: 2px;
	--wiki-navigation-search-border-image: url(filepath://Border_frame.png) 72 / 20px / 4px;
	--wiki-navigation-search-border-image--hover: var(--wiki-navigation-search-border-image);
	--wiki-navigation-search-box-shadow: none;
	--wiki-navigation-search-box-shadow--hover: var(--wiki-navigation-search-box-shadow);
	--wiki-navigation-search-text-color: var(--wiki-content-text-color);
	--wiki-navigation-search-font-size: var(--wiki-navigation-font-size);
	--wiki-navigation-search-height: 2em;
	--wiki-navigation-search-button-color: currentColor;
	--wiki-navigation-search-button-color--hover: var(--wiki-navigation-search-button-color);
	--wiki-navigation-search-button-color-opacity: 80%;
	--wiki-navigation-search-button-color-opacity--hover: 95%;
	--wiki-navigation-search-bottom-spacing: 3px;
	--wiki-navigation-search-highlight-background-color: color-mix(in srgb, var(--wiki-accent-color) 5%, transparent);
	--wiki-navigation-gap-between-left-and-right: calc(max(0px, var(--wiki-navigation-tab-spacing))); /* minimum width between #left-navigation and #right-navigation before tabs start to collapse */
}

/*** mobile adjustments ***/
@media screen and (max-width: 720px) {
	body.has-vector-mobile-menu{
		--wiki-sidebar-offset: 0px; /* Vertical offset */
		--wiki-sidebar-margin: 0px;
		--wiki-sidebar-heading-background: none;
		--wiki-sidebar-heading-border-image: url(filepath://Border_frame.png) 72 / 20px / 4px;
		--wiki-sidebar-heading-margin: 0px 0px -0.5em 0px;
		--wiki-sidebar-list-margin: 0px;
		--wiki-sidebar-list-background: none;
		--wiki-sidebar-list-border-image: url(filepath://Border_frame.png) 72 / 20px / 4px;
		--wiki-sidebar-list-item-background: none;
		--wiki-sidebar-list-item-border-image: none;
		--wiki-sidebar-list-item-background--hover: none;
		--wiki-sidebar-list-item-border-image--hover: none;
		--wiki-sidebar-list-item-spacing: 0px;
		--wiki-sidebar-line-height: 1.125;
		--wiki-sidebar-background-opacity: 100%;
		--wiki-navigation-search-border-width: 1px;
		--wiki-logo-offset-x: 0px;
		--wiki-logo-offset-y: 0px;
	}
}


/*****************************
**** END SHARED VARIABLES ****
******************************/

/******************************************************************************************
********************************* End user-edit variables *********************************
******************************************************************************************/

/******************************
* Fallback for older browsers *
* DONT EDIT THIS              *
*******************************/
@supports not (color:color-mix(in srgb, #000, transparent)) {
	.view-dark,
	.view-light,
	:root {
		--wiki-content-text-mix-color: var(--wiki-content-text-color);
		--wiki-content-text-mix-color-95: var(--wiki-content-background-color);
		--wiki-content-background-color--secondary: var(--wiki-content-dynamic-color--secondary--inverted);
		--wiki-content-border-color--secondary: var(--wiki-content-border-color);
		--wiki-content-border-color--accent: var(--wiki-accent-color);
		--wiki-accent-color--hover: var(--wiki-accent-color);
		--wiki-navigation-search-highlight-background-color: transparent;
	}
}

/*****************************
* End older browser fallback *
******************************/

/*****************************
*     PortableInfoboxes      *
******************************/
:root {
	--pi-background: var(--wiki-content-background-color);
	--pi-secondary-background: var(--wiki-accent-color);
	--pi-secondary-background-label: var(--wiki-accent-label-color);
	--pi-border-color: color-mix(in srgb, var(--pi-secondary-background) 50%, transparent);
}

.portable-infobox .pi-title,
.portable-infobox .pi-header {
	text-align: center;
	font-size: 1.5em;
	background: color-mix(in srgb, var(--pi-secondary-background) 75%, transparent);
	color: var(--pi-secondary-background-label);
}

.portable-infobox .pi-data,
.portable-infobox .pi-group {
	background: var(--wiki-content-background-color--secondary);
}

.portable-infobox .pi-image {
	padding: 8px;
}

.pi-image-thumbnail {
	max-width: 100%;
}

.pi-caption {
	color: var(--wiki-content-text-mix-color);
}

.pi-section-navigation .pi-section-tab.pi-section-active,
.pi-section-navigation .pi-section-tab.current,
.pi-media-collection .pi-tab-link.current {
	background: var(--pi-secondary-background);
	color: var(--pi-secondary-background-label);
}

.pi-collapse > .pi-item:first-child {
	cursor: pointer;
}

/* overqualify these to overwrite normal content heading styles */
.mw-body .portable-infobox h2,
.mw-body .portable-infobox h3 {
	border-bottom: 0;
	font-family: inherit;
	font-weight: 700;
	margin: 0;
}

/*****************************
*   End PortableInfoboxes    *
******************************/


/*******************
* Main page layout *
********************/

#mp-container {
	display: grid;
	gap: 10px;
	clear:both; /* for .mw-indicators combined with NOTITLE */
}

@media screen and (max-width: 990px) {
	/* for mobile screens */
	#mp-container {
		grid-template-areas:var(--main-page-layout--mobile);
		grid-template-columns:var(--main-page-layout-columns--mobile, 100%);
	}

	.mp-box.mp-hide-on-mobile {
		display: none;
	}
}

@media screen and (min-width: 990px) and (max-width: 1350px) {
	/* for narrow screens, between 990px and 1350px */
	#mp-container {
		grid-template-areas:var(--main-page-layout--tablet);
		grid-template-columns:var(--main-page-layout-columns--tablet, 1fr 1fr);
	}

	.mp-box.mp-hide-on-tablet {
		display: none;
	}
}

@media screen and (min-width: 1350px) {
	/* for all other screens, 1350px and wider */
	#mp-container {
		grid-template-areas:var(--main-page-layout--desktop);
		grid-template-columns:var(--main-page-layout-columns--desktop, 2fr 1fr 2fr);
	}

	.mp-box.mp-hide-on-desktop {
		display: none;
	}
}

.mp-box {
	position: relative;
	display: flex;
	flex-flow: column nowrap;
	width: 100%;
	box-sizing: border-box;
	background: color-mix(in srgb, var(--wiki-content-background-color--secondary) 25%, transparent);
	border: 1px solid var(--wiki-content-border-color);
	padding: 0px;
}

.mp-body {
	height: 100%;
	display: block !important;
	padding: 0.5em;
	flex-flow: column nowrap;
}

.mp-box.centered-content .mp-body {
	height: 100%;
	display: flex;
	flex-flow: column nowrap;
	justify-content: space-evenly;
}

.mp-box.has-floating-image {
	display: block;
}

.mp-box.has-floating-image .mp-body {
	height: unset;
	display: block;
}

.mp-box.header-only {
	border-bottom-width:0px;
}

.mp-box.header-only .mp-body {
	display:none;
}

.mp-box.missing .mw-inputbox-input {
	/* max-width doesn't override the input element's 'size' property, but that property does work as a max-width itself, so we can set width:100% for the same effect */
	width:100% !important;
}

/* overqualified to override normal heading styles */
.mw-body .mp-box h2 {
	text-align: center;
	font-weight: bold;
	font-family: var(--wiki-content-heading-font-family);
	overflow: initial;
	border-bottom: 1px solid var(--wiki-content-border-color);
	font-size: 150%;
	margin: 0;
	padding: 5px 0;
	color: var(--wiki-content-heading-color);
}

#mp-box-welcome {
	text-align: center;
	position: relative;
	overflow: hidden;
}

#mp-box-welcome h2 {
	font-size: 200%;
}

#mp-welcome {
	display: flex;
	flex-flow: column nowrap;
	position: relative;
	height: 100%;
	z-index: 2;
	box-sizing: border-box;
}

#mp-welcome .welcome-subtitle {
	height: 100%;
	background: color-mix(in srgb, var(--wiki-content-dynamic-color--inverted) 85%, transparent);
	padding: 0.5em;
}

#mp-banner {
	position: absolute;
	width: 100%;
	height: 100%;
	filter: blur(5px);
	z-index: -1;
	background: url(filepath://MP_banner.jpg);
	background-size: cover;
	background-repeat: no-repeat;
	background-position: top center;
}

.view-dark #mp-banner {
	filter: blur(5px) brightness(50%);
}

.view-light #mp-banner {
	filter: blur(5px) contrast(50%);
}

/* [[Template:MP_link]] */
.mp-links {
	--gap: 10px;
}

.mp-links > ul {
	display: flex;
	flex-flow: row wrap;
	justify-content: space-evenly;
	margin: 2px;
	gap: var(--gap);
}

.mp-links > ul > li {
	display: flex;
	flex-flow: column nowrap;
	align-items: stretch;
	text-align: center;
	box-sizing: border-box;
	flex: max(calc(50% - var(--gap)), 5em) 1 1;
	outline: 1px solid var(--wiki-content-link-color);
	transition: 0.1s ease-in;
}

.mp-links > ul > li:hover {
	background-color: color-mix(in srgb, var(--wiki-content-link-color) 20%, transparent);
}

.mp-links.columns-1 > ul > li {flex: max(calc(100% - var(--gap)), 5em) 1 1;}
.mp-links.columns-2 > ul > li {flex: max(calc(50% - var(--gap)), 5em) 1 1;}
.mp-links.columns-3 > ul > li {flex: max(calc((100% / 3) - var(--gap)), 5em) 1 1;}
.mp-links.columns-4 > ul > li {flex: max(calc(25% - var(--gap)), 5em) 1 1;}
.mp-links.columns-5 > ul > li {flex: max(calc(20% - var(--gap)), 5em) 1 1;}
.mp-links.columns-6 > ul > li {flex: max(calc((100% / 6) - var(--gap)), 5em) 1 1;}
.mp-links.columns-7 > ul > li {flex: max(calc((100% / 7) - var(--gap)), 5em) 1 1;}
.mp-links.columns-8 > ul > li {flex: max(calc((100% / 8) - var(--gap)), 5em) 1 1;}
.mp-links.columns-max > ul > li {flex: max(calc(0% - var(--gap)), 5em) 1 1;}

.mp-links > ul > li:hover a {
	text-decoration: underline;
}

.mp-links > ul > li > a {
	display: flex;
	align-items: center;
	justify-content: center;
	height: 100%;
	flex: 1 1 auto;
	box-sizing: border-box;
	padding: 5px;
}

.mp-links > ul > li > a:first-child {
	height: 100%;
}

.mp-links > ul > li > a:last-child:not(:first-child) {
	height: unset;
}

.mp-links.stretch,
.mp-links.stretch > ul {
	height: 100%;
}

.mp-links.side-image li {
	flex-flow: row nowrap;
}

.mp-links.plain > ul > li {
	outline-color: transparent;
}

/***********************
* End main page layout *
************************/

/** as of Module:navbox version 1.2.2 **/

/*********************************************************************************************************************
* Semantically-correct horizontal lists (for Module:Navbox, and they're more machine-readable than {{*}}-formatting) *
**********************************************************************************************************************/
.hlist dl,
.hlist ol,
.hlist ul {
	margin: 0;
	padding: 0;
}

/* Display list items inline */
.hlist dd,
.hlist dt,
.hlist li {
	/*
	 * don't trust the note that says margin doesn't work with inline
	 * removing margin: 0 makes dds have margins again
	 * We also want to reset margin-right in Minerva
	 */
	margin: 0; 
	display: inline;
}

/* Display requested top-level lists inline */
.hlist.inline,
.hlist.inline dl,
.hlist.inline ol,
.hlist.inline ul,
/* Display nested lists inline */
.hlist dl dl,
.hlist dl ol,
.hlist dl ul,
.hlist ol dl,
.hlist ol ol,
.hlist ol ul,
.hlist ul dl,
.hlist ul ol,
.hlist ul ul {
	display: inline;
}

/* Hide empty list items */
.hlist .mw-empty-li {
	display: none;
}

/* TODO: :not() can maybe be used here to remove the later rule. naive test
 * seems to work. more testing needed. like so: */
.hlist dt:not(:last-child)::after {
	content: ":\20";
}
.hlist dd:not(:last-child)::after,
.hlist li:not(:last-child)::after {
	/* "space, Middle Dot, space" 
	We use unicode numbers instead of the raw characters due to a Firefox encoding bug on unicode characters.
	The space is also encoded because raw spaces combined with a unicode number strips the spaces under some conditions such as single-line lists */
	/* content: "\20\00B7\20"; font-weight: bold; */
    /* "space &nbsp; • &nbsp; space" 
       There may (and likely) be an extra whitespace between <li>s, 
       therefore we have to use a space character as last character of this sequence. 
       By this way, the last space and the next whitespce will collapse as a single space,
       to make the whitespace on both sides of the middle dot the same width.
    */
	content: "\20\A0\2022\A0\20"; 
	font-weight: inherit;
}

/* Add parentheses around nested lists */
.hlist dd ol::before,
.hlist dd ul::before,
.hlist dd dl::before,
.hlist dt ol::before,
.hlist dt ul::before,
.hlist dt dl::before,
.hlist li ol::before,
.hlist li ul::before,
.hlist li dl::before {
	content: "\20(";
	font-weight: inherit;
}

.hlist dd ol::after,
.hlist dd ul::after,
.hlist dd dl::after,
.hlist dt ol::after,
.hlist dt ul::after,
.hlist dt dl::after,
.hlist li ol::after,
.hlist li ul::after,
.hlist li dl::after {
	content: ")";
	font-weight: inherit;
}

/* Put ordinals in front of ordered list items */
.hlist ol {
	counter-reset: listitem;
}

.hlist ol > li {
	counter-increment: listitem;
}

.hlist ol > li::before {
	content: " " counter(listitem) ".\20";
}

/* Progressive enhancement:
 * try to make the dot always follow the list item in same line
 */
.hlist :is(li,dt,dd):not(:has(:is(li,dt,dd))){
	display: inline-block;
}

/********************************************
* End semantically-correct horizontal lists *
*********************************************/

/*********************************************************************************************************************
* Semantically-correct horizontal lists (for Module:Navbox, and they're more machine-readable than {{*}}-formatting) *
**********************************************************************************************************************/
.hlist dl,
.hlist ol,
.hlist ul {
	margin: 0;
	padding: 0;
}

/* Display list items inline */
.hlist dd,
.hlist dt,
.hlist li {
	/*
	 * don't trust the note that says margin doesn't work with inline
	 * removing margin: 0 makes dds have margins again
	 * We also want to reset margin-right in Minerva
	 */
	margin: 0;
	display: inline;
}

/* Display requested top-level lists inline */
.hlist.inline,
.hlist.inline dl,
.hlist.inline ol,
.hlist.inline ul,
	/* Display nested lists inline */
.hlist dl dl,
.hlist dl ol,
.hlist dl ul,
.hlist ol dl,
.hlist ol ol,
.hlist ol ul,
.hlist ul dl,
.hlist ul ol,
.hlist ul ul {
	display: inline;
}

/* Hide empty list items */
.hlist .mw-empty-li {
	display: none;
}

/* TODO: :not() can maybe be used here to remove the later rule. naive test
*  seems to work. more testing needed. like so: */
.hlist dt:not(:last-child)::after {
	content: ":\20";
}

.hlist dd:not(:last-child)::after,
.hlist li:not(:last-child)::after {
	/* "space, Middle Dot, space"
	We use unicode numbers instead of the raw characters due to a Firefox encoding bug on unicode characters.
	The space is also encoded because raw spaces combined with a unicode number strips the spaces under some conditions such as single-line lists */
	/* content: "\20\00B7\20"; font-weight: bold; */
	/* "space &nbsp; • &nbsp; space"
	   There may (and likely) be an extra whitespace between <li>s,
	   therefore we have to use a space character as last character of this sequence.
	   By this way, the last space and the next whitespace will collapse as a single space,
	   to make the whitespace on both sides of the middle dot the same width.
	*/
	content: "\20\A0\2022\A0\20";
	font-weight: inherit;
}

/* Add parentheses around nested lists */
.hlist dd ol::before,
.hlist dd ul::before,
.hlist dd dl::before,
.hlist dt ol::before,
.hlist dt ul::before,
.hlist dt dl::before,
.hlist li ol::before,
.hlist li ul::before,
.hlist li dl::before {
	content: "\20(";
	font-weight: inherit;
}

.hlist dd ol::after,
.hlist dd ul::after,
.hlist dd dl::after,
.hlist dt ol::after,
.hlist dt ul::after,
.hlist dt dl::after,
.hlist li ol::after,
.hlist li ul::after,
.hlist li dl::after {
	content: ")";
	font-weight: inherit;
}

/* Put ordinals in front of ordered list items */
.hlist ol {
	counter-reset: listitem;
}

.hlist ol > li {
	counter-increment: listitem;
}

.hlist ol > li::before {
	content: " " counter(listitem) ".\20";
}

/* Progressive enhancement:
*  try to make the dot always follow the list item in same line
*/
.hlist :is(li,dt,dd):not(:has(:is(li,dt,dd))) {
	display: inline-block;
}

/********************************************
* End semantically-correct horizontal lists *
*********************************************/

/*** Miscellaneous ***/
.responsive-image {
	max-width: 100%;
	height: auto;
	box-sizing: border-box;
}

.view-dark .invert-on-dark,
.view-light .invert-on-light {
	filter: invert(100%);
}

.pixelated {
	image-rendering: pixelated;
}

@media screen and (min-width: 720px) {
	.mobileonly {
		display: none;
	}
}

@media screen and (max-width: 720px) {
	.nomobile {
		display: none;
	}
}

/*** Utility classes for standard MW galleries ***/
/* it's important that spaced comes before centered in the sheet */
.gallery.gallery.gallery.spaced { /* this selector looks ridiculous but is actually part of stock Vector and therefore a necessary override */
	display: flex;
	flex-flow: row wrap;
	justify-content: space-evenly;
	margin-left: unset;
}

.gallery.centered {
	text-align: center;
}

/**************************
* Start Modular Templates *
**************************/

/********* [[Template:Ambox]] *********/
.ambox {
	--ambox-color: var(--wiki-accent-color);

	border: 1px solid var(--wiki-content-border-color);
	border-left: 10px solid var(--ambox-color);
	border-radius: 2px;
	display: flex;
	align-items: center;
	gap: .6em;
	margin: 1em 0;
	padding: 3px .6em;
	background-color: var(--wiki-content-background-color--secondary);
	box-shadow: 2px 2px 5px 0px #0002;
}

@media (min-width: 720px) {
	.ambox {
		margin-inline: 10%;
	}
}

.ambox.tiny {
	padding: .04rem .5em;
	margin-inline: 0;
	width: fit-content;
}

.ambox + .ambox {
	margin-top: -.6em;
}

.ambox-content {
	flex: 1;
}

.ambox-content p {
	margin: .15em 0;
}

.ambox-title {
	font-weight: bold;
}

/********* [[Template:Hatnote]] *********/
.hatnote {
	padding: 1px 0 1px 1.6em;
	margin-bottom: 0.5em;
	font-style: italic;
	border-top: 1px solid var(--wiki-content-border-color--secondary);
	border-bottom: 1px solid var(--wiki-content-border-color--secondary);
}

.hatnote.icon {
	padding-left: 0;
}

/********* [[Template:Spoiler]] *********/
.spoiler-content {
	background-color: color-mix(in srgb, var(--wiki-content-dynamic-color) 50%, transparent);
	transition: all 0.3s;
	cursor: pointer;
	overflow: auto;
}

@supports not (color:color-mix(in srgb, #000, transparent)) {
	.spoiler-content {
		background-color: var(--wiki-content-dynamic-color--secondary);
	}	
}

.spoiler-content > * {
	pointer-events: none;
	opacity: 0;
	transition: all 0.3s;
}

.spoiler-content.show {
	background-color: transparent;
}

.spoiler-content.show > * {
	pointer-events: unset;
	opacity: 1;
}

/********* [[Template:Link icon]] *********/
.link-icon {
	--link-icon-line-height: 1.5em;
	--link-icon-size: 1.5em;
	display: inline-flex;
	align-items: center;
	height: var(--link-icon-line-height);
	vertical-align: bottom;
}

.link-icon .regular {
	align-self: center;
}

.link-icon .regular a {
	display: flex;
}

.link-icon .regular img {
	height: var(--link-icon-size);
	max-width: var(--link-icon-size);
}

.link-icon .fallback {
	outline: 1px solid var(--wiki-content-text-color);
	border-radius: 50%;
	text-align: center;
	width: var(--link-icon-size);
	line-height: var(--link-icon-size);
}

.link-icon.notext,
.link-icon.notext .fallback {
	display: inline-block;
}

/********* [[Template:Quote]] *********/
.quote {
	background: var(--wiki-content-background-color--secondary);
	border-radius: 5px;
	border: 2px solid var(--wiki-content-border-color);
	margin: .5em 0;
	padding: .5em;
	overflow-y: hidden;
}

.quote .block {
	display: block;
}

.quote .title {
	font-size: large;
	font-weight: bold;
}

.quote .content {
	font-style: italic;
}

.quote .author {
	font-weight: bold;
	text-align: end;
}

.quote .marks-wrapper {
	display: flex;
	gap: 5px;
}

.quote .marks-wrapper::before,
.quote .marks-wrapper::after {
	font-size: 100px;
	line-height: 0px;
}

.quote .marks-wrapper::before {
	content: "\201C";
	margin-top: 40px;
}

.quote .marks-wrapper::after {
	content: "\201D";
	align-self: end;
	margin-bottom: -10px;
}

.client-js .mw-charinsert-item {
	display: none;
}

/************************
* End Modular Templates *
*************************/

/*****************************
* Used by [[Template:Color]] *
******************************/
.color__splotch {
	display: inline-block;
	height: 1em;
	width: 1em;
	box-sizing: border-box;
	vertical-align: text-top;
	border-radius: 50%;
	border: 1px solid var(--wiki-content-text-color);
}

/*********************
* End Template:Color *
**********************/

/*********************************
* Used by [[Template:TOC limit]] *
**********************************/
.toclimit-2 .toclevel-1 ul,
.toclimit-3 .toclevel-2 ul,
.toclimit-4 .toclevel-3 ul,
.toclimit-5 .toclevel-4 ul,
.toclimit-6 .toclevel-5 ul,
.toclimit-7 .toclevel-6 ul {
	display: none;
}
/*************************
* End Template:TOC limit *
**************************/

/*********************************
* Used by [[Template:TOC right]] *
**********************************/
@media all and (min-width: 720px) {
	.tocright {
		float: right;
		clear: right;
		margin: 0 0 0.5em 1em; 
	}
}
/*************************
* End Template:TOC right *
**************************/

/**********************************************************
* Template:Navbox (RANGER) (needs semantic horizontal lists above) *
***********************************************************/
.ranger-navbox{
  --navbox-background: none; /* for entire navbox */
  --navbox-margin: 0.5em auto;
  --navbox-padding: 4px;
  --navbox-gap: 3px; /* when using zero-value, it must be 0px */
  --navbox-outer-border-color: var(--wiki-content-border-color--accent);
  --navbox-outer-border-width: 1px;
  --navbox-outer-border-style: solid;
  --navbox-outer-border-radius: 0px;
  --navbox-font-size: calc(1em - 2px);
  --navbox-title-color: var(--wiki-accent-label-color);
  --navbox-title-font-size: calc(125%);
  --navbox-title-background: var(--wiki-accent-color);
  --navbox-title-icon-color: var(--wiki-accent-label-color);
  --navbox-title-link-color: var(--navbox-title-color);
  --navbox-title-link-color--visited: var(--navbox-title-link-color);
  --navbox-title-link-color--hover: var(--wiki-accent-link-color);
  --navbox-title-redlink-color: var(--navbox-title-link-color);
  --navbox-title-link-decoration: underline solid;
  --navbox-title-redlink-decoration: underline wavy;
  --navbox-title-padding--y: 0.5em;
  --navbox-above-background: color-mix(in srgb, var(--wiki-content-text-color) 15%, transparent);
  --navbox-above-color: var(--wiki-content-text-color);
  --navbox-above-padding: var(--navbox-list-padding);
  --navbox-below-background: var(--navbox-above-background);
  --navbox-below-color: var(--navbox-above-color);
  --navbox-below-padding: var(--navbox-above-padding);
  --navbox-header-color: var(--navbox-title-color);
  --navbox-header-font-size: calc(110%);
  --navbox-header-background: var(--navbox-title-background);
  --navbox-header-icon-color: var(--navbox-title-icon-color);
  --navbox-header-link-color: var(--navbox-title-link-color);
  --navbox-header-link-color--visited: var(--navbox-title-link-color--visited);
  --navbox-header-link-color--hover: var(--navbox-title-link-color--hover);
  --navbox-header-redlink-color: var(--navbox-title-redlink-color);
  --navbox-header-link-decoration: var(--navbox-title-link-decoration);
  --navbox-header-redlink-decoration: var(--navbox-title-redlink-decoration);
  --navbox-header-padding--y: 0.3em;
  --navbox-subheader-font-size: calc(100%);
  --navbox-subheader-padding--y: calc(var(--navbox-header-padding--y)/2);
  --navbox-list-background: color-mix(in srgb, var(--wiki-content-text-color) 5%, transparent);
  --navbox-list-background--striped: color-mix(in srgb, var(--wiki-content-text-color) 8%, transparent);
  --navbox-list-color: var(--wiki-content-text-color);
  --navbox-list-padding: 0.25em 0.5em;
  /* --navbox-group-* also apply to .ranger-subgroup */
  --navbox-group-text-align: left;
  --navbox-group-text-align--mobile: left; /* only for mobile view */
  --navbox-group-background: color-mix(in srgb, var(--wiki-accent-color) 20%, transparent);
  --navbox-group-color: var(--wiki-content-text-color);
  --navbox-group-padding: var(--navbox-list-padding);
  --navbox-tree-line-color: color-mix(in srgb, var(--wiki-accent-color) 30%, transparent);
  --navbox-tree-line-width: 2px;
  --navbox-tree-indent: 1em;
  --navbox-tree-line-indent: 0.5em;
  --navbox-tree-line-spacing: var(--navbox-gap);
  --icon-chevron-down: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' class='icon icon-tabler icon-tabler-chevron-down' width='24' height='24' viewBox='0 0 24 24' stroke-width='2' stroke='currentColor' fill='none' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath stroke='none' d='M0 0h24v24H0z' fill='none'%3E%3C/path%3E%3Cpath d='M6 9l6 6l6 -6'%3E%3C/path%3E%3C/svg%3E");
  --icon-metalinks: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' class='icon icon-tabler icon-tabler-edit' width='24' height='24' viewBox='0 0 24 24' stroke-width='2' stroke='currentColor' fill='none' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath stroke='none' d='M0 0h24v24H0z' fill='none'%3E%3C/path%3E%3Cpath d='M7 7h-1a2 2 0 0 0 -2 2v9a2 2 0 0 0 2 2h9a2 2 0 0 0 2 -2v-1'%3E%3C/path%3E%3Cpath d='M20.385 6.585a2.1 2.1 0 0 0 -2.97 -2.97l-8.415 8.385v3h3l8.385 -8.415z'%3E%3C/path%3E%3Cpath d='M16 5l3 3'%3E%3C/path%3E%3C/svg%3E");
  --navbox-icon-offset--x: 0.5rem; /* should be an absolute length (rem-based or px-based) */
}
.ranger-navbox.pill, 
.ranger-navbox.pill-mobile{
  /** vars for the "pill" style only (`.pill` and ".pill-mobile" clases) **/
  --navbox-pill-gap: 0.3em;
  --navbox-pill-padding: 0.25em 0.75em;
  --navbox-pill-border-radius: 3px;
  --navbox-pill-box-shadow: none;
  --navbox-pill-background: color-mix(in srgb, var(--wiki-content-text-color) 5%, transparent);
  --navbox-pill-box-shadow--hover: inset 0 0 3px var(--navbox-list-color);
  --navbox-pill-background--hover: var(--navbox-pill-background);
  /* remove list cell background */
  --navbox-list-background: none;
  --navbox-list-background--striped: color-mix(in srgb, var(--wiki-content-text-color) 3%, transparent);
}
.ranger-navbox.no-underline-title-links{
  --navbox-title-link-color: var(--wiki-accent-link-color);
  --navbox-title-link-decoration: none;
  --navbox-title-redlink-decoration: none;
}
.ranger-navbox.noborder,
.ranger-navbox.no-border{
  --navbox-padding: 0px;
  --navbox-outer-border-width: 0px;
}

/******************************
* Fallback for older browsers *
*******************************/
@supports not (color:color-mix(in srgb, #000, transparent)) {
	.ranger-navbox {
		--navbox-above-background: var(--wiki-content-background-color--secondary);
		--navbox-list-background: transparent;
		--navbox-list-background--striped: var(--wiki-content-background-color--secondary);
		--navbox-group-background: var(--wiki-content-background-color--secondary);
		--navbox-tree-line-color：var(--wiki-content-background-color--secondary);
	}
	.ranger-navbox.pill, 
	.ranger-navbox.pill-mobile {
	  --navbox-pill-background: var(--wiki-content-background-color--secondary);
	  --navbox-list-background--striped: transparent;
	}
}
/***************
* End fallback *
****************/

.ranger-navbox{
  border-color: var(--navbox-outer-border-color);
  border-style: var(--navbox-outer-border-style);
  border-width: var(--navbox-outer-border-width);
  border-radius: var(--navbox-outer-border-radius);
  padding: var(--navbox-padding);
  font-size: var(--navbox-font-size);
  margin: var(--navbox-margin);
  background: var(--navbox-background);
  line-height: 1.5;
  clear:both;
}

.ranger-navbox * {
  border: 0;
}
.ranger-navbox .center *{
  margin-left: unset;
  margin-right: unset;
}
.ranger-navbox, 
.ranger-navbox .ranger-section,
.ranger-navbox .ranger-listbox{
  display: flex;
  flex-direction: column;
  gap: var(--navbox-gap);
}
.ranger-navbox .ranger-title,
.ranger-navbox .ranger-header{
  text-align: center;
  min-height: 1.5em;
  position: relative;
  z-index: 0;
  font-weight: bold;
}
.ranger-navbox .ranger-title{
  color: var(--navbox-title-color);
  background: var(--navbox-title-background);
  font-size: var(--navbox-title-font-size);
  padding: var(--navbox-title-padding--y) calc(1.5em + var(--navbox-icon-offset--x)); /* left and right padding equal to the size and position of the edit/collapse buttons */
}
.ranger-navbox .ranger-title a,
.ranger-navbox .ranger-title a:visited,
.ranger-navbox .ranger-title a:hover,
.ranger-navbox .ranger-title a.external,
.ranger-navbox .ranger-title a.external:visited,
.ranger-navbox .ranger-title a.external:hover {
	text-decoration: var(--navbox-title-link-decoration);
}
.ranger-navbox .ranger-title a.new,
.ranger-navbox .ranger-title a.new:visited {
	text-decoration: var(--navbox-title-redlink-decoration);
}
.ranger-navbox .ranger-title a,
.ranger-navbox .ranger-title a.external,
.ranger-navbox .ranger-title a.external:visited {
  color: var(--navbox-title-link-color);
}
.ranger-navbox .ranger-title a:visited{
  color: var(--navbox-title-link-color--visited);
}
.ranger-navbox .ranger-title a.new,
.ranger-navbox .ranger-title a.new:visited{
    color:var(--navbox-title-redlink-color);
}
.ranger-navbox .ranger-title a:hover,
.ranger-navbox .ranger-title a:visited:hover,
.ranger-navbox .ranger-title a.external:hover,
.ranger-navbox .ranger-title a.external:visited:hover {
  color:var(--navbox-title-link-color--hover);
}
.ranger-navbox .ranger-header{
  color: var(--navbox-header-color);
  background: var(--navbox-header-background);
  font-size: var(--navbox-header-font-size);
  padding: var(--navbox-header-padding--y) calc(1.5em + var(--navbox-icon-offset--x)); /* left and right padding equal to the size and position of the edit/collapse buttons */
}
.ranger-navbox .ranger-sublist .ranger-header{
  font-size: var(--navbox-subheader-font-size);
  padding: var(--navbox-subheader-padding--y) calc(1.5em + var(--navbox-icon-offset--x)); /* left and right padding equal to the size and position of the edit/collapse buttons */
}
.ranger-navbox .ranger-header a,
.ranger-navbox .ranger-header a:visited,
.ranger-navbox .ranger-header a:hover,
.ranger-navbox .ranger-header a.external,
.ranger-navbox .ranger-header a.external:visited,
.ranger-navbox .ranger-header a.external:hover {
	text-decoration: var(--navbox-header-link-decoration);
}
.ranger-navbox .ranger-header a.new,
.ranger-navbox .ranger-header a.new:visited {
	text-decoration: var(--navbox-header-redlink-decoration);
}
.ranger-navbox .ranger-header a,
.ranger-navbox .ranger-header a.external,
.ranger-navbox .ranger-header a.external:visited {
  color: var(--navbox-header-link-color);
}
.ranger-navbox .ranger-header a:visited{
  color: var(--navbox-header-link-color--visited);
}
.ranger-navbox .ranger-header a.new,
.ranger-navbox .ranger-header a.new:visited{
    color:var(--navbox-header-redlink-color);
}
.ranger-navbox .ranger-header a:hover,
.ranger-navbox .ranger-header a:visited:hover,
.ranger-navbox .ranger-header a.external:hover,
.ranger-navbox .ranger-header a.external:visited:hover {
  color:var(--navbox-header-link-color--hover);
}
.ranger-navbox .ranger-meta{
  font-size: var(--navbox-title-font-size);
  position: absolute;
  left: var(--navbox-icon-offset--x);
  top: calc(var(--navbox-title-padding--y) + 0.08em); /* 0.08em: vertial offset tweak based on the icon graph */
  display: block;
}
.ranger-navbox .ranger-meta .nv{
  --mask: var(--icon-metalinks);
  display: block;
  width: 0.84em; /* based on the icon graph */
  height: 0.84em;
  -webkit-mask: var(--mask);
  mask: var(--mask);
  -webkit-mask-size: 100% 100%;
  mask-size: 100% 100%;
  -webkit-mask-position: center center;
  mask-position: center center;
  background-color: var(--navbox-title-icon-color);
}
.ranger-navbox .ranger-meta .nv > a{
  display: block;
  width: 100%;
  height: 100%;
  opacity: 0;
}
.ranger-navbox .ranger-meta .nv > a > span{
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
}
.ranger-navbox .ranger-meta:has(.mw-selflink){
	display: none;
}
.ranger-navbox,
.ranger-navbox .ranger-section{
  position: relative;
}
.ranger .mw-collapsible-toggle-placeholder{
  display: none;
}
.ranger-navbox .ranger-title > .ranger-title-text,
.ranger-navbox .ranger-header > .ranger-header-text{
  pointer-events: none;
}
.ranger-navbox .ranger-title > .ranger-title-text a,
.ranger-navbox .ranger-header > .ranger-header-text a{
  pointer-events: auto;
}
.ranger-navbox .ranger-title > .mw-collapsible-toggle,
.ranger-navbox .ranger-header > .mw-collapsible-toggle{
  --mask: var(--icon-chevron-down);
  position: absolute;
  right: 0;
  top: 0;
  z-index: -1;
  display: block;
  width: 100%;
  height: 100%;
  overflow:hidden;
}
.ranger-navbox.small-collapsible-toggle-click-area .ranger-title > .mw-collapsible-toggle,
.ranger-navbox.small-collapsible-toggle-click-area .ranger-header > .mw-collapsible-toggle{
  width: 1.5em;
  height: 1.5em;
  right: var(--navbox-icon-offset--x);
}
.ranger-navbox.small-collapsible-toggle-click-area .ranger-title > .mw-collapsible-toggle{
  top: var(--navbox-title-padding--y);
}
.ranger-navbox.small-collapsible-toggle-click-area .ranger-header > .mw-collapsible-toggle{
  top: var(--navbox-header-padding--y);
}
.ranger-navbox.small-collapsible-toggle-click-area .ranger-sublist .ranger-header > .mw-collapsible-toggle{
  top: var(--navbox-subheader-padding--y);
}
.ranger-navbox .ranger-title > .mw-collapsible-toggle::before,
.ranger-navbox .ranger-header > .mw-collapsible-toggle::before{
  content: "";
  display: block;
  width: 1.5em;
  height: 1.5em;
  position: absolute;
  right: var(--navbox-icon-offset--x);
  -webkit-mask: var(--mask);
  mask: var(--mask);
  -webkit-mask-size: 100% 100%;
  mask-size: 100% 100%;
  -webkit-mask-position: center center;
  mask-position: center center;
  background-color: var(--navbox-title-icon-color);
  transform: scaleY(-1);
}
.ranger-navbox .ranger-title > .mw-collapsible-toggle::before{
  top: var(--navbox-title-padding--y);
}
.ranger-navbox .ranger-header > .mw-collapsible-toggle::before{
  top: var(--navbox-header-padding--y);
}
.ranger-navbox .ranger-sublist .ranger-header > .mw-collapsible-toggle::before{
  top: var(--navbox-subheader-padding--y);
}
.ranger-navbox.small-collapsible-toggle-click-area .ranger-title > .mw-collapsible-toggle::before,
.ranger-navbox.small-collapsible-toggle-click-area .ranger-header > .mw-collapsible-toggle::before{
  top: 0;
  right: 0;
}
.ranger-navbox .ranger-header > .mw-collapsible-toggle::before{
  background-color: var(--navbox-header-icon-color);
}
.ranger-navbox .ranger-title > .mw-collapsible-toggle.mw-collapsible-toggle-collapsed::before,
.ranger-navbox .ranger-header > .mw-collapsible-toggle.mw-collapsible-toggle-collapsed::before{
  transform: none;
}
.ranger-navbox .ranger-title > .mw-collapsible-toggle *,
.ranger-navbox .ranger-title > .mw-collapsible-toggle::after,
.ranger-navbox .ranger-header > .mw-collapsible-toggle *,
.ranger-navbox .ranger-header > .mw-collapsible-toggle::after{
  display: none;
}
.ranger-navbox .ranger-list{
  width: unset;
  padding: var(--navbox-list-padding);
}
.ranger-navbox .ranger-above{
  background: var(--navbox-above-background);
  color: var(--navbox-above-color);
  padding: var(--navbox-above-padding);
  width: unset;
}
.ranger-navbox .ranger-below{
  background: var(--navbox-below-background);
  color: var(--navbox-below-color);
  padding: var(--navbox-below-padding);
  width: unset;
}
.ranger-navbox .ranger-sublist{
  display: flex;
  flex-direction: column;
  gap: var(--navbox-gap);
}
.ranger-navbox .ranger-section-body{
  display: grid;
  gap: var(--navbox-gap);
  grid-template-columns: auto minmax(0,1fr);
}
/* gap fix for collapsed content */
.ranger-navbox [class^="ranger-"][hidden="until-found"]{
  margin-top: calc(0px - var(--navbox-gap)) !important;
}
.ranger-navbox .ranger-row{
  display: contents;
}
.ranger-navbox .ranger-group,
.ranger-navbox .ranger-subgroup{
  text-align: var(--navbox-group-text-align);
  white-space: nowrap;
  font-weight: bold;
  background: var(--navbox-group-background);
  color: var(--navbox-group-color);
  padding: var(--navbox-group-padding);
  width: unset;
}
/* for desktop view */
.ranger-navbox.group-align-left .ranger-group,
.ranger-navbox.group-align-left .ranger-subgroup{
  --navbox-group-text-align: left;
}
.ranger-navbox.group-align-center .ranger-group,
.ranger-navbox.group-align-center .ranger-subgroup{
  --navbox-group-text-align: center;
}
.ranger-navbox.group-align-right .ranger-group,
.ranger-navbox.group-align-right .ranger-subgroup{
  --navbox-group-text-align: right;
}
/* for mobile view */
.ranger-navbox.mobile-group-align-left .ranger-group,
.ranger-navbox.mobile-group-align-left .ranger-subgroup{
  --navbox-group-text-align--mobile: left;
}

.ranger-navbox.mobile-group-align-center .ranger-group,
.ranger-navbox.mobile-group-align-center .ranger-subgroup{
  --navbox-group-text-align--mobile: center;
}

.ranger-navbox.mobile-group-align-right .ranger-group,
.ranger-navbox.mobile-group-align-right .ranger-subgroup{
  --navbox-group-text-align--mobile: right;
}

.ranger-navbox .ranger-listbox > .ranger-wrap{
  background: var(--navbox-list-background);
  color: var(--navbox-list-color);
  flex-grow: 1;
}
.ranger-navbox .ranger-sublist{
  flex-grow: var(--count);
}
.ranger-navbox .ranger-listbox:first-child{ /* A list-n without group-n */
  grid-column-end: span 2;
}
.ranger-navbox .ranger-group,
.ranger-navbox .ranger-subgroup,
.ranger-navbox .ranger-listbox > .ranger-wrap{
  display: grid;
  justify-items: stretch;
  align-items: center;
}
.ranger-navbox.striped-even .ranger-even,
.ranger-navbox.striped-odd .ranger-odd{
  background: var(--navbox-list-background--striped);
}
/* make links use full line height (larger click box)*/
.ranger-navbox .hlist a{
	display: inline-block;
}

.ranger-navbox .align-left,
.ranger-navbox .alignleft{
  text-align: left;
}
.ranger-navbox .align-center,
.ranger-navbox .aligncenter{
  text-align: center;
}
.ranger-navbox .align-right,
.ranger-navbox .alignright{
  text-align: right;
}

/* responsive */
@media screen and (max-width: 720px) {
  .ranger-navbox .ranger-section-body,
  .ranger-navbox .ranger-sublist {
    display: flex;
    flex-flow: column;
  }
  .ranger-navbox .ranger-row{
    display: block;
  }
  .ranger-navbox .ranger-group + .ranger-listbox > .ranger-sublist:first-child,
  .ranger-navbox .ranger-subgroup + .ranger-listbox > .ranger-sublist:first-child{
    margin-top: var(--navbox-gap);
  }
  .ranger-navbox .ranger-listbox.empty{
    display: none;
  }
  .ranger-navbox .ranger-group,
  .ranger-navbox .ranger-subgroup{
    text-align: var(--navbox-group-text-align--mobile);
    white-space: normal;
  }
  
  .ranger-navbox .ranger-sublist {
    padding-left: var(--navbox-tree-indent);
    margin-left: var(--navbox-tree-line-indent);
  }
  .ranger-navbox .ranger-subgroup,
  .ranger-navbox .ranger-listbox {
    position:relative;
  }
  .ranger-navbox .ranger-group br,
  .ranger-navbox .ranger-subgroup br{
    display: none;
  }
  .ranger-navbox .ranger-sublist > .ranger-section > .ranger-header{
    margin-left: calc( 0px - var(--navbox-tree-indent) - var(--navbox-tree-line-indent));
  }
  .ranger-navbox .ranger-sublist .ranger-row > ::before{
    position: absolute;
    left: calc(0px - var(--navbox-tree-indent));
    top: 0;
    width: var(--navbox-tree-line-width);
    height: 100%;
    content: '';
    display: block;
    background-color: var(--navbox-tree-line-color);
  }
  .ranger-navbox .ranger-sublist .ranger-row > .ranger-listbox::before,
  .ranger-navbox .ranger-row.empty-list > .ranger-subgroup::before{
    height: calc(100% + var(--navbox-gap));
  }
  .ranger-navbox .ranger-sublist .ranger-row:last-child > ::before {
    display: none;
  }
  .ranger-navbox .ranger-sublist .ranger-row:last-child > :first-child::before {
    display: block;
    height: calc(50% + var(--navbox-tree-line-width)/2);
  }
  .ranger-navbox .ranger-subgroup::after,
  .ranger-navbox .empty-group > .ranger-listbox > .ranger-wrap::after{
    position: absolute;
    left: calc(0px - var(--navbox-tree-indent) + var(--navbox-tree-line-width));
    width: calc(var(--navbox-tree-indent) - var(--navbox-tree-line-spacing) - var(--navbox-tree-line-width));
    height: var(--navbox-tree-line-width);
    content: '';
    background-color: var(--navbox-tree-line-color);
  }
  /* increase height for links */
  .ranger-navbox .hlist{
    line-height: 2;
  }
}
/**** `.pill` class: the "pill" style  ****/
/* remove middle dots betweem items */
.ranger-navbox.pill .hlist dd:not(:last-child)::after,
.ranger-navbox.pill .hlist li:not(:last-child)::after{
  display: none;
}
/* remove parentheses around nested lists*/
.ranger-navbox.pill .hlist dd ol::before,
.ranger-navbox.pill .hlist dd ul::before,
.ranger-navbox.pill .hlist dd dl::before,
.ranger-navbox.pill .hlist dt ol::before,
.ranger-navbox.pill .hlist dt ul::before,
.ranger-navbox.pill .hlist dt dl::before,
.ranger-navbox.pill .hlist li ol::before,
.ranger-navbox.pill .hlist li ul::before,
.ranger-navbox.pill .hlist li dl::before,
.ranger-navbox.pill .hlist dd ol::after,
.ranger-navbox.pill .hlist dd ul::after,
.ranger-navbox.pill .hlist dd dl::after,
.ranger-navbox.pill .hlist dt ol::after,
.ranger-navbox.pill .hlist dt ul::after,
.ranger-navbox.pill .hlist dt dl::after,
.ranger-navbox.pill .hlist li ol::after,
.ranger-navbox.pill .hlist li ul::after,
.ranger-navbox.pill .hlist li dl::after {
  display: none;
}
/* make lists inline-flex */
.ranger-navbox.pill .hlist ul,
.ranger-navbox.pill .hlist ol,
.ranger-navbox.pill .hlist dl{
  display: inline-flex;
  gap: var(--navbox-pill-gap);
  flex-wrap: wrap;
}
/* "pill" style for items */
.ranger-navbox.pill .hlist li,
.ranger-navbox.pill .hlist dt,
.ranger-navbox.pill .hlist dd{
  padding: var(--navbox-pill-padding);
  border-radius: var(--navbox-pill-border-radius);
  box-shadow: var(--navbox-pill-box-shadow);
  background: var(--navbox-pill-background);
  /* 100% height */
  display: flex;
  align-items: center;
  /* for nested lists */
  gap: var(--navbox-pill-gap); 
  flex-wrap: wrap;
}
/* Add a hover / focus feedback style */
.ranger-navbox.pill .hlist dd:hover,
.ranger-navbox.pill .hlist dd:focus,
.ranger-navbox.pill .hlist dt:hover,
.ranger-navbox.pill .hlist dt:focus,
.ranger-navbox.pill .hlist li:hover,
.ranger-navbox.pill .hlist li:focus {
  box-shadow: var(--navbox-pill-box-shadow--hover);
  background: var(--navbox-pill-background--hover);
}
/**** `.pill-mobile` class: only apply the "pill" style on mobile ****/
@media screen and (max-width: 720px) {
	/* remove middle dots betweem items */
	.ranger-navbox.pill-mobile .hlist dd:not(:last-child)::after,
	.ranger-navbox.pill-mobile .hlist li:not(:last-child)::after{
	  display: none;
	}
	/* remove parentheses around nested lists*/
	.ranger-navbox.pill-mobile .hlist dd ol::before,
	.ranger-navbox.pill-mobile .hlist dd ul::before,
	.ranger-navbox.pill-mobile .hlist dd dl::before,
	.ranger-navbox.pill-mobile .hlist dt ol::before,
	.ranger-navbox.pill-mobile .hlist dt ul::before,
	.ranger-navbox.pill-mobile .hlist dt dl::before,
	.ranger-navbox.pill-mobile .hlist li ol::before,
	.ranger-navbox.pill-mobile .hlist li ul::before,
	.ranger-navbox.pill-mobile .hlist li dl::before,
	.ranger-navbox.pill-mobile .hlist dd ol::after,
	.ranger-navbox.pill-mobile .hlist dd ul::after,
	.ranger-navbox.pill-mobile .hlist dd dl::after,
	.ranger-navbox.pill-mobile .hlist dt ol::after,
	.ranger-navbox.pill-mobile .hlist dt ul::after,
	.ranger-navbox.pill-mobile .hlist dt dl::after,
	.ranger-navbox.pill-mobile .hlist li ol::after,
	.ranger-navbox.pill-mobile .hlist li ul::after,
	.ranger-navbox.pill-mobile .hlist li dl::after {
	  display: none;
	}
	/* make lists inline-flex */
	.ranger-navbox.pill-mobile .hlist ul,
	.ranger-navbox.pill-mobile .hlist ol,
	.ranger-navbox.pill-mobile .hlist dl{
	  display: inline-flex;
	  gap: var(--navbox-pill-gap);
	  flex-wrap: wrap;
	}
	/* "pill" style for items */
	.ranger-navbox.pill-mobile .hlist li,
	.ranger-navbox.pill-mobile .hlist dt,
	.ranger-navbox.pill-mobile .hlist dd{
	  /* 100% height */
	  display: flex;
	  align-items: center;
	  /* for nested lists */
	  gap: var(--navbox-pill-gap);
	  flex-wrap: wrap;
	}
	/* "pill" style for items */
	.ranger-navbox.pill-mobile .hlist li,
	.ranger-navbox.pill-mobile .hlist dt,
	.ranger-navbox.pill-mobile .hlist dd{
	  padding: var(--navbox-pill-padding);
	  border-radius: var(--navbox-pill-border-radius);
	  box-shadow: var(--navbox-pill-box-shadow);
	  background: var(--navbox-pill-background);
	  /* 100% height */
	  display: flex;
	  align-items: center;
	  /* for nested lists */
	  gap: var(--navbox-pill-gap);
	  flex-wrap: wrap;
	}
	/* Add a hover / focus feedback style */
	.ranger-navbox.pill-mobile .hlist dd:hover,
	.ranger-navbox.pill-mobile .hlist dd:focus,
	.ranger-navbox.pill-mobile .hlist dt:hover,
	.ranger-navbox.pill-mobile .hlist dt:focus,
	.ranger-navbox.pill-mobile .hlist li:hover,
	.ranger-navbox.pill-mobile .hlist li:focus {
	  box-shadow: var(--navbox-pill-box-shadow--hover);
	  background: var(--navbox-pill-background--hover);
	}
}
/*********************
* End Template:Navbox*

/* Custom styles for images */
.pixel-img {
	image-rendering: pixelated;
}

/* Custom navigation */
#mw-head {
	border-image: none !important;
    margin-bottom: 1em;
}

#mw-panel, #mw-head, #footer {
  image-rendering: pixelated;
}

@media screen and (max-width: 720px) {
	#left-navigation,
	#right-navigation:not(:is(#p-search)) {
	    margin-bottom: .5em !important;
	}
	
	body.has-vector-mobile-menu #mw-panel .vector-menu-portal,
	.vector-menu-portal .vector-menu-content {
		border-image: none !important;
	}
	
	.vector-menu-portal .vector-menu-heading {
	  margin: 0 !important;
	}
}

/* Discord link */
#n-Wiki-Discord a::before {
  content: url(https://ballxpit.wiki.gg/images/thumb/Discord.png/16px-Discord.png);
  margin: 0 .5em 0 0;
  display: inline-block;
}

/* Fix margins in balls navbox */
.balls-navbox .hlist ul li span {
  margin: -1em !important;
}

/* Balls infobox */
.infobox-ball .pi-image img {
  transform: scale(5);
  image-rendering: pixelated;
  margin: 8em 0;
}
```

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
