# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 3

FILE="ans10.txt"
OPFILE="ans10nospace.txt"

sed -e 's/[\t ]//g;/^$/d' $FILE > $OPFILE