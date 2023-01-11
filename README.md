# media-categorization-assistant
 Displays media files one at a time to user, then allows files to be copied to various according to user input

**Configure Environment**
1. This program uses VLC to open photo/video files. Install it [here](https://www.videolan.org/vlc/).
2. In VLC preferences (Tools > Preferences > Interface) enable "Pause on last frame of a video". This will prevent videos from auto-playing once they finish.

 **Configure Program**
 1. Create variables for directory (folder) paths.
 2. Create/edit options in the validOptions dictionary.
 3. Edit the fileOperations function to perform actions based on user input.

This program works in phases. It will first attempt to open files using VLC. Then it will attempt to open media using a web browser and HTML. Finally, it will open any remaining files using the default program.

Disclaimer: This program was designed to copy, move, and delete files. Exercise caution when using it.