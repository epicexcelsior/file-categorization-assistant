# file-categorization-assistant
 Displays media files one at a time to user, then allows files to be copied to various according to user input

**Configure Environment**
1. This program uses VLC to open photo/video files. Install it [here](https://www.videolan.org/vlc/)
2. In VLC preferences (Tools > Preferences > Interface) enable "Pause on last frame of a video". This will prevent videos from auto-playing once they finish.
3. In the default apps section of Windows Settings (Apps > Default apps) change program association for png, jpg, jpeg, mp4, mov, and webm files to VLC.

 **Configure Program**
 1. Create variables for directory (folder) paths
 2. Create/edit options in validOptions dictionary
 3. Edit fileOperations function to perform actions based on user input

This program currently supports most image/video filetypes through VLC. Files opened by other programs will work but they will not be closed after they're opened.

Disclaimer: This is a basic program created for a specific use case. It requires changes to function in different environments and use cases. Exercise caution when using it.