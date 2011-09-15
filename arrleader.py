#!/usr/bin/env python2

def arrLeader(A):

    A.sort()
    
    last_digit = A[0]
    last_count = 0
    current_count = 0
    current_digit = A[0]
    
    for digit in A:
        if digit == current_digit:
            current_count += 1
        else:
            # If we've changed digit, check if we need
            # to update the highest figure...
            if current_count > last_count:
                last_count = current_count
                last_digit = current_digit

            current_digit = digit
            current_count = 1
           
    if last_count > len(A) / 2:
        return last_digit
    
    return -1

if __name__=='__main__':
    arrLeader([4, 2, 2, 3, 2, 4, 2, 2, 6, 4])

