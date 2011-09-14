#!/usr/bin/env python2

from collections import defaultdict

def equi(A):
    sums = defaultdict(int)
    s = 0
    for x, a in enumerate(A):
        s += a
        sums[x] = s
    
    sums_r = defaultdict(int)
    s_r = 0
    for x, a in enumerate(A):
        sums_r[x] = s - sums[x] + a
        if sums_r[x] == sums[x]:
            return x
    return -1
            

if __name__=="__main__":
    print equi([-7, 1, 5, 2, -4, 3, 0])

""" Result: 100! :D """