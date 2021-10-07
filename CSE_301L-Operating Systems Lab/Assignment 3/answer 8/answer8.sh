# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 3

read -p "Enter text file name: " FILENAME
# cat $FILENAME | openssl dgst -sha256
echo "md5sum" > ans8encrypt.txt
md5sum $FILENAME >> ans8encrypt.txt
echo "md5sum" >> ans8encrypt.txt
sha256sum $FILENAME >> ans8encrypt.txt