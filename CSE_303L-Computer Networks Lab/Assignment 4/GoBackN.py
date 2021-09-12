#!/usr/bin/env python3
#! @author: @ruhend(Mudigonda Himansh)
#! Assignment 4
#! Go Back N

"""
[Go Back N]
"""

import sys
import select    # Will be used to timeout transmissions
import string


def InputFunc():
    """
    InputFunc [This Function is used to take declare input.]

    Returns:
        [int]: [windowSize]
        [int]: [dataBits]
        [int]: [Timeout]
    """
    dataStr = '1010010011'
    dataStr = " ".join(dataStr)
    windowSize = 4
    # Makes the input string to a list
    dataBits = [int(x) for x in dataStr.split()]
    Timeout = 5
    # Returns the variables to the main function
    return windowSize, dataBits, Timeout


def send(dataSent, index, windowSize):
    """
    send [summary]

    Args:
        dataSent ([list])
        index ([int])
        windowSize ([int])
    """
    print("Data Sent  : ", dataSent)
    print("Data Index : ", index)


def GBN(windowSize, DataBits, Timeout):
    """
    GBN [The main function that makes the program work]

    Args:
        windowSize ([int])
        DataBits ([list])
        Timeout ([int])
    """
    lenDataBits = len(DataBits)
    i = 0
    # To keep a track of the data being sent RN. This is the sliding window
    currentWindow = list()
    for i in range(windowSize):
        currentWindow.append(DataBits[i])  # Filling the window with elements
    i += 1
    while i <= lenDataBits+windowSize:  # While loop to loop over the elements
        if len(currentWindow) <= windowSize:  # To Handle Edge Cases
            if currentWindow != []:  # If the currentWindow size is not empty...
                print(currentWindow)
                # Do the parallel user(Receiver) input thingy
                a, o, e = select.select([sys.stdin], [], [], Timeout)
                if (a):  # If input is provided
                    ack = sys.stdin.readline().strip()  # Read the input
                    # if the ack matches the index of the databit sent, then accept
                    if ack == str(i-windowSize):
                        # This could be anything, I've taken this as it would be easier to evaluate
                        print(" + Ack Received!")
                        currentWindow.pop(0)  # Popping the sent element
                        if i < lenDataBits:  # If next elements exist, append them
                            currentWindow.append(DataBits[i])
                        i += 1  # Incremented i
                    else:
                        print(" - Ack Error... Sending window elements again...")
                        #  Nothing needs to be done as i is not incremented
                else:
                    print(" - Timeout Error")
                    #  Nothing needs to be done as i is not incremented
            else:
                print("**** End of Transmission ****")
                break


def main():
    """
    main [Main Function]
    """
    print("**** Start of Transmission ****")
    windowSize, dataBits, Timeout = InputFunc()
    GBN(windowSize, dataBits, Timeout)


if __name__ == '__main__':
    main()
