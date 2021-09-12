#!/usr/bin/env python3
#! @author: @ruhend(Mudigonda Himansh)
#! Assignment 4
#! Go Back N

"""
 [summary]

Returns:
    [type]: [description]
"""

import sys
import select
import string  # Will be used to timeout transmissions


def InputFunc():
    dataStr = '123456789987654321'
    dataStr = " ".join(dataStr)
    windowSize = 4
    dataBits = [int(x) for x in dataStr.split()]
    Timeout = 5
    return windowSize, dataBits, Timeout


def send(dataSent, index, windowSize):
    print("Data Sent  : ", dataSent)
    print("Data Index : ", index)


def GBN(windowSize, DataBits, Timeout):
    lenDataBits = len(DataBits)
    i = 0
    currentWindow = list()
    for i in range(windowSize):
        currentWindow.append(DataBits[i])
        print("appended", DataBits[i])
    i += 1
    while i <= len(DataBits)+windowSize:
        print(i)
        if len(currentWindow) <= windowSize:
            print(currentWindow)
            a, o, e = select.select([sys.stdin], [], [], Timeout)
            if (a):
                ack = sys.stdin.readline().strip()
                if ack == str(i-windowSize):
                    print(" + Ack Received!")
                    if currentWindow != []:
                        currentWindow.pop(0)
                        if i < len(DataBits):
                            currentWindow.append(DataBits[i])
                        i += 1
                    else:
                        print("****End of Transmission****")
                        break
                else:
                    print(" - Ack Error")
                    # print("Expected", str(i-windowSize))
                    # print("Received", str(ack))
            else:
                print(" - Timeout Error")
    # print(currentWindow)
    # currentWindow.pop()
    # print(currentWindow)


def main():
    windowSize, dataBits, Timeout = InputFunc()
    GBN(windowSize, dataBits, Timeout)


if __name__ == '__main__':
    main()
