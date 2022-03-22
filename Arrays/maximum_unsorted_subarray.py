"""
You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.

Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.

If A is already sorted, output -1.
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        B = [i for i in A]
        n = len(A)
        A.sort()
        start = -1
        end = -1
        end_fixed = 0
        
        for i in range(len(A)):
            if end_fixed and A[i]!= B[i]:
                end_fixed = 0
            if start == -1:
                if A[i] != B[i]:
                    start = i
            elif not end_fixed:
                if A[i] == B[i]:
                    end = i-1
                    end_fixed = 1
                    
        if start == -1:
            return [-1]
        if end == -1 or end_fixed == 0:
            end = n-1
        return [start , end]
