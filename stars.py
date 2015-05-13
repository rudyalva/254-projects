#!/usr/bin/python3
#********************************************
# Name: Rodolfo Alvarado
# CWID: 897282844
# CPSC-254, Spring 2015
# Lab Project #5 - 1
#
# Print right-aligned triangle of stars whose size is indicated by
# the supplied argument.
#********************************************
import sys
import re

def main():
	#integer check 
	integerPattern = r'^[+-]?[0-9]+$'
	isInt = re.match(integerPattern, sys.argv[1])
	#if valid int continue else exit with error
	if not isInt:
		print('usage: stars.py <integer>')
		exit(1)

	stars = int(sys.argv[1])
	spaces = int(stars - 1)
	#first loop prints rows
	for rows in range(1,stars+1):
		#second loop  printd spaces for alignment
		for space in range (rows,spaces+1):
			print(' ', end='')
		#third loop prints *
		for star in range (1,rows+1):
			print('*', end ='')
		print()

if __name__ == "__main__":
	if len(sys.argv) == 2:
		main()
	else:
		print("Usage: " + sys.argv[0] + " <integer>")
