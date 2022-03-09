"""
Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

class Solution:

    # @param A : string

    # @param B : string

    # @return an integer

    def minDistance(self, A, B):

        A = list(A)
        B = list(B)
        m = len(A)
        n = len(B)

        # Cache to store the answers, 2D list for tabular approach
        dp = [[0]*(n+1) for i in range(m+1)]

        # Populate the extra cells to handle the base cases
        for i in range(m+1):
            dp[i][0] = i
            
        for j in range(n+1):
            dp[0][j] = j
            
        # Iterate through both the lists
        for i in range(m):
            for j in range(n):
                # We have 3 choices at each iteration

                # 1. swap/identical last char
                a = dp[i][j] + (0 if A[i] == B[j] else 1) 
                
                # 2. remove last char
                b = dp[i][j+1]+1 
                
                # 3. add last char
                c = dp[i+1][j]+1
                
                # Choose the one with the minimum cost
                dp[i+1][j+1] = min(a,b,c)

        return dp[m][n]
