# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 2

#! Question 2
read -p "Enter the number to find if a number is even/odd : " evenoddnumber

if [[ $(expr $evenoddnumber % 2) == 0 ]]; then
    echo "$evenoddnumber is an even number"
else
    echo "$evenoddnumber is an odd number"
fi
