# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 3

cp alpha.txt beta.txt

file="beta.txt"
counter=0

out="betaodd.txt" # odd file name

if [ ! -f $file ]; then
    echo "$file not a file!"
    exit 2
fi

while read line; do
    # find out odd or even line number
    isEvenNo=$(($counter % 2))

    if [ $isEvenNo -eq 0 ]; then
        # odd match; copy all odd lines $out file
        echo $line >>$out
    fi
    # increase counter by 1
    ((counter++))
done <$file
# remove input file
/bin/rm -f $file

# rename temp out file
/bin/mv $out $file
