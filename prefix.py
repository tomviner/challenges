#!/usr/bin/env python2

from collections import defaultdict

def ps(A):
    flags = defaultdict(bool)
    [flags[x] for x in set(A)]
    for p, a in enumerate(A):
        flags[a] = True
        if all(flags.values()):
            return p
    return 0

if __name__=='__main__':
    print ps([2, 2, 1, 0, 1])

""" Score: 92.3

Detected time complexity:
O(N*log(N)) or O(N) or O(N**3)

Failed on 

random_n_10000 
random test 10 000 elements and values. 1.276 s.    TIMEOUT ERROR 
running time: >1.28 sec., time limit: 1.10 sec.

"""