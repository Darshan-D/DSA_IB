"""
You are given an integer N and the task is to reverse the digits of the given integer. Return 0 if the result overflows and does not fit in a 32 bit signed integer
"""

class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        neg = False
        
        if A < 0:
            neg = True
            A = str(A)
            A = A[1:]
            A = A[::-1]
        
        else:
            A = str(A)
            A = A[::-1]
        
        A = int(A)
        
        if A > 2147483647:
            return 0

        if neg:
            return A*-1
        
        return A
