# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 2

#! Question 10
clear
read -p "Enter a string to be entered : " str
echo
len=$(($(echo $str | wc -c) - 1))
i=1
j=$((len / 2))
while [[ $i -le $j ]]; do
    k=$(echo $str | cut -c $i)
    l=$(echo $str | cut -c $len)
    if test $k != $l; then
        echo "String is not palindrome"
        exit
    fi
    i=$(expr $i + 1)
    len=$(expr $len - 1)
done
echo "String is palindrome"
