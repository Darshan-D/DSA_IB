"""
Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.

Also given an integer C which represents knapsack capacity.

Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.

NOTE:

You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
"""
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer

    # Tabulation (Bottom Up Approach)
    def solve(self, A, B, C):
        n = len(A)

        # Initialize the table, initialization value is same 
        # as base condition in recursive solution
        dp = [[0]*(C+1) for i in range(n+1)]
        
        # Start iterating from idx 1, as idx 0 contains base condition
        for i in range(1, n+1):
            for j in range(1, C+1):
                
                # If current item weight is less than the space available in the knapsack
                if B[i-1] <= j:
                    # Use the previous answer, just update the weight, by adding weight of curr item
                    dp[i][j] = dp[i-1][j-B[i-1]] + A[i-1]
                    
                # We need to know the maximum wt, hence check if taking curr item or not
                # taking curr item, which gives the highest wt, and update answer accordinglt
                dp[i][j] = max(dp[i][j], dp[i-1][j])
    
        # Return the bottom right most cell value, as that gives the answer
        return dp[n][C]
