#!/usr/bin/env python2

def isAnagramOfPalindrome(S):
    """
    >>> isAnagramOfPalindrome('')
    False
    >>> any(isAnagramOfPalindrome(n*'a') for n in range(1, 10)) # all already ordered as only palindrome
    False
    >>> any(isAnagramOfPalindrome(n*'a' + 'b' + n*'a') for n in range(1, 10)) # all already ordered as only palindrome
    False
    >>> isAnagramOfPalindrome('ab')
    False
    >>> isAnagramOfPalindrome('aab')
    True
    >>> isAnagramOfPalindrome('aba') # already ordered as only palindrome
    False
    >>> isAnagramOfPalindrome('abab')
    True
    >>> isAnagramOfPalindrome('abba') # has one other palindrome
    True
    >>> isAnagramOfPalindrome('abcba') # has one other palindrome
    True
    >>> isAnagramOfPalindrome('aabc')
    False
    >>> isAnagramOfPalindrome('aaabb')
    True
    >>> isAnagramOfPalindrome('aaabc')
    False
    >>> isAnagramOfPalindrome('aaaabb')
    True
    >>> isAnagramOfPalindrome('aaaabbc')
    True
    >>> isAnagramOfPalindrome('tangent')
    False
    >>> isAnagramOfPalindrome('nolemonnomelon') # already palindrome but others possible
    True
    """
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
            return False
    else:
        # Not sure what I was thinking - odd count should only be *ONE* rather than
        # odd :S 
        if evens.count(False) != 1:
            return False
    # We've got what we need to build a palindrome
    return True

if __name__=='__main__':
    import sys
    if sys.argv[1:] and sys.argv[1] == 'test':
        import doctest
        doctest.testmod()
    else:
        print isAnagramOfPalindrome("dooernedeevrvn")

