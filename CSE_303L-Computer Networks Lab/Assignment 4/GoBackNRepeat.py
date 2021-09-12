#!/usr/bin/env python3
#! @author: @ruhend(Mudigonda Himansh)
#! Assignment 4
#! Go Back N Repeat

"""
 [summary]

Returns:
    [type]: [description]
"""

import sys, select, string # Will be used to timeout transmissions


def InputFunc():
    dataStr = '1011010'
    dataStr = " ".join(dataStr)
    windowSize = 4
    dataBits = [int(x) for x in dataStr.split()]
    Timeout = 5
    return windowSize, dataBits, Timeout

def send(dataSent, index,windowSize):
    print("Data Sent  : ", dataSent)
    indexArray = list()
    count = 0
    while count<len(dataSent):
        indexArray.append(index)
        index += 1
        count += 1
    print("Data Index : ", indexArray)

def calcComp(i,windowSize):
    comp = ''
    for j in range(windowSize):
        comp += ' '+str(i)
        i += 1 
    comp = comp.strip()
    return comp

def GBN(windowSize, DataBits, Timeout):
    lenDataBits = len (DataBits)
    i = 0
    lenToSend =lenDataBits-windowSize
    rem = lenToSend%windowSize
    q = lenToSend//windowSize
    while i <=rem+q*windowSize:
        send(DataBits[i:i+windowSize], i,windowSize)
        comp = calcComp(i,windowSize)
        print(">",comp)
        a, o, e = select.select( [sys.stdin], [], [], Timeout )
        if (a):
            if sys.stdin.readline().strip() == comp:
                i+=windowSize
            else:       
                print(" - Ack Error")
        else:
            print(" - Timeout Error")
    print(i,lenDataBits)
    while i <= lenDataBits:
        send(DataBits[-rem:], i,windowSize)
        comp = calcComp(i,rem)
        print(">",comp)
        a, o, e = select.select( [sys.stdin], [], [], Timeout )
        if (a):
            if sys.stdin.readline().strip() == comp:
                i+=windowSize
            else:       
                print(" - Ack Error")
        else:
            print(" - Timeout Error")

def main():
    windowSize, dataBits, Timeout = InputFunc()
    GBN(windowSize, dataBits, Timeout)

if __name__ == '__main__':
    main()