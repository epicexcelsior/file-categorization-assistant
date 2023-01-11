# FILE CATEGORIZATION ASSISTANT
# Created by EpicExcelsior on December 26, 2022

# Description: Loops through a directory of media files, opens each file individually,
# and prompts the user to categorize the file. File is copied to different folders depending
# on user input

# Prerequisites: Edit the variables below, then edit the fileOperations function as needed.

###################################################
# Path to folder to be categorized
sourceFolder = r"C:\Users\epice\Downloads\emojis"

# Path to VLC executable
vlcPath = r"C:\Program Files\VideoLAN\VLC\vlc.exe"

# Define paths to destination folders
folderOne = r"C:\PATH\TO\FOLDER"
folderTwo = r"C:\PATH\TO\FOLDER"
folderThree = r"C:\PATH\TO\FOLDER"

# Any folders in this list will be created if they don't already exist
destDirPaths = [folderOne, folderTwo, folderThree]


# Define valid options
validOptions = {
    '1': "Copy to folder 1",
    '2': "Copy to folder 1 and 2",
    '3': "Copy to folder 2",
    '4': "Copy to folder 3",
    '5': "Delete"
}
###################################################

import os
import subprocess
from shutil import copy2, rmtree

###################################################
# Define automated file operations (copying, deleting)
# Edit as needed
def fileOperations(path, choice):
    if choice == '1':
        copy2(path, sfw)
        print(f'{f} copied to 1.')
    elif choice == '2':
        copy2(path, sfw)
        copy2(path, meme2)
        print(f'{f} copied to 1 and 2.')
    elif choice == '3':
        copy2(path, meme2)
        print(f'{f} copied to 2.')
    elif choice == '4':
        copy2(path, saturday)
        print(f'{f} copied to 3.')
    elif choice == '5':
        copy2(path, delete)
        print(f'{f} copied to deleted folder.')
###################################################


# Create destination folders if they don't already exist
def createFolders():
    # Check if folders exist. Add missing folders to dict to be added later.
    for path in destDirPaths:
        if not os.path.isdir(path):
            os.mkdir(path)


# Accept user input within pre-defined options
# Args: prompt (str) and iterable (list)
def inputValidation(prompt, iterable):
    choice = input(prompt).lower()

    while choice not in iterable:
        print("Invalid option. Please try again.")
        choice = input(prompt).lower()

    return choice


# Checks if a file's extension is included in a provided list
def extensionInList(filepath, iterable):
    _, extension = os.path.splitext(filepath)
    extension = extension[1:]  # remove the first . from the extension
    return extension in iterable # True if it's in the list, false if not


vlcFormats = ['mp4', 'webm', 'jpeg', 'jpg', 'png', '3g2', '3gp', '3gp2', '3gpp', 'amv',
'asf', 'avi', 'bik', 'flv', 'gxf', 'm1v', 'm2v', 'm2t', 'm2ts', 'm4v', 'mkv', 'moov', 'mov',
'mpeg', 'mpeg1', 'mpeg2', 'mpeg4', 'mpg', 'mpv', 'mt2s', 'mts', 'mxf', 'nsv', 'ogm', 'ogv',
'qt', 'rm', 'rmvb', 'swf', 'ts', 'vob', 'wmv', '3ga', 'aac', 'ac3', 'aif', 'aiff', 'amr', 'ape',
'au', 'flac', 'm4a', 'm4b', 'm4p', 'mid', 'midi', 'mka', 'mp3', 'mpa', 'ogg', 'ra', 'wav', 'weba',
'bmp', 'ico', 'tiff', 'mms', 'rtp', 'rtsp', 'sdp']
browserFormats = ['gif', 'webp', 'apng']


createFolders()
# Print list of valid options
print("Welcome to the file categorizer.\nValid options:")
for key in validOptions.keys():
    print(key, '-', validOptions[key])
print("Q - quit\n")


browserFiles = [] # Paths to files that can't be opened with VLC (to be opened later in a web browser)

# PHASE 1 - Open files using VLC
# "Walk" through all files in folder & subfolders
for (subdir, dirs, files) in os.walk(sourceFolder):
    for f in files:
        filePath = os.path.join(subdir, f) # Joins path of current subdirectory with current file
        
        # If filepath is in vlcFormats, deal with it now
        # Else add it to later list
        if extensionInList(filePath, vlcFormats):
            try:
                # Open file using VLC executable
                p = subprocess.Popen([vlcPath, filePath], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except:
                print(f"Failed to open '{filePath}'")
                browserFiles.append(filePath)
                continue

            # Get user input (forces valid input)
            operation = inputValidation("Enter category: ", list(validOptions.keys()) + ['q'])

            # Exit loop upon user input
            if operation == 'q': break

            # Perform operations according to user input
            fileOperations(filePath, operation)
        else:
            browserFiles.append(filePath)
            print(f'{filePath} can\'t be opened by VLC. It will be opened by the default program at the end.')
            continue


# Close VLC
try:
    subprocess.run([vlcPath, "vlc://quit"])
    p.terminate()
except:
    print("Unable to close VLC.")


laterFiles = [] # Paths to files that can't be opened with a browser (to be opened later with default program)
# PHASE 2 - Open files using HTML & web browser
print('\nNow viewing files that could not be opened by VLC.\n')
for f in browserFiles:
    if extensionInList(f, browserFormats):
        try:
            open(f"{f}.html", "w").write(f"<html><body><img src='{f}'></body></html>")
            webbrowser.open_new_tab(f"{f}.html")
        except:
            print(f"Failed to open '{f}'")
            continue

        operation = inputValidation("Enter category: ", list(validOptions.keys()) + ['q'])

        if operation == 'q':
            os.remove(f'{f}.html')
            break

        fileOperations(f, operation)
        os.remove(f'{f}.html')
    else:
        laterFiles.append(f)


# PHASE 3 - Open files using default program
print('\nNow viewing files that could not be opened by VLC or browser.\n')
for filePath in laterFiles:
    try:
        # Open file using default program
        os.startfile(filePath)
    except:
        print(f"Failed to open '{filePath}'")
        continue

    operation = inputValidation("Enter category: ", list(validOptions.keys()) + ['q'])

    if operation == 'q': break

    fileOperations(filePath, operation)


# Confirms deletion of files in specified directory, then deletes all directory contents
deleteConf = inputValidation('No more files. Delete files in "deleted" folder? (y/n): ', ['y', 'n'])
if deleteConf == 'y':
    try:
        rmtree(deleteDir)
    except:
        print("Failed to delete files.")


print("Program is finished.")