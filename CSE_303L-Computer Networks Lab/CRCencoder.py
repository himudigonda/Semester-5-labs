#! /usr/bin/python3
#! @authot: @ruhend (Mudigonda Himansh)
#! CRC Encoder

def list2int(mylist):
    char_divisor = [str(integer) for integer in mylist]
    str_divisor = "". join(char_divisor)
    int_divisor = int(str_divisor,2 )
    return int_divisor

def DecimalToBinary(num):
    answer = []
    if num >= 1:
        DecimalToBinary(num // 2)
    bindigit = num % 2
    answer.append(bindigit)
    return answer

def perform_XOR(divisor, divider):
    divider = list2int(divider)
    divisor = list2int(divisor)
    xor = divider^divisor 
    xor = DecimalToBinary(xor)
    print("xor ",xor)


dataword = [int (i) for i in input().split(' ')]
# print(dataword)

divisor = [int (i) for i in input().split(' ')]
# print(divisor)

extra_zeros = len(divisor)-1
for i in range(extra_zeros):
    dataword.append(0)
# print(dataword)
remainder = 0
i = 0
while (dataword):
    i = i+1
    print("iteration: ",i)
    if remainder==0:
        first_element = dataword[0]
    else:
        first_element=remainder[0]
    divider = dataword[0:4]
    if first_element:
        print("remainder: ",remainder )
        if remainder!=0:
            divider = remainder
        print(divider)
        remainder = perform_XOR(divisor, divider)
        print(remainder)
        # divider.pop(0)
        dataword.pop(0)
    else:
        # divider.pop(0)
        dataword.pop(0)
    # print(first_element)
