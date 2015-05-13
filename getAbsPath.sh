#!/bin/bash
#*******************************************************************
# Name: Rodolfo Alvarado
# CWID: 897282844
# CPSC-254, Spring 2015
# Lab Project #4 - 5
#	Write a Bash shell script named “getAbsPath.sh” that does the following:
#	a. Take 1 or more relative paths to files or directories as arguments and print the
#	corresponding absolute paths
#	b. For each argument print the argument as is, followed by “ => ”, followed by the
#	corresponding absolute path
#	c. If argument is a file or directory that doesn’t exist, print “does not exist” after “ => “
#	d. If argument is already an absolute path, print “already absolute path” after “ => “
#	e. If argument is a symbolic link you do not have to follow the link, just determine the absolute
#	path of the symbolic link
#	f. If there is no argument, print an error message and exit
#	g. Important: You can NOT use “realpath” or “readlink” commands. 
#*******************************************************************
# Verify that an argument of a function is called
if [ $# -lt 1 ];
	then
	echo "usage: ./getAbsPath.sh <relative path> [<relative path>...] "
	exit 1
fi
while [ -n "$1" ];
	do	
	if [  -d ${1}   ] || [  -f ${1}   ];
	then
		if [[ ${1} = /* ]];
		then
			name=$1
			echo "$1 => already absolute" 
		else #$(cd $(dirname "$1") && pwd -P)/$(basename "$1")
			echo "$1 => `echo $(cd $(dirname "$1") && pwd -P)/$(basename "$1")`"
		fi
	else
		echo "error: $1 => does not exist!"
		exit 1
	fi
	shift 1
done
exit 0
