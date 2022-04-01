"""
Given an integer array A, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        zeros = 0
        for num in A:
            if num == 0:
                zeros += 1

        i = 0
        while i < len(A):
            if A[i] == 0:
                del A[i]
                continue
            i+=1

        A = A + [0]*zeros

        return A
