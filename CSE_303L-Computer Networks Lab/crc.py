#!/usr/bin/env python3

def crc(msg, div, code='000'):
    msg = msg + code
    msg = list(msg)
    div = list(div)
    print(msg,div)
    for i in range(len(msg)-len(code)):
        if msg[i] == '1':
            for j in range(len(div)):
                msg[i+j] = str((int(msg[i+j])+int(div[j]))%2)
                print(i,j, msg[i+j])
    return ''.join(msg[-len(code):])

print('Test 1 ---------------------------')
# Use a divisor that simulates: x^3 + x + 1
msg = '1010'
div = '1011'

print('Input message:', msg)
print('Divisor:', div)
code = crc(msg, div)
print('Output code:', code)
print('Success:', crc(msg, div, code) == '000')
# # TEST 2 ####################################################################
# print('Test 2 ---------------------------')
# # Use a divisor that simulates: x^2 + 1
# div = '0101'
# msg = '00101111011101'

# print('Input message:', msg)
# print('Divisor:', div)

# # Enter the message and divisor to calculate the error-checking code
# code = crc(msg, div)

# print('Output code:', code)

# # Perform a test to check that the code, when run back through, returns an
# # output code of '000' proving that the function worked correctly
# print('Success:', crc(msg, div, code) == '000')