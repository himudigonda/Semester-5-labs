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
import select    # Will be used to timeout transmissions
import string  

def InputFunc():
    dataStr = '1010010011'
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
        #^ print("appended", DataBits[i])
    i += 1
    while i <= len(DataBits)+windowSize:
        #^ print(i)
        if len(currentWindow) <= windowSize:
            if currentWindow != []:
                print(currentWindow)    
                a, o, e = select.select([sys.stdin], [], [], Timeout)
                if (a):
                    ack = sys.stdin.readline().strip()
                    if ack == str(i-windowSize):
                        print(" + Ack Received!")
                        currentWindow.pop(0)
                        if i < len(DataBits):
                            currentWindow.append(DataBits[i])
                        i += 1
                    else:
                        print(" - Ack Error... Sending window elements again...")
                else:
                    print(" - Timeout Error")
            else:
                print("**** End of Transmission ****")
                break
def main():
    print("**** Start of Transmission ****")
    windowSize, dataBits, Timeout = InputFunc()
    GBN(windowSize, dataBits, Timeout)

if __name__ == '__main__':
    main()
