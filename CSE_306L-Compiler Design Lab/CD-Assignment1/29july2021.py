
#! /usr/bin/python3.9
#! @author: @ruhend
# ? Date Created : #1

# establish imports here

# global variables here

###### info #########
#! blank is no transition
#! null means epsilon transition

def convertnfa2dfa(_nfa_matrix):
    dfa_matrix = []
    # CODE HERE
    # 1->2->3->4->5
    #
    return dfa_matrix


def get_inputs():
    sizeofmatrix = 5
    nfa_matrix = [
        [' ', '+', '-', 'T', "t"],
        [' ', 'D', '/', '+', '-'],
        ['+', '=', 'm', '-', '-'],
        ['-', '-', '+', 'w', '-'],
        ['+', '+', '=', '',  ' ']
    ]
    #xxxxx input=>           '+-=m+'
    # transition=>      1->2->5->3->3->1
    # start state=>     1
    # 
    # while loop->      equivalence
    
    ###### JOIN WHATS APP CALL ASAP #######
    dfa_matrix = convertnfa2dfa(nfa_matrix)
    print(nfa_matrix)

# define main function


def main():
    get_inputs()


main()
