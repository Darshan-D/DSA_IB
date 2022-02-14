"""
Given two strings A and B. Find the longest common sequence ( A sequence which does not need to be contiguous), which is common in both the strings.

You need to return the length of such longest common subsequence.
"""
class Solution:
    def lcs(self, X , Y):

        # find the length of the strings
        m = len(X)
        n = len(Y)

        # Make a 2D array with dimensions (m+1)x(n+1)
        dp = [[0 for j in range (n+1)] for i in range (m+1)]

        # Iterate through the array (tabulation approach)
        # Start from the bottom right cell of the 2D array
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # If ith character of X and jth character of Y are same
                # then take the diagonal value and add 1 
                if X[i] == Y[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]

                # Else take the max of right cell or bottom cell
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        # Return the value of first cell, since we started from bottom right,
        # top left will contain desired answer
        return dp[0][0]


    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        r_len = self.lcs(A, B)
        return r_len