#! /bin/bash
#! @author: @ruhend (Mudigonda Himansh)
#! Assignment 4

str=$1$2
length=$((wc -c <<< $str))

echo "Concated String : "
echo $str
echo "Length : "
wc -c <<< $str
