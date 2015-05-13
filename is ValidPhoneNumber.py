#!/usr/bin/python3
#********************************************
# Name: Rodolfo Alvarado
# CWID: 897282844
# CPSC-254, Spring 2015
# Lab Project #5 - 3
#
# Takes in arguement and checks to see if 
# the supplied argument is valid phone # format.
#********************************************
import sys
import re

def main():
#if arguments are less than on 1 exit with error message
	if len(sys.argv) < 2:
		print('usage: ./isValidPhoneNumber.py "phone number"')
		exit(1)
	#phone string saved 
	phoneNumberString=sys.argv[1]
	print(phoneNumberString)
	#phone pattern regex's
	phonePattern = r'^(1-)?\d{3}-\d{3}-\d{4}$'
	phonePattern2 = r'^\d{3}\s?\d{3}\s?\d{4}$'
	phonePattern3 = r'^(\(?\d{3}\)\s|\d{3}/)\d{3}-\d{4}$'

	isPhoneNumber = re.match(phonePattern, phoneNumberString)
	isPhoneNumber2 = re.match(phonePattern2, phoneNumberString)
	isPhoneNumber3 = re.match(phonePattern3, phoneNumberString)
	#if valid print valid else invalid
	if isPhoneNumber:
		print('valid phone number.')
	elif isPhoneNumber2:
		print('valid phone number.')
	elif isPhoneNumber3:
		print('valid phone number.')
	else:
		print('invalid phone number.')

if __name__ == "__main__":
	main()
