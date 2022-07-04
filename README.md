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
3. Insert "Fast git" folder into this folder (not "Fast-git", namely "Fast git")

## O.S.
Tested only Windows 10. Not tested on other versions.

## More
### 1. Set token
To grant access to the plugin when working with repositories, you need to create an access token using this link https://github.com/settings/tokens.  
Then, in the context menu, click the "Set token" function and enter it in the input field that appears.
Required scopes:
1. All repos
2. All admin:org  

### 2. Set remote url
If, after cloning someone else's repository, you need to add a link from your repository, then in the context menu:  
Click "Set remote url" → and select an open folder in our project. It must contain a git!

### 3. Create repository
You need to quickly create a repository so that it is already in sync with your git account, then:
Click "Create repository" → and select an open folder in our project. Folder name must not contain spaces!

### 4. Update repository
The fourth and probably the most important function of this plugin, because of which I was constantly annoyed by opening cmd,  
going to the folder path, entering 3 commands, namely:
git add .
git commit --allow-empty-message -m ''
git push "url"
NOW:
1. Open the context menu.
2. Hover over the plugin.
3. Hover over "Update repository".
4. Select the desired folder and click.

OR:
1. Press the key combination ctrl + "num"

### 5. Clone repository to
Well, here I don't even know what to explain...  
You just hover over "Clone repository to", select a folder from those added to the project and enter a link to the repository.
