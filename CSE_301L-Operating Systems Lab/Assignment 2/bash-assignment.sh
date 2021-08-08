#! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 2

#!  QUESTIONS
# Write the shell script for each of these programs and submit the  word file with code, input and output ?
# 1.    Write a script to find the greatest of three numbers (numbers passed as command line parameters)
# 2.    Write a script to check whether the given no. is even/odd
# 3.    Write a script to calculate the average of n numbers.
# 4.    Write a script to check whether the given number is prime or not.
# 5.    Write a script to check whether the given input is a number or a string.
# 6.    Write a script to compute no. of characters and words in each line of given file.
# 7.    Write a script to print the Fibonacci series upto n terms
# 8.    Write a script to calculate the factorial of a given number
# 9.    Write a script to calculate the sum of digits of the given number
# 10.   Write a script to check whether the given string is a palindrome

# #! Question 1
# read -p "Enter the three numbers : " number1 number2 number3

# if [[ $number1 -gt $number2 && $number1 -gt $number3 ]]; then
#     echo "$number1 is the greatest number"
# fi

# if [[ $number2 -gt $number3 && $number2 -gt $number1 ]]; then
#     echo "$number2 is the greatest"
# fi

# if [[ $number3 -gt $number1 && $number3 -gt $number2 ]]; then
#     echo "$number3 is the greatest"
# fi

# #! Question 2
# read -p "Enter the number to find if a number is even/odd : " evenoddnumber

# if [[ $(expr $evenoddnumber % 2) == 0 ]]; then
#     echo "$evenoddnumber is an even number"
# else
#     echo "$evenoddnumber is an odd number"
# fi

# #! Question 3
# echo "Enter Size : "
# read N
# i=1
# sum=0
# echo "Enter Numbers : "
# while [ $i -le $N ]; do
#     read num
#     sum=$((sum + num))
#     i=$((i + 1))
# done
# avg=$(echo $sum / $N | bc -l)

# echo $avg
