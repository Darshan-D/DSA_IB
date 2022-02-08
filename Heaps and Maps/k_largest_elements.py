"""
Given an 1D integer array A of size N you have to find and return the B largest elements of the array A.

NOTE:

Return the largest B elements in any order you like.
"""


import heapq as hp 

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
        
    def solve(self, A, B):

        # Build the min heap
        hp.heapify(A)
        
        # Remove the N-B smallest element
        # this will give B largest elements
        for i in range(len(A)-B):
            hp.heappop(A)
            
        return A