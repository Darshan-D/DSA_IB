"""
Given an array A containing N integers.

You need to find the maximum sum of triplet ( Ai + Aj + Ak ) such that 0 <= i < j < k < N and Ai < Aj < Ak.

If no such triplet exist return 0.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Sort the array
        A.sort()

        # Max prefix array
        max_left = [A[0]]

        # Max suffix array
        max_right = [A[-1]]
        
        mx = float("-inf")
        n = len(A)
        
        # Populate max prefix array
        for i in range(1, n):
            if A[i] > max_left[-1]:
                max_left.append(A[i])
            else:
                max_left.append(max_left[-1])

        # Populate max suffix array
        for i in range(n-2,-1,-1):
            if A[i] > max_right[0]:
                max_right.insert(0, A[i])
            else:
                max_right.insert(0, max_right[-1])
        
        # Iterate the array, current element will be our second element
        # we will get first element from prefix array and third element
        # from suffix array
        for i in range(1, n-1):
            a = max_left[i-1]   # First element
            b = A[i]            # Second element
            c = max_right[i+1]  # Third element

            if a+b+c > mx:
                
                if a<b<c:
                    mx = a+b+c

        return mx