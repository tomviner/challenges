#!/usr/bin/env python2

def isAnagramOfPalindrome(S):
    # An palindrome is basically a string mirrored and stuck back onto
    # itself, so for each character on one side there should be another
    # corresponding to it on the other. hence all counts should be even
    # UNLESS! the string is an odd length - in which case we could fit in
    # a single character as a pivot point. check for these conditions and
    # we'll know if we have a palindrome.

    evens = [S.count(x) % 2 == 0 for x in set(S)]
    if len(S)%2 == 0:
        # Our string is even so counts of all characters should be mod2
        if not all(evens):
            return 0
    else:
        # Our string is odd lenth so we should have one "spare" odd character
        # since false respresents an odd count it should have remainder 1 when
        # mod2'd
        if evens.count(False) % 2 != 1:
            return 0
    # We've got what we need to build a palindrome
    return 1

if __name__=='__main__':
    isAnagramOfPalindrome("dooernedeevrvn")

