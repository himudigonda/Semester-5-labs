#! /bin/bash

for a in 1 2 3 4 5 6
do
    echo $a
done

for a in  {1..100}
do
    echo $a
done

for a in {1..10..2}
do
    echo $a
done


for a in  {1..10}
do
    if  [[ $a == 3 ]] || [[ $a == 5 ]]
    then
        echo $a
    fi
done

for i in $(seq 1 3 20)
do
   echo "Welcome $i times"
done


for (( b=1; b<=5; b=b+2 ))
do  
   echo "Welcome $b times"
done

for file in /home/ruhend/Documents
do 
    echo $(file)
done