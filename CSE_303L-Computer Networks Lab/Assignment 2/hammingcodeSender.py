
def calcRedundantBits(m):
    # Use the formula 2 ^ r >= m + r + 1
    # to calculate the no of redundant bits.
    # Iterate over 0 .. m and return the value
    # that satisfies the equation
    for i in range(m):
        if(2**i >= m + i + 1):
            return i


def posRedundantBits(data, r):
    # Redundancy bits are placed at the positions
    # which correspond to the power of 2.
    j = 0
    k = 1
    m = len(data)
    res = ''
    # If position is power of 2 then insert '0'
    # Else append the data
    for i in range(1, m + r+1):
        if(i == 2**j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            # 1011001 
            # 101'0'10'0'01'0''0'
            # 
            # 
            k += 1
    # The result is reversed since positions are
    # counted backwards. (m + r+1 ... 1)
    return res[::-1]



def main():
    data = '1011001'
    m    = len(data)
    r    = calcRedundantBits(m)
    arr  = posRedundantBits(data, r)
    print(data, m, r, arr)


if __name__ == '__main__':
    main()
