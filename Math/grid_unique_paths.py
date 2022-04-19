"""
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?



Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
              OR  : (0, 0) -> (1, 0) -> (1, 1)
"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        # Create a 2D table to store
        # results of subproblems
        p, q = A, B
        # Create a 1D array to store
        # results of subproblems
        dp = [1 for i in range(q)]
        for i in range(p - 1):
            for j in range(1, q):
                dp[j] += dp[j - 1]
        return dp[q - 1]
