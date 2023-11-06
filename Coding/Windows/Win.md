# windows

## exclude a folder from indexing
indexing options -> modify

## exclude a exe from anti-malware
win + i -> update & security -> windows security -> virus & threat protection -> exclusions -> MsMpEng.exe

## Change PWD in remote machine
when remote to that machine using CRTL+ALT+END to change your password

## enable remote access for an account
Add Remote Desktop Users in Local Users and Groups: lusrmgr.msc\\
groups: remote desktop users, add

## explorer.exe eats memory
3rd party Explorer shell extensions are the normal cause. There are utilities like ShellEXView to track these down.

On a File Explorer Window if you click: File -> "Change Folder and Search Options", there's a checkbox in "Adbanced settings" called "Launch Folder Windows in a separate process" - that may limit any memory leaks to the Video folder windows.

## Check for administrator rights using Command Prompt
net user [username]

Computer Management -> user and groups

## ring-fence network folder
note we do this through group membership though and windows
only refreshes that on login (ie you may need to log out and in to get access back).

## remote desk setting
run mstsc. Click Show Options and select Advanced. Click Settings and select Use these RD Gateway server settings and enter exchange.rxxcxx.com.au as the server name.  Other settings can be left as default, but you may want to check “Use my RD Gateway credentials for the remote computer” on this dialog as well to avoid another prompt.

## Change remote machine password
Press **CRTL+ALT+END**

## check cpu cores
msinfo32
