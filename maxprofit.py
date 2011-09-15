#!/usr/bin/env python2

def maxProfit(A):
    
    while(len(A)>1):
        max_price, min_price = max(A), min(A)
        max_index, min_index = A.index(max_price), A.index(min_price)
        if max_index > min_index:
            return max_price - min_price
        A.pop(max_index)

    return 0

if __name__=='__main__':
    print maxProfit([23171, 21011, 21123, 21366, 21013, 21367])

