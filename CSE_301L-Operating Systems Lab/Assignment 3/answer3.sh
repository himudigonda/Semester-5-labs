# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 3

a=($(wc <<<$1))
chars=${a[2]}
chars=$((chars-1))
echo "length of the string is: $chars"
