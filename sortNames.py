#!/usr/bin/python3
#********************************************
# Name: Rodolfo Alvarado
# CWID: 897282844
# CPSC-254, Spring 2015
# Lab Project #5 - 4
#
# Read in 1 file (filename supplied as argument) and create another file named
# “sortedNames.txt”. If there is not exactly 1 argument or the file pointed to by the
# argument doesn’t exist, print an error message and exit. 
#********************************************
import sys,re
import os.path

#check for no arguments
fileDirectory=str(sys.argv[0])
fileDirectory=fileDirectory[2:]
if len(sys.argv) < 1:
	print('usage: ./sortNames.py "filename.txt"')
	exit(1)
#check if file exits else exit with error
if os.path.isfile(sys.argv[1]):
	pass
else:
	print('file does not exist! \nusage: ./sortNames.py "filename.txt"')
	exit(1)
#saving inputefile name and declaring list for names
inputfile = sys.argv[1]
outputfile = 'sortedNames.txt'
Names=[]
#regex object with pattern of first middle last and first last names
firstMiddleLast = re.compile(r'^(\w+) (\w\.?|\w+) (\w+)$')
firstLast =  re.compile(r'^(\w+) (\w+)$')

infile =open(inputfile,'r') 
#opening and reading from input file
for line in infile:
	#checking if name is a match for first last or first middle last
	isFML = firstMiddleLast.match(line)
	isFL = firstLast.match(line)
	#if line is either then name will append to Names list
	if isFML:
		Names.append(isFML.group(3)+ ', ' + isFML.group(1) + ' ' + isFML.group(2) + '\n')
	elif isFL:
		Names.append(isFL.group(2)+ ', ' + isFL.group(1) + '\n')
infile.close()
#Names list is sorted
Names=sorted(Names)
#saving first argument to find directory and compare it with current
fileDirectory=str(sys.argv[0])
#finds last instance of '/'
lastForwardSlash = fileDirectory.rfind('/')
#concantenating current directory with file directory 
fileDirectory=os.getcwd()+fileDirectory[1:lastForwardSlash]
#comparing current and file if not same cd into file Directory
if os.getcwd() != fileDirectory:
	os.chdir(fileDirectory)
#creating and opening sortedNames.txt
with open(outputfile, 'w') as outfile:
	#name will be written to output file
	for name in Names:
		outfile.write(name)
