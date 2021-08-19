import keyword
import re

f = open('InputProg.c', 'r')

keywords = list('auto', 'break', 'case', 'char', 
                'const', 'continue', 'default', 'do', 
                'double', 'else', 'enum', 'extern',
                'float', 'for', 'goto', 'if',
                'int', 'long', 'register', 'return',
                'short', 'signed', 'sizeof', 'static',
                'struct', 'switch', 'typedef', 'union',
                'unsigned', 'void', 'volatile', 'while',
                )
print(keywords)
operators = {'=', '+', '-', '*', '/', '++', '--', '^','%'}


operators = {'=': 'Assignment Operator', '+': 'Addition Operator', '-': 'Substraction Operator',
             '/': 'Division Operator', '*': 'Multiplication Operator', '++': 'increment Operator', '--': 'Decrement Operator'}
operator_keys = operators.keys()

comments = {r'//': 'Single Line Comment', r'/*': 'Multiline Comment Start',
            r'*/': 'Multiline Comment End', '/**/': 'Empty Multiline comment'}
comment_keys = comments.keys()

header = {'.h': 'header file'}
header_keys = header.keys()

sp_header_files = {'<stdio.h>': 'Standard Input Output Header',
                   '<string.h>': 'String Manipulation Library'}

macros = {r'#\w+': 'macro'}
macros_keys = macros.keys()

datatype = {'int': 'Integer', 'float': 'Floating Point',
            'char': 'Character', 'long': 'long int'}
datatype_keys = datatype.keys()

keyword = {'return': 'keyword that returns a value from a block'}
keyword_keys = keyword.keys()

delimiter = {';': 'terminator symbol semicolon (;)'}
delimiter_keys = delimiter.keys()

blocks = {'{': 'Blocked Statement Body Open',
          '}': 'Blocked Statement Body Closed'}
block_keys = blocks.keys()

builtin_functions = {'printf': 'printf prints its argument on the console',
                     'scanf': 'scanf takes in the input from the user through console'}

punctuations = {'_', '`', '~', '!', '@', '#', '$', '&', '(', ')', '|', '"', "'" ,':', ';', '{', '}', '[', ']', '<', '>', '?', '/'}

numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Flags
dataFlag = False


i = f.read()

count = 0
program = i.split('\n')

for line in program:
    count = count+1
    tokens = line.split(' ')
    print("Tokens are", tokens)
    for token in tokens:
        if '\r' in token:
            position = token.find('\r')
            token = token[:position]
        if token in block_keys:
            print(blocks[token])
        if token in operator_keys:
            print("Operator is: ", operators[token])
        if token in comment_keys:
            print("Comment Type: ", comments[token])
        if token in macros_keys:
            print("Macro is: ", macros[token])
        if '.h' in token:
            print("Header File is: ", token, sp_header_files[token])
        if '()' in token:
            print("Function named", token)
        if dataFlag == True and (token not in non_identifiers) and ('()' not in token):
            print("Identifier: ", token)
        if token in datatype_keys:
            print("type is: ", datatype[token])
            dataFlag = True

        if token in keyword_keys:
            print(keyword[token])

        if token in delimiter:
            print("Delimiter", delimiter[token])
        if '#' in token:
            match = re.search(r'#\w+', token)
            print("Header", match.group())
        if token in numerals:
            print(token, type(int(token)))
        else:
            pass
    dataFlag = False

    print("________________________")


f.close()
