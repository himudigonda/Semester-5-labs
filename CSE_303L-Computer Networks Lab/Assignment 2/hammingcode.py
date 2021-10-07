#! /usr/bin/python3
#! @author: @ruhend (Mudigonda Himansh)
#! CN Assignment 2

"""[Assignment 2: Hamming Code]
    Input     : 0010
    Placement : __0_010
    Output    : 0101010
"""


def inputPhase():
    data = [int(x) for x in input().split()]
    k = len(data)     #
    flag = False
    p = 0                           # Total number of pairity bits
    while not flag:
        p += 1
        if 2**p >= p+k+1:
            flag = True
    n = p + k
    print("This is  {},{} Hamming Code".format(n, k))
    return data, n, p, k


def makeArray(n):
    arr = [0]*n
    print(arr)


def pairityAndMessageLOC(n, p):
    PairityPOS = list()
    MessagePOS = list()
    for i in range(p):
        PairityPOS.append(2**i)
    for i in range(1, n+1):
        if i not in PairityPOS:
            MessagePOS.append(i)
        pass
    print(PairityPOS, MessagePOS)
    return PairityPOS, MessagePOS


def pairityBitVal():
    # ? p1 : check 1 bit, skip 1 bit
    # ? p2 : check 2 bits, skip 2 bits
    # ? pn : check n bits, skip n bits
    p1 = [0, 2, 4, 6, 8]
    p2 = [3, 6, 7]
    p4 = [5, 6, 7]
    p8 = [9]

    pass


def main():
    data, n, p, k = inputPhase()
    makeArray(n)
    PairityPOS = pairityAndMessageLOC(n, p)


if __name__ == '__main__':
    main()
