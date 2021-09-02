#! /bin/bash
#! @author: @ruhend (Mudigonda Himansh)
#! Assignment 4

# Number of vowels in a given text file. •
# Number of blank spaces. •
# Number of characters. •
# Number of symbols. •
# Number of lines •
file="testFile5.txt"
str=$(cat $file)
echo "Number of vowels: "
echo $str | perl -ne "print s/[aeiou]/[aeiou]/g"
echo ""

echo "Number of Blank Spaces: "
echo $str | perl -ne "print s/[ ]/[ ]/g"
echo ""

echo "Number of Characters: "
echo $str | perl -ne "print s/[\w\W,.]/[\w\W,.]/g"
echo ""

echo "Number of Symbols: "
echo $str | perl -ne "print s/[^a-zA-Z0-9., ]/[^a-zA-Z0-9., ]/g"
echo ""

echo "Number of Lines: "
wc -l $file | sed 's/[a-zA-z. ]//g'
echo ""
