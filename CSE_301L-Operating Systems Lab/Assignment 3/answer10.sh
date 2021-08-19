# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 3

FILE="normal2lower.txt"
OPFILE="removespaces.txt"

sed -e 's/[\t ]//g;/^$/d' $FILE > $OPFILE