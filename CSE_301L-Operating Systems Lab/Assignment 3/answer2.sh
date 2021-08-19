# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 3

read -p "Enter the string: " charl5
a=($(wc <<<$charl5))
chars=${a[2]}
chars=$((chars-1))


if [[ chars -lt 5 ]]; then
    echo "string size less than 5"
else
    echo "string size is greater than 5"
fi
