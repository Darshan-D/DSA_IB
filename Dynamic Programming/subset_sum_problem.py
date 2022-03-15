"""
Given an integer array A  of size N.

You are also given an integer B, you need to find whether their exist a subset in A whose sum equal B.

If there exist a subset then return 1 else return 0.
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # If thought of the recursive solution,
        # then we have two choices, whether to take a number or not
        # and with each decision value of B decreases
        # hence the size of array and value of B becomes two arguments which
        # change over time, so we make a 2d matrix denoting the same values
        # in rows and cols respectively
        dp = [[False for i in range(B+1)] for j in range(len(A))]

        # The base conditions, will be
        # 1. First column will be all True, since there will always be a subset (empty set)
        # which will give sum as 0
        # 2. First row, except for first cell, will be all False, since we can't make sum
        # greater than 0 from an empty array
        # Initialize the array as per base conditions
        for i in range(len(A)):
            for j in range(B+1):
                if j == 0:
                    dp[i][j] = True

        for i in range(1, len(A)):
            for j in range(1, B+1):
                # Check if current number is smaller than required target (B)
                if A[i-1] <= j:
                    # Either take the current element OR don't take the current element
                    # Here we are updating the value of B, using j - A[i-1]
                    # where j represents value of B and A[i-1] represents current A ele
                    dp[i][j] = (dp[i-1][j - A[i-1]]) or (dp[i-1][j])

                # If not, then don't take it i.e. take the previous answer
                else:
                    dp[i][j] = dp[i-1][j]

        # The answer will be stored in right bottom last cell
        # convert it to 1/0 based on True or False
        return 1 if dp[-1][-1] is True else 0 
