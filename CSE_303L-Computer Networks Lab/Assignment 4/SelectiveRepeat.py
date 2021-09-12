#!/usr/bin/env python3
#! @author: @ruhend(Mudigonda Himansh)
#! Assignment 4
#! Selective Repeat

"""
 [summary]

Returns:
    [type]: [description]
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
    dataBits = [int(x) for x in dataStr.split()]
    Timeout = 5
    return windowSize, dataBits, Timeout


def SR(windowSize, DataBits, Timeout):
    """
    SRN [The main function that makes the program work]

    Args:
        windowSize ([int])
        DataBits ([list])
        Timeout ([int])
    """
    lenDataBits = len(DataBits)
    i = 0
    ackIssueFlag = False  # A Status Flag to mark when an issue occured
    # To keep a track of the data being sent RN. This is the sliding window
    currentWindow = list()
    for i in range(windowSize):
        currentWindow.append(DataBits[i])  # Filling the window with elements
    i += 1
    while i <= lenDataBits+windowSize:  # While loop to loop over the elements
        if len(currentWindow) <= windowSize:  # To Handle Edge Cases
            if currentWindow != []:  # If the currentWindow size is not empty...
                if ackIssueFlag == False:  # If the status Flag is not triggered...
                    if i <= lenDataBits:   # While loop to loop over the elements below the window size limit
                        # ^ These below apf to cover Edge Cases
                        print(" > Sending Element with Indeces : ",
                              i-windowSize, "to", i-1)
                    elif i == lenDataBits:
                        print(" > Sending Element with Indeces : ", i-windowSize)
                    else:
                        print(" > Sending Element with Indeces : ",
                              i-windowSize, "to", lenDataBits-1)
                    print(currentWindow)
                if ackIssueFlag:  # If the status Flag is triggered...
                    print(" > Re-Sending Element with Index : ",
                          i-windowSize)  # Init re-send
                    print(" ± Resending", i-windowSize,
                          "th bit with issue : ", DataBits[i-windowSize])
                # Do the parallel user(Receiver) input thingy
                a, o, e = select.select([sys.stdin], [], [], Timeout)
                if (a):   # If input is provided
                    ack = sys.stdin.readline().strip()
                    # if the ack matches the index of the databit sent, then accept
                    if ack == str(i-windowSize):
                        # This could be anything, I've taken this as it would be easier to evaluate
                        print(" + Ack Received!")
                        currentWindow.pop(0)  # Popping the sent element
                        if i < lenDataBits:  # If next elements exist, append them
                            currentWindow.append(DataBits[i])
                        i += 1  # Incremented i
                        ackIssueFlag = False  # Reset Trigger
                    else:
                        print(" - Ack Error... Sending window elements again...")
                        ackIssueFlag = True  # Activate Trigger as Issue has occured
                else:
                    # No need to Activate Trigger here
                    print(" - Timeout Error")
                    # ? Why is it not necessary?
                    # Since we are implementing a Sliding Window protocol, for timeout the entire window is retransmitted
                    # There are cases, where only one bit might get lost, but would require Parallel Programming, and Multi-Threading.
                    #  Since, the objective is to code the logic of the protocol, This Edge Case is ignored.
            else:
                print("**** End of Transmission ****")
                break


def main():
    """
    main [Main Function]
    """
    print("**** Start of Transmission ****")
    windowSize, dataBits, Timeout = InputFunc()
    SR(windowSize, dataBits, Timeout)


if __name__ == '__main__':
    main()
