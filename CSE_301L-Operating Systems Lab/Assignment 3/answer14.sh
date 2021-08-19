# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 3

cp alpha.txt gamma.txt

file="gamma.txt"
counter=0

odd="gammaodd.txt" # odd file name
even="gammaeven.txt"
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

# rename temp out file
/bin/mv $odd oddfile.txt
/bin/mv $even evenfile.txt
