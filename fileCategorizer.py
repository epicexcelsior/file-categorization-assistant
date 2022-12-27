# File Categorization Assistant
# Created by EpicExcelsior on December 26, 2022

# Description: Loops through a directory of media files, opens each file individually,
# and prompts the user to categorize the file. File is copied to different folders depending
# on user input

# Prerequisites: It's easiest to set the default program for various file types to VLC
# Windows Settings -> Apps -> Default apps -> Change all relevant types to VLC (can be reverted later)

import os
import subprocess
from shutil import copy2, rmtree

# Define path of source directory
sourceDir = r"C:\Users\epice\Downloads\fake downloads"

# Define paths to destination directories
sfw = r"C:\Users\epice\Downloads\Memes\SFW"
meme2 = r"C:\Users\epice\Downloads\Memes\Meme2"
saturday = r"C:\Users\epice\Downloads\Memes\Saturday"

# Define valid options
optionDict = {
    'a': "SFW",
    'b': "neutral",
    'c': "sensitive",
    'd': "cursed Saturday",
    'e': "delete"
}

# Create directory to store deleted files
try:
    os.mkdir(r"C:\Users\epice\Downloads\Memes\Delete")
except:
    print("Deleted folder already created.")
delete = r"C:\Users\epice\Downloads\Memes\Delete"

# Print list of valid options
print("Welcome to the file categorizer.\nValid options:")
for key in optionDict.keys():
    print(key, '=', optionDict[key])
print("\n")


def fileOperations(file_path):
    if choice == 'q':
        print("Program terminated.")
        return
    elif choice == 'a':
        copy2(file_path, sfw)
        print(f'{f} copied to sfw.')
    elif choice == 'b':
        copy2(file_path, sfw)
        copy2(file_path, meme2)
        print(f'{f} copied to sfw and meme2.')
    elif choice == 'c':
        copy2(file_path, meme2)
        print(f'{f} copied to meme2.')
    elif choice == 'd':
        copy2(file_path, saturday)
        print(f'{f} copied to saturday.')
    elif choice == 'e':
        copy2(file_path, delete)
        print(f'{f} deleted.')


# Confirms deletion of files in specified directory, then deletes all directory contents
def deleteDir(deleteDir):
    # Confirm deletion of deleted files. Forces valid user input.
    deleteConf = ''
    while deleteConf not in ['y', 'n']:
        deleteConf = input('No more files. Delete files in "deleted" folder? (y/n): ').lower()

    if deleteConf == 'y':
        try:
            rmtree(deleteDir) # Delete directory contents
        except:
            print("Failed to delete files.")


for (subdir, dirs, files) in os.walk(sourceDir):
    for f in files:
        filePath = os.path.join(subdir, f) # Joins path of current subdirectory with current file
        # process = Popen(["open", filePath], stdout=PIPE, stderr=PIPE)
        try:
            os.startfile(filePath) # Opens default program for file's filetype
        except:
            print(f"File {f} failed to open")

        # Get user input (forces valid input)
        choice = input("Enter category: ").lower()
        while choice not in (list(optionDict.keys()) + ['q']):
            print("Invalid category option. Please try again.")
            choice = input("Enter category: ").lower()

        # Perform operations according to user input
        fileOperations(filePath)

    # Kills VLC
    try:
        os.system('taskkill /F /IM vlc.exe')
    except:
        print("Unable to terminate VLC.")

    deleteDir(delete)

    print("Program is finished.")