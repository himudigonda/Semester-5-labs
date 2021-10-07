# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 3

FILE=$(cat ans12.txt)
# string="The Big browN FoX JumpeD oVeR THE LazY Dog"
echo $FILE | tr "[:upper:]" "[:lower:]" > ans12.txt
