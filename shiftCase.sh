#!/bin/bash
#*******************************************************************
# Name: Rodolfo Alvarado
# CWID: 897282844
# CPSC-254, Spring 2015
# Lab Project #4 - 4
#	Write a Bash shell script named “shiftCase.sh” that
#	a. Convert the supplied string arguments to all uppercase or all lowercase depending on the
#	supplied flag
#	b. If the flag is “-l” performs the lowercase conversion and print the result to screen
#	c. If the flag is “-u” performs the uppercase conversion and print the result to screen
#	d. Only alphabetic characters are converted. Non-alphabetic characters (such as numbers,
#	punctuation marks, etc.) are not affected.
#	e. If there is no argument, or a flag other than “-l” or “-u”, or both “-l” and “-u” flags are
#	specified, then print an error message and exit 

#ERROR: usage: ./shiftCase.sh -l | -u <string to convert> [<string to convert>...]
#./shiftCase.sh -d Testings
#ERROR: error: -d: not supported

#sanity checks
if [ $# -lt 2 ];
	then
	echo "usage: ./shiftCase.sh -l | -u <string to convert> [<string to convert>...]"
	exit 1
elif [ $1 = "-l" ] && [ $2 = "-u" ];
	then
	echo "usage: ./shiftCase.sh -l | -u <string to convert> [<string to convert>...]"
	exit 2
elif [ $1 = "-u" ] && [ $2 = "-l" ];
	then
	echo "usage: ./shiftCase.sh -l | -u <string to convert> [<string to convert>...]"
	exit 2
elif [ $1 = "-lu" ] || [ $1 = "-ul" ]; 
	then
	echo "usage: ./shiftCase.sh -l | -u <string to convert> [<string to convert>...]"
	exit 2
fi

while getopts ":l:u:" opt;
do
   case "$opt" in
	l) 
		while [ -n "$1" ];
			do
			shift 1
			echo -n ${1,,}
			echo " "
			
		done
		;;
	u) 
		while [ -n "$1" ];
			do	
			shift 1
			echo -n ${1^^}
			echo " "
		done
		;;	
	*) echo "error: $1: not supported" 
		exit 3;; 
   esac
done
exit 0
