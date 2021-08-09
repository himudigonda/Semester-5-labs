# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 2

#! Question 6
file_path=./stats.txt

echo "Words per line"
while read p; do
    wc -w <<<$p
done <$file_path

echo "Chars per line"
while read p; do
    wc -c <<<$p
done <$file_path
