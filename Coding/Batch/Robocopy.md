# robocopy

|Option |Description |
|:--|:--|
|/s |Copies subdirectories. Note that this option excludes empty directories |
|/e |Copies subdirectories. Note that this option includes empty directories |
|/b |Copies files in Backup mode |
|/v |produce Verbose output, showing skipped files |
|/np |not show percentage progress of each file copy |
|/mov  |Moves files and deletes them from the source after they are copied |
|/purge |Deletes destination files and directories that no longer exist in the source |
|/r:[n] |number of retries |
|/w:[t] |wait time in sec between retries |
|/mt:[n] |multi-threaded switch |
|/log:[file] |log file path |
|/xa:SH |exclude hidden system files |
|/xd folder |exclude the folder |

## mirror a folder without deleting destination files
```bat
Robocopy "C:\src" "F:\bak" /s /r:5 /w:15 /mt:4 /np /log:backup.log
```
