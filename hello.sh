#!/bin/bash
#*******************************************************************
# Name: Rodolfo Alvarado
# CWID: 897282844
# CPSC-254, Spring 2015
# Lab Project #4 - 2
#	Write a Bash shell script named “hello.sh” that
#	a. Prints different messages depending on the time of day when it is executed
#	b. Print “Hello <username>, it is <time>. Have a good morning!” if between 6am (inclusive)
#	and noon (exclusive)
#	c. Print “Hello <username>, it is <time>. Have a good afternoon!” if between noon (inclusive)
#	and 6pm (exclusive)
#	d. Print “Hello <username>, it is <time>. Have a good evening!” if between 6pm (inclusive) and
#	midnight (exclusive)
#	e. Print “Hello <username>, it is <time>. Don’t work too hard!” if between midnight (inclusive)
#	and 6am (exclusive)
#	f. Replace “<username>” with the actual username of the user running the script
#	g. Replace “<time>” with the actual current time in the format “HH:mm AM/PM”
#	h. This script should not take any argument, so if there is any argument supplied print an error
#*******************************************************************
if [ $# -gt 0 ];
	then
	echo "error: too many arguments"
	echo "usage: ./hello.sh"
	exit 1
fi
# setting hour min and username variables
hour=$(date +"%H")
#time=$(date +"%T")
minutes=$(date +"%M")
userName=$(whoami)

# check hour to detemermine am or pm
if [ $hour -ge 12 ];
	then
	ampm="PM"
else
	ampm="AM"
fi

# changes 24 hr clock to 12 hr clock
# might not be needed 
case $hour in
	13) newHour="1:$minutes $ampm";;
	14) newHour="2:$minutes $ampm";;
	15) newHour="3:$minutes $ampm";;
	16) newHour="4:$minutes $ampm";;
	17) newHour="5:$minutes $ampm";;
	18) newHour="6:$minutes $ampm";;
	19) newHour="7:$minutes $ampm";;
	20) newHour="8:$minutes $ampm";;
	21) newHour="9:$minutes $ampm";;
	22) newHour="10:$minutes $ampm";;
	23) newHour="11:$minutes $ampm";;
	24) newHour="12:$minutes $ampm";;
esac

time=$newHour

# checks hour then displays message according to time 
if [ $hour -ge 6 ] && [ $hour -lt 12 ];
	then
	echo "Hello $userName, it is $time. Have a good morning!"
elif [ $hour -ge 12 ] && [ $hour -lt 18 ];
	then
	echo "Hello $userName, it is $time. Have a good afternoon!"
elif [ $hour -ge 18 ] && [ $hour -lt 24 ];
	then
	echo "Hello $userName, it is $time. Have a good evening!"
elif [ $hour -ge 18 ] && [ $hour -lt 24 ];
	then
	echo "Hello $userName, it is $time. Don't work too hard!"
fi
exit 0
