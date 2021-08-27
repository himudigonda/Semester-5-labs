def wt(bt_list):
    print("****************************")
    print("Waiting Time")
    wt_list = list()
    wt_list.append(0)
    for i in range(4):
        wt_list.append(bt_list[i]+wt_list[i])
    print(wt_list)
    return wt_list


def tt(wt_list, bt_list):
    print("****************************")
    print("Total Time")
    tt_list = list()
    for i in range(len(bt_list)):
        val = bt_list[i]+wt_list[i]
        tt_list.append(val)
    print(tt_list)


p_list = ['p1', 'p2', 'p3', 'p4', 'p5']
bt_list = list()  # 2 3 4 5 6
print("****************************")
print("Enter burst times of the processes:")
for i in range(len(p_list)):
    print("    Enter burst times of the P"+str(i+1)+" : ")
    val = input("    ")
    bt_list.append(int(val))
print("****************************")
print("Process List")
print(p_list)
print("****************************")
print("Burst Time")
print(bt_list)
wt_list = wt(bt_list)
tt(wt_list, bt_list)
print("****************************")
