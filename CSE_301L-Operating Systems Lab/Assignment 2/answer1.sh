# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 2

#! Question 1
read -p "Enter the three numbers : " number1 number2 number3

if [[ $number1 -ge $number2 && $number1 -ge $number3 ]]; then
    echo "$number1 is the greatest number"
fi

if [[ $number2 -ge $number3 && $number2 -ge $number1 ]]; then
    echo "$number2 is the greatest"
fi

if [[ $number3 -ge $number1 && $number3 -ge $number2 ]]; then
    echo "$number3 is the greatest"
fi
