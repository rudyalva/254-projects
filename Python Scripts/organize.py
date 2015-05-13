#!/usr/bin/python3
#################################################################
# Organize student file submissions by moving each student's
# submissions into his/her own folder and renaming the files
#################################################################

# Import modules with needed functionalities
import os
import sys
import re
import shutil

# Sanity checks
if len(sys.argv) != 2:
    print("usage: " + sys.argv[0] + " <dir to organize>")
    exit(1)
    
if not os.path.isdir(sys.argv[1]):
    print("error: " + sys.argv[1] + ": not a valid directory")
    exit(1)

rootDir = sys.argv[1]
print("Organizing: " + rootDir)

# This will match anything with ends with ".sh"
# and contains 4 underscores. The 2 sets of parentheses
# will capture the actual strings of the match.
pattern = r'^(.*)_.*_.*_.*_(.*\.sh)$'

# For each file in input dir
for fname in os.listdir(rootDir):
    
    # Get the full path to the file
    fullpath = os.path.join(rootDir, fname)

    # Skip over directories
    if os.path.isdir(fullpath):
        continue

    # Match filename against pattern
    mo = re.match(pattern, fname)

    # Match successful
    if mo:
        # Student name is in 1st capture group
        student = mo.group(1)
        # Script name is in 2nd capture group
        script = mo.group(2)
        
        print("Processing: " + student + ", " + script)

        # Create directory for each student
        studentDir = os.path.join(rootDir, student)
        if not os.path.exists(studentDir):
            os.makedirs(studentDir)

        # Move the student's file into his/her directory
        # and rename the file (note: shutil.move() both
        # move and rename the file at the same time)
        destFile = os.path.join(studentDir, script)
        shutil.move(fullpath, destFile)

    # Match not successful
    else:
        print("Skipping: " + fname)
