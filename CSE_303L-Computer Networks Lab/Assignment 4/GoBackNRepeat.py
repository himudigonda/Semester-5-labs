#!/usr/bin/env python3
#! @author: @ruhend(Mudigonda Himansh)
#! Assignment 4
#! Go Back N Repeat

''' [GoBackNRepeat]
'''

import sys, select # Will be used to timeout transmissions


def InputFunc():
    dataStr = '1 2 3 4 5 6 7 8 9 0'
    windowSize = 5
    dataBits = dataStr.split()
    Timeout = 5
    return windowSize, dataBits, Timeout

def send(dataSent, index):
    print("Data Sent  : ", dataSent)
    print("Data Index : ", index)

def GBN(windowSize, DataBits, Timeout):
    lenDataBits = len (DataBits)
    statusFlag = False
    i = 0
    while statusFlag==False:
        send(DataBits[i], i)
        a, o, e = select.select( [sys.stdin], [], [], Timeout )
        if (a):
            comp = "ack "+str(i)
            if sys.stdin.readline().strip() == comp:
                # statusFlag = True
                if (i == lenDataBits):
                    statusFlag = True
                print("Hi")
        i = i+1

def main():
    windowSize, dataBits, Timeout = InputFunc()
    GBN(windowSize, dataBits, Timeout)

if __name__ == '__main__':
    main()