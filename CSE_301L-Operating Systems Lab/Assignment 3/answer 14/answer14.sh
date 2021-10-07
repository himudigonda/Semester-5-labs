# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 3

file="ans14.txt"
counter=0

odd="ans14odd.txt" # odd file name
even="ans14even.txt"
if [ ! -f $file ]; then
    echo "$file not a file!"
    exit 2
fi

while read line; do
    # find out odd or even line number
    isEvenNo=$(($counter % 2))

    if [ $isEvenNo -eq 0 ]; then
        # odd match; copy all odd lines $out file
        echo $line >>$odd
    fi
    if [ $isEvenNo -eq 1 ]; then
        # odd match; copy all odd lines $out file
        echo $line >>$even
    fi
    # increase counter by 1
    ((counter++))
done <$file

