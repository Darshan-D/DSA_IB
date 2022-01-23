"""
Given an 1D integer array A containing N distinct integers.

Find the number of unique pairs of integers in the array whose XOR is equal to B.
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        c = 0
        a = set(A)

        for i in a:
            find_num = i^B
            
            if find_num in a:
                c += 1

        # Dividing by 2 since we need no. of pairs
        return int(c/2)