#! /bin/bash
#! @author: @ruhend (Mudigonda Himansh)
#! Assignment 4

calc() {
    echo "What do you wanna do?"
    echo "1. Addition"
    echo "2. Subraction"
    echo "3. Multiplication"
    echo "4. Division"
    echo "x. Exit"
    read -p "Choice : " choice

    if [[ $choice == 1 ]]; then
        read -p "Enter numbers 1 : " a
        read -p "Enter numbers 2 : " b
        echo "==>" $((a + b))
        calc
    elif [[ $choice == 2 ]]; then
        read -p "Enter numbers 1 : " a
        read -p "Enter numbers 2 : " b
        echo "==>" $((a - b))
        calc
    elif [[ $choice == 3 ]]; then
        read -p "Enter numbers 1 : " a
        read -p "Enter numbers 2 : " b
        echo "==>" $((a * b))
        calc
    elif [[ $choice == 4 ]]; then
        read -p "Enter numbers 1 : " a
        read -p "Enter numbers 2 : " b
        echo "==>" $((a / b))
        calc
    else
        echo "==> Exiting"
        exit
    fi
}

calc
