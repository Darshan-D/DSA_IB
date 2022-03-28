"""
Given two sequences A, B, count number of unique ways in sequence A, to form a subsequence that is identical to the sequence B.

Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of 
the characters without disturbing the relative positions of the remaining characters. (ie, “ACE” is a subsequence of “ABCDE” while “AEC” is not).
"""

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        s = A
        t = B
        n=len(s)
        m=len(t)
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1,n+1):
            dp[0][i]=1
        
        for i in range(1,m+1):
            for j in range(i,n+1):
                if i==1and j==1:
                    if t[i-1]==s[j-1]:
                        dp[i][j]=1
                else:
                    if t[i-1]==s[j-1]:
                        dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
                    else:
                        dp[i][j]=dp[i][j-1]
        return dp[m][n]
