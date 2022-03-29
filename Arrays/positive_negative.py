"""
Given an integer array A.
Find the number of positive and negative integers in it an return them in an array.
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # make an arr to store pos and neg count
        ans = [0,0]
        for num in A:
            # Check for pos/neg num and inc count
            if num < 0:
                ans[1] += 1
            elif num > 0:
                ans[0] += 1

        return ans
