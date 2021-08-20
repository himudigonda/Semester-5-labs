#!/usr/bin/env python3

def crc(msg, div, code='000'):
    msg = msg + code  # Concatinating message and code
    msg = list(msg)  # Self explainatory
    div = list(div)  # Self explainatory
    # print(msg,div) # Self explainatory

    for i in range(len(msg)-len(code)):
        if msg[i] == '1':
            for j in range(len(div)):
                # Performing XOR logic using %2 to remove the need of intgrating remainder with the divisor again.
                msg[i+j] = str((int(msg[i+j])+int(div[j])) % 2)
                # print(i,j, msg[i+j])
    return ''.join(msg[-len(code):])


# Use a divisor that simulates: x^3 + x + 1
msg = '1010'
div = '1011'
print("Encode: ", msg, div)
print('Message:', msg)
print('Divisor:', div)
code = crc(msg, div)
print('Output code:', code)


# FALSE
code = '101'
print("Decode: Testing with code = ", code)
print('Corrupt:', crc(msg, div, code) != '000')
# TRUE
code = '011'
print("Decode: Testing with code = ", code)
print('Corrupt:', crc(msg, div, code) != '000')
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
