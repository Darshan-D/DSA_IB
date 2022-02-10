"""
You are given K sorted integer arrays in a form of 2D integer matrix A of size K X N.

You need to merge them into a single array and return it.
"""
import heapq

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        heap = []
        k = len(A)
        n = len(A[0])
        res = []

        # Add all the elements into the heap
        for i in range(k):
            for j in range(n):
                heapq.heappush(heap, A[i][j])

        # Remove all the elements from the heap, this will give us
        # elements in increasing order
        for i in range(k):
            for j in range(n):
                res.append(heapq.heappop(heap))
        
        return res
