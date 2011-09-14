#!/usr/bin/env python2
import sys

def problem_1():
    """
        If we list all the natural numbers below 10 that are multiples of 3 or 5, 
        we get 3, 5, 6 and 9. The sum of these multiples is 23.

        Find the sum of all the multiples of 3 or 5 below 1000
    """

    x = range(1000)
    items = [v for v in x if v % 5 == 0 or v % 3 == 0]
    print sum(items)

def problem_2():
    """
        Each new term in the Fibonacci sequence is generated by adding the 
        previous two terms. By starting with 1 and 2, the first 10 terms will be:

            1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

        By considering the terms in the Fibonacci sequence whose values do not 
        exceed four million, find the sum of the even-valued terms.
    """

    x0, x1 = 1, 1

    even_sum = 0
    while(x0<4000000):
        if (x0 % 2 == 0):
            even_sum += x0
        x0, x1 = x1, x0 + x1

    print even_sum

if __name__=='__main__':
    try:
        number = sys.argv[1]
    except IndexError:
        number = 1

    try:
        locals()['problem_%s' % number]()
    except KeyError:
        sys.exit("I've not done that yet!")