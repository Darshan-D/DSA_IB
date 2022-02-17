"""
Given an integer array A of size N.

You can pick B elements from either left or right end of the array A to get maximum sum.

Find and return this maximum possible sum.

NOTE: Suppose B = 4 and array A contains 10 elements then

You can pick first four elements or can pick last four elements or can pick 1 from front and 3 from back etc . you need to return the maximum possible sum of elements you can pick.
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # Take the sum of first B elements
        Sum = Max = sum(A[:B])
        N = len(A)

        # Move the window of B elements which gave Sum by step size of 1
        for b in range(1, B+1):
            # Remove the first element from the window
            # and add a new element to the window
            Sum = Sum - A[B - b] + A[N - b]

            # If Sum becomes greater update the Max
            if Sum > Max:
                Max = Sum
                
        return Max