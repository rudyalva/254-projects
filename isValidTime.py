#!/usr/bin/python3
#********************************************
# Name: Rodolfo Alvarado
# CWID: 897282844
# CPSC-254, Spring 2015
# Lab Project #5 - 2
#
# takes in argument and checks if valid time 
# format
#********************************************
import sys
import re

#print('this is argument 1: {}'.format(sys.argv[1]))
#print('usage: {} hour:minutes am/pm'.format(sys.argv[0]))
#print(sys.argv[0],sys.argv[1],sys.argv[2])
#timestring=sys.argv[1]
def main():
	# if length = 2 then time string is set to sys.argv
	# else if it will check if string entered has 2 arguments 7:00 pm
	# else error
	timestring=sys.argv[1]
	#elif len(sys.argv) == 3 :
	#	dayOrNight = sys.argv[2]
	#	if(dayOrNight.upper() == 'AM' or dayOrNight.upper() =='PM'):
	#		timestring=str(sys.argv[1]+dayOrNight)
	#regular expression for valid time
	timePattern = r'^[+]?(12|11|10|0?[0-9]):[0-5][0-9][\s]?(am|pm|AM|PM)$'
	#check if string matches patter
	isTime = re.match(timePattern, timestring)
	#print valid or invalid
	if isTime:
		print('valid time')
	else:
		print('invalid time')

if __name__ == "__main__":
	if len(sys.argv) == 2:
		main()
	else:
		print('usage: {} <hour:minutes am/pm>'.format(sys.argv[0]))
		exit(1)
