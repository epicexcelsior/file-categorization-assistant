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


createFolders()
# Print list of valid options
print("Welcome to the file categorizer.\nValid options:")
for key in validOptions.keys():
    print(key, '-', validOptions[key])
print("\n")


# "Walk" through all files in folder & subfolders
for (subdir, dirs, files) in os.walk(sourceFolder):
    for f in files:
        filePath = os.path.join(subdir, f) # Joins path of current subdirectory with current file
        try:
            p = subprocess.run([vlcPath, filePath]) # Open file using VLC executable
        except:
            print(f"Failed to open '{f}'")

        # Get user input (forces valid input)
        operation = inputValidation("Enter category: ", list(validOptions.keys()) + ['q'])

        # Exit loop upon user input
        if operation == 'q': break

        # Perform operations according to user input
        fileOperations(filePath, operation)


# Close VLC
try:
    subprocess.run([vlcPath, "vlc://quit"])
    p.terminate()
except:
    print("Unable to close VLC.")


# Confirms deletion of files in specified directory, then deletes all directory contents
deleteConf = inputValidation('No more files. Delete files in "deleted" folder? (y/n): ', ['y', 'n'])
if deleteConf == 'y':
    try:
        rmtree(deleteDir)
    except:
        print("Failed to delete files.")


print("Program is finished.")