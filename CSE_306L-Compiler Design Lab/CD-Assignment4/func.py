#! /usr/bin/python3
#! @author : @ruhend
#! CD Assignment 4


def inputF():
    lines = []
    while True:
        line = input()
        if line:
            line.strip()
            line.replace("\t","")
            lines.append(line)
        else:
            break
    return lines


[
['func', 'muladd', ':', 'int', 'a', ',', 'int', 'b', ',', 'int', 'c', ':', 'int', '{'],
['int', 'd',  '=', 'a', '*', 'b',';'],
['int e = d + c;'],
['return d, e;'],
['}']
]


[
'func muladd : int a, int b, int c : int {',
'int d = a * b;',
'int e = d + c;',
'return d, e;',
'} '
]

def solve () :
    print(inputF())
    print("hi")
    pass

solve()