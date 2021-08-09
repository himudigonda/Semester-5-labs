# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 2

#! Question 9
read -p "Enter the number to be summed place by place : " input
sum=0
while [[ input -gt 0 ]]; do
    # echo "$input"
    remainder=$((input % 10))
    sum=$((sum + remainder))
    input=$((input / 10))
done
echo "$sum"
