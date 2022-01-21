"""
For Given Number N find if its COLORFUL number or not

Return 0/1

COLORFUL number:

A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
"""

class Solution:
    # @param A : integer
    # @return an integer
    
    def colorful(self, A):
        # Make every possible combination and check if it already exists
        A = str(A)
        A = list(A)
        A = list(map(int, A))
        p = set()
        for i in range(len(A)):
            prod = 1
            for j in range(i, len(A)):
                prod *= A[j]
                if prod in p:
                    return 0
                p.add(prod)
        return 1