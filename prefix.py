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
