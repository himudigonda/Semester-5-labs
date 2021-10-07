#! /usr/bin/python3
#! @author : @ruhend(Mudigonda Himansh)
#! Non preemptive SRTF Scheduling algorithm

"""[What is SRTF]
    SRTF is a scheduling algorithm standing for
    shortest time remaining first.
"""


def processInput():
    # ProcessNumber : [BurstTime, ArrivalTime]
    ArrivalTime = 0
    ProcessList = {
        1: 6,
        2: 2,
        3: 7,
        4: 1
    }
    return ProcessList


def non_preemptive():
    ProcessList = processInput()
    TotalTurnOverTime = 0
    ProcessSeq = list()
    processListSorted = sorted(ProcessList.items(), key=lambda x: x[1])
    for i in range(len(ProcessList)):
        if processListSorted:
            print(processListSorted)
            remove_key = processListSorted.pop(0)
            TotalTurnOverTime += remove_key[1]
            ProcessSeq.append(remove_key[0])
    print("Process Flow         : ", ProcessSeq)
    print("Total Turn Over Time : ", TotalTurnOverTime)


def non_preemptive():
    ProcessList = processInput()
    TotalTurnOverTime = 0
    ProcessSeq = list()
    processListSorted = sorted(ProcessList.items(), key=lambda x: x[1])
    for i in range(len(ProcessList)):
        if processListSorted:
            print(processListSorted)
            remove_key = processListSorted.pop(0)
            TotalTurnOverTime += remove_key[1]
            ProcessSeq.append(remove_key[0])
    print("Process Flow         : ", ProcessSeq)
    print("Total Turn Over Time : ", TotalTurnOverTime)


if __name__ == '__main__':
    non_preemptive()
