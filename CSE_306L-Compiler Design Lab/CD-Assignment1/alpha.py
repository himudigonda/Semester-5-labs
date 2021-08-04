#! /usr/bin/python
#! @author: @ruhend (Mudigonda Himansh)
#! date : 2 august 2021
#! Reg no: AP19110010169
#! Section: CSE-D
#! https://ruhend.github.io/links

import pandas as pnda
# nfa_file = open(r"input.txt")
nfa = {
    'A': {'a': ['A', 'B'], 
          'b': ['A']}, 
    'B': {'a': ['C'], 
          'b': ['C']}, 
    'C': {'a': ['D'], 
          'b': ['D']}, 
    'D': {'a': [], 
          'b': []}
}

class nfadfa:
    def init(self):
        t = 2 # since we have a 2 way transition by default
        keys = list(list(nfa.keys())[0])
        weights = list(nfa[keys[0]].keys())
        return nfa, t, keys, weights

        
    def make_dfa(self,nfa, keys, weights, t):
        dfa = {}
        new_states = []
        dfa[keys[0]] = {}
        for y in range(t):
            var = "".join(nfa[keys[0]][weights[y]])
            dfa[keys[0]][weights[y]] = var
            if var not in keys:
                new_states.append(var)
                keys.append(var)

        while len(new_states) != 0:
            dfa[new_states[0]] = {}
            for _ in range(len(new_states[0])):
                for i in range(len(weights)):
                    temp = []
                    for j in range(len(new_states[0])):
                        temp += nfa[new_states[0][j]][weights[i]]
                    s = ""
                    s = s.join(temp)
                    if s not in keys:
                        new_states.append(s)
                        keys.append(s)
                    dfa[new_states[0]][weights[i]] = s

            new_states.remove(new_states[0])
        return dfa

    def conclude(self,dfa, nfa_fstates):
        print("DFA : ")
        print(dfa)
        print("DFA transition table : ")
        dfa_table = pnda.DataFrame(dfa)
        print(dfa_table.transpose())

        dfa_states_list = list(dfa.keys())

        dfa_fstates = []
        for x in dfa_states_list:
            for i in x:
                if i in nfa_fstates:
                    dfa_fstates.append(x)
                    break

        print("DFA Final states : ", dfa_fstates)


    def main(self):
        nfa, t, keys, weights = nfadfa.init(self)
        nfa_fstates = ['D']
        print("NFA : ")
        print(nfa)
        print("NFA transition table : ")
        nfa_table = pnda.DataFrame(nfa)
        print(nfa_table.transpose())
        dfa = nfadfa.make_dfa(self,nfa, keys, weights, t)
        nfadfa.conclude(self,dfa, nfa_fstates)

if __name__=='__main__':
    nfadfahandler = nfadfa()
    nfadfa.main(nfadfahandler)