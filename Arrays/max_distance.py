"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].
"""
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        A = list(A)
        for i in range(n):
            A[i] = (A[i],  i)

        A.sort()

        mx_dist = float('-infinity')
        mx_idx = float('-infinity')

        # there is repeating pattern
        for i in range(n-1, -1, -1):

            # Left side se jo bhi max abb tak aaya h uska dhyaan rakh rahe h
            mx_idx = max(mx_idx, A[i][1])

            # Ab tak ka jo bhi max mx_dist hoga uska dhyaan yaha pe rakh rahe h
            # mx_dist is abb tak ka mx_idx - current val
            mx_dist = max(mx_dist, mx_idx-A[i][1])

        return mx_dist

            
