"""
Given a string A, find the common palindromic sequence ( A sequence which does not need to be contiguous and is a pallindrome), which is common in itself.

You need to return the length of longest palindromic subsequence in A.

NOTE:

Your code will be run on multiple test cases (<=10). Try to come up with an optimised solution.

"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        m = len(A)
        
        # Make a 2D grid of size MxM
        dp = [[0 for i in range(m+1)] for j in range (m+1)]

        # Second string will be the reverse of given string
        # it will be used to compare with the original string
        # since we are looking for longest pallindrome we are 
        # reversing it
        B = A[::-1]
        
        # Iterate through the bottom right
        # End at top left
        for i in range(m-1, -1, -1):
            for j in range(m-1, -1, -1):

                # If there's a match of characters between 2 strings
                # then take the -ve diagonal value and increase by 1
                if A[i] == B[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]

                # Else take the max of our of right and bottom element
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        # Top left element will be our answer
        return dp[0][0]