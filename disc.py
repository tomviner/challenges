#!/usr/bin/env python2
from itertools import combinations

def number_of_disc_intersections(A):
    boundries = list()

    for x, r in enumerate(A):
        boundries.append((x-r, x+r))
    
    r = range(len(A))
    pairs = combinations(r, 2)

    def overlap(k, j):
        k, j = boundries[k], boundries[j]
        if (k[1]>=j[0]):
            return 1
        else:
            return 0

    counts = list()

    for pair in pairs:
        counts.append(overlap(*pair))
    
    return sum(counts)

    
if __name__=='__main__':
    cnt = number_of_disc_intersections(range(2000))
    print "Count is %d" % cnt
    