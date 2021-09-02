#! /bin/bash
#! @author: @ruhend (Mudigonda Himansh)
#! Assignment 4

FILE="testFile2.txt"

count_a=$(grep -o " a " $FILE | wc -l | sed 's/[a-zA-z. ]//g')
count_an=$(grep -o " an " $FILE | wc -l | sed 's/[a-zA-z. ]//g')
count_the=$(grep -o " the " $FILE | wc -l | sed 's/[a-zA-z. ]//g')

# sum=$(count_a+count_an+count_the)

sum=$((count_a + count_an + count_the))

echo  $sum