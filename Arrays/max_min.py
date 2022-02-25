"""
Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        mn = A[0]
        mx = A[-1]
        sm = mn + mx
        return sm
