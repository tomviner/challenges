#!/usr/bin/env/python2

def is_prime(x):
    if x % 2 == 0:
        return False
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True

if __name__=='__main__':
    pass

