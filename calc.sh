#!/bin/bash
#*******************************************************************
# Name: Rodolfo Alvarado
# CWID: 897282844
# CPSC-254, Spring 2015
# Lab Project #4 - 2
#	a. Performs addition (+), subtraction (-), multiplication (x), and integer division (/) math
#	operations.
#	b. Takes in 2 operands and 1 operator and prints the result. Example: “calc.sh 5 + 3” would
#	print “8” and “calc.sh 9 / 2” would print “4”
#	c. If there are not exactly 3 arguments, or the second argument is not one of the operators in
#	part (a), or first or third argument is not an integer, print an error message and exit
#	$1 =  valid int $2 = operator $3 = valid int

# sanity check for atleast 3 arguments
if [ $# -ne 3 ];
	then
	echo "usage: $0 <number> <operator> <number>"
	exit 
fi
# this function checks whether or not an argument is 
# a valid integer, returns true or false
isValidInt()
{
	if [[ $1 =~ ^[+-]?[0-9]+$ ]]; then
		return 0
	else
		return 1
	fi
}
# if argument 1 & 3 are not valid error code printed
# and exit 1, else it will proceed
if  ! isValidInt $1 
	then
	echo "error: $1 is not a valid int."
	exit 1
elif ! isValidInt $3
	then
	echo "error: $3 is not a valid int."
	exit 1
fi
# saving both integers to variables
operand=$1
operandTwo=$3
# if statement to check for operators[x+-/] and save
# else exit with 2 and error message
if [ "$( echo $2 | grep  '^[+/-]$')" ];
	then
	operator=$2
elif [ "$( echo $2 | grep  '^[x]$')" ];
	then
	operator="*"
else
	echo "error: $2 must be [+x-/]"
	exit 2
fi
# case statement to decide which operation is choosen
case $operator in
	"+" ) echo `expr $operand + $operandTwo`;;
	"-" ) echo `expr $operand - $operandTwo`;;
	"*" ) echo `expr $operand \* $operandTwo`;;
	"/" ) 
		if [ $operandTwo = 0 ];
			then
			echo "error: cannot divide by zero"
			exit 3
		else 
			echo `expr $operand / $operandTwo`
		fi ;;
esac
exit 0
