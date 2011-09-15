#!/usr/bin/env python2

def amplitude(A):
    diff = 0
    for i, x in enumerate(A):
        try:
            current_diff = A[i+1]-A[i]
            if current_diff > diff:
                diff = current_diff
        except IndexError:
            pass
    
    return diff


if __name__=='__main__':
    print amplitude(range(10000000))

