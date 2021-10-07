#! /bin/bash

# if command
# then
# 	statements
# 	statements
# 	statements
# fi


# if condition; then
# 	statements
# elif
# 	statements
# elif
# 	statements
# else
# 	statements
# fi


if [[ $1 -gt 0 ]]
then
	echo "$1 is +ve"
else
	echo "$1 is -ve"
fi

if test $2 -gt 0
then
	echo "$2 is +ve"
else
	echo "$2 is -ve"
fi

if  [ $3 == 0 ]
then
	echo "$3 is 0"
else
	echo "$3 is not 0"
fi

