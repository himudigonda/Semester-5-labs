# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 3

read -p "Enter text file name: " FILENAME
read -p "Password/Key: " PASSWORD
crypt $PASSWORD < $FILENAME > $FILENAME.cpy

echo "$FILENAME.cpy is now created!"