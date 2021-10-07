# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 2

#! Question 3
echo "Enter Size : "
read N
i=1
sum=0
echo "Enter Numbers : "
while [ $i -le $N ]; do
    read num
    sum=$((sum + num))
    i=$((i + 1))
done
avg=$(echo $sum / $N | bc -l)

echo $avg
