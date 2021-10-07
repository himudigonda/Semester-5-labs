#! /usr/bin/env python3
#! @author: @ruhend(Mudigonda Himansh)
#! Assignment 5
#! SRTF

proc_info = {
    #   a, b, r
    1: [0, 1, 1],
    2: [1, 3, 3],
    3: [0, 4, 4],
    4: [3, 2, 2],
    5: [1, 2, 2]
}


def main():
    flag = True
    procs_left = list()
    proc_flow = list()
    proc_stat = {
        #   completion_time, waiting_time
        1: [0],
        2: [0],
        3: [0],
        4: [0],
        5: [0]
    }
    run = 0
    while flag == True:
        for i in proc_info:
            current_proc = proc_info[i]
            if current_proc[2] != 0 and current_proc[0] == run and i not in procs_left:
                procs_left.append(i)
                # print("rstarst")
        for i in procs_left:
            print(procs_left, i, proc_flow)
            proc_info[i][2] -= 1
            if proc_info[i][2] == 0 and i in procs_left:
                procs_left.remove(i)
            proc_flow.append(i)
        run += 1
        if not procs_left:
            flag = False
main()
