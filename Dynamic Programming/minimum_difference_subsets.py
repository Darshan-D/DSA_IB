"""
Given an integer array A containing N integers.

You need to divide the array A into two subsets S1 and S2 such that the absolute difference between their sums is minimum.

Find and return this minimum possible absolute difference.

NOTE:

Subsets can contain elements from A in any order (not necessary to be contiguous).
Each element of A should belong to any one subset S1 or S2, not both.
It may be possible that one subset remains empty.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        B=sum(A)
        n=len(A)
        
        # Initialize the mat
        dp = [[False for x in range(B+1)] for y in range(n+1)]
        
        for i in range(n+1):
            for j in range(B+1):
                if(i==0):
                    dp[i][j]=False
                if(j==0):
                    dp[i][j]=True
                    
                # Check if its possible to get curr sum with curr elements
                elif(A[i-1]<=j):
                    dp[i][j]=dp[i-1][j-A[i-1]]  or dp[i-1][j]
                    
                else:
                    dp[i][j]=dp[i-1][j]
        
        st=[]
        
        # Find all the possbile sums and append it to st
        for i in range(B//2+1):
            if(dp[n][i]==True):
                st.append(i)
        ans=1000000
        
        # since we need to minimize abs(S2-S1), we can rewrite the aim as minimize
        # abs(B[i]-S1-S1) i.e. abs(B[i]-2*S1) as, S2-S1 = B[i]
        for i in range(len(st)):
            ans=min(ans, (B-2*st[i]))
            
        return ans
