#!/bin/bash
#********************************************
# Name: Rodolfo Alvarado
# CWID: 897282844
# CPSC-254, Spring 2015
# Lab Project #4 - 1
#
# Print right-aligned triangle of stars whose size is indicated by
# the supplied argument.
#********************************************
# sanity checks
if [ $# -ne 1 ]
then
	echo "usage: $0 <number>"
	exit 1
fi
# is valid function
isValidInt()
{
	if [[ $1 =~ ^[+-]?[0-9]+$ ]]; then
		return 0
	else
		return 1
	fi
}

if ! isValidInt $1
then
	echo "error: $1 is not a valid integer"
	exit 1

# assuming $1 is already a valid number
elif [ $1 -lt 1 ]
then 
	echo "error: $1 is not a postivie integer"
	exit 1
fi

spaces=$(($1 - 1))
# loop will print out star and spaces according $1
for ((line = 1; line <=$1; line++))
do
	for((space=1; space <=$spaces; space++))
	do
		echo -n " "
	done
	for((star=1; star <=$line; star ++))
	do
		echo -n "*"
	done
	echo
	spaces=$((spaces - 1))
done
exit 0
