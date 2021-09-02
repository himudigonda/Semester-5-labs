#! /bin/bash
#! @author : @ruhend (Mudigonda Himansh)
#! Assignment 4
file=testFile1.txt
lines=$(wc -l $file | sed 's/[a-zA-z. ]//g')
line=1
echo "Total Lines: $lines"

while [ $line -le $lines ]
do
    echo "$line"
    sed "${line}q;d" $file
    line=$((line+1))
    if [[ $(( line % 15 )) == 1 ]]
    then
        read -n1 temp
    fi
done