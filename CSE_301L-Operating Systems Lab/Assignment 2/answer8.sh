# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 2

#! Question 8
read -p "Enter the number to find factorial : " limit
i=$limit
fact=1
while [[ $i -gt 0 ]]; do
    # echo "$i"
    fact=$((fact * i))
    i=$((i - 1))
done
echo "$fact"
