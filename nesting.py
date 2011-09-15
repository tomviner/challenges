#!/usr/bin/env python2

def nesting(S):
    # First case, S is empty so valid
    if len(S)==0:
        return 1
        
    # Check if we start/end with an invalid char
    if S[0] == ')' or S[-1] == "(":
        return 0

    counter = 0

    for char in S:
        if char=='(':
            counter += 1
        if char==')':
            counter -= 1
            
        # If counter goes negative the cancelling has messed up
        # so we've an invalid nesting present somewhere
        if counter < 0:
            return 0

    if counter == 0:
        return 1

    return 0

if __name__=='__main__':
    nesting("(()(())())")

