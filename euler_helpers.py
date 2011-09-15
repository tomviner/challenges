#!/usr/bin/env/python2
import math
from collections import defaultdict

def is_prime(x):
    """ 
        Niavely checks if a given 'x' is prime 
    """
    if x % 2 == 0:
        return False
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True


def sieve(x):
    """ 
        Generates a list of primes up to 'x' via sieve technique. Could
        be better but works ok.
        
            In [113]: time sieve(10000);
            CPU times: user 1.42 s, sys: 0.00 s, total: 1.43 s
    """

    sieve = range(3, x, 2)
    primes = dict()

    p = 2
    while p < x:
        for cnt, n in enumerate(sieve[::p]):
            if cnt == 0:
                primes[p] = True
            print p, n, primes
        p += 1
   

    return primes
    
if __name__=='__main__':
    pass

