"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        A = list(A)
        
        if len(A) <= 1:
            return 0
            
        # Sort the elemets
        A.sort()
        N = len(A)
        max_diff = A[1] - A[0]
        
        # Find the max distance in sorted form
        for i in range(1, N):
            diff = A[i] - A[i-1]
            if diff > max_diff:
                max_diff = diff

        return max_diff
