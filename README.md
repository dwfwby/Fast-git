# Fast-git

All of the following is translated in Google translator!

This git is a plugin for the sublime text program. Its advantage is that you don't need to install **gh cli** and **git** as they come with a set. 
Everything is implemented using batch commands sent by sublime text. But I can admit that because of this, the weight is significantly large.

## Basic functional (context menu)
1. Set token → «input token»
2. Set remote url → «choise open folder» → «input url»
3. Create repository → «choise open folder»
4. Update repository → «choise open folder»
5. Clone repository → «choise open folder»

## Key bindings 
Also added keyboard shortcuts for quick pushing. "ctrl+<number from 1 to 0 on keyboard>"  
Example:  
 - Your opened folder is the first one in the list, press ctrl+1.  
 - Or your opened folder is second in the list, press ctrl+2. And so on.
 
## Instalation  
1. Open context menu in sublime text (key ALT)
2. Go "preferences" → "browse packages"
3. Insert "Fast git" folder into this folder

## O.S.
Tested only Windows 10. Not tested on other versions.

## More
### 1. Set token
To grant access to the plugin when working with repositories, you need to create an access token using this link https://github.com/settings/tokens. Then, in the context menu, click the "Set token" function and enter it in the input field that appears.
Required scopes:
1. All repos
2. All admin:org
