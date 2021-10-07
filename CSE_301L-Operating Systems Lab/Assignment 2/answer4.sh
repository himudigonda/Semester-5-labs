# ! /bin/bash
# @author : @ruhend (Mudigonda Himansh)
# Assignment 2

#! Question 4
echo "Enter the number to check if it is prime or not : "
read prime_target

if [[ $prime_target -eq 2 || $prime_target -eq 1 || $prime_target -eq 0 ]]; then
    echo "Prime"
    exit
fi

if [[ $prime_target%2 -eq 0 ]]; then
    prime_half=$(($prime_target / 2))
else
    # prime_target=$((prime_target + 1))
    prime_half=$(((prime_target + 1) / 2))
fi
i=2
while [ $i -le $prime_half ]; do
    # echo "$prime_half $prime_target $i $(($prime_target % $i))"
    if [[ $(($prime_target % $i)) == 0 ]]; then
        # echo "Not Prime $prime_half $prime_target $i $(($prime_target % $i))"
        echo "Not Prime"
        exit
    fi
    i=$((i + 1))
done
echo "Prime"
