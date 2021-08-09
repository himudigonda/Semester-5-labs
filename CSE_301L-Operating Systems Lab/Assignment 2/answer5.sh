# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 2

#! Question 5
read -p "Enter Number or String : " numorstring

echo "$numorstring" | grep "^[A-Za-z]*$"
val="$?"

if [[ $val == 0 ]]; then
    echo "String"
    break
fi

echo "$numorstring" | grep "^[0-9]*$"
val="$?"

if [[ $val == 0 ]]; then
    echo "Number"
fi
