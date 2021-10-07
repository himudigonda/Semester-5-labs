# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 3

ls -l
read -p "Enter the file name: " file_name

echo "Stat full: "
stat $file_name
echo "Stat modify: "
stat $file_name | grep "Modify"
echo "Stat F: "
ls -la | grep $file_name
