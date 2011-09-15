#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from math import factorial
from itertools import izip

def space_crews(T, D):

    countries = izip(T, D)
    factorials = dict()

    def nCr(n, r):
        def _f(f):
            return factorials.setdefault(f, factorial(f))
        nfac = _f(n)
        return nfac / (_f(r) * _f(n-r))

    country_ways = (nCr(t, d) for t, d in countries)
    total_ways = reduce(lambda x, y: x*y, country_ways)
    
    if total_ways > 1410000016:
        total_ways %= 1410000017

    return total_ways

    
if __name__=='__main__':
    space_crews([6, 4, 7], [1, 3, 4])
    
"""
N countries (numbered from 0 to N−1) participate in a space mission. Each country has trained a certain number of astronauts and each country has to delegate a certain number of astronauts to the mission's crew. How many different ways are there to select the crew?

For example, suppose there are three countries A-land, B-land and C-land and

A-land has 6 astronauts;
B-land has 4 astronauts;
C-land has 7 astronauts.
and

A-land has to delegate 1 astronaut;
B-land has to delegate 3 astronauts;
C-land has to delegate 4 astronauts.
Then

there are 6 different ways in which A-land can delegate 1 out of 6 astronauts;
there are 4 different ways in which B-land can delegate 3 out of 4 astronauts;
there are 35 different ways in which C-land can delegate 4 out of 7 astronauts.
Each country's choice is independent, so the total number of different ways to build the mission crew is 6*4*35=840.

Write a function

def space_crews(T,D)

that, given two non-empty zero-indexed arrays T and D consisting of N integers each, returns the number of different ways in which the space crew can be selected, where:

T[K] = number of astronauts in country K;
D[K] = number of astronauts to be delegated from country K.
Assume that:

N is an integer within the range [1..1,000];
each element of array T is an integer within the range [0..1,000,000];
each element of array D is an integer within the range [0..1,000,000];
T[i] ≥ D[i] for i=0..(N−1).
For example, given N=3 and

T[0] = 6  T[1] = 4  T[2] = 7
D[0] = 1  D[1] = 3  D[2] = 4
the function should return 840, as explained above. If the result exceeds 1,410,000,016, the function should return the remainder of the result modulo 1,410,000,017.

Complexity:

expected worst-case time complexity is O(max(T)*log(max(T))+N);
expected worst-case space complexity is O(N+max(T)), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""

