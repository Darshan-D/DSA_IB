"""
actual ip format: "AB"
actual op format: 28
"""

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        
        res = 0
        for i in range(len(A)):
            res+= (ord(A[i])-64)*(26**(len(A)-i-1))
        return res
