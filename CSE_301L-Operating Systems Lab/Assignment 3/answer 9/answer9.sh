# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 3

Source="ans9.txt"
Wdlist="wordlist.txt"

cat $Source | sed 's/ /\n/g' | sed '/^$/d' | sort -u > $Wdlist