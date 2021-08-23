# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 3

FILE=$1
# string="The Big browN FoX JumpeD oVeR THE LazY Dog"
lowercase=$(echo $FILE | tr '[A-Z]' '[a-z]'])

# change file name
echo $lowercase
mv $FILE $lowercase
