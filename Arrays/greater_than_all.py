"""
Given an integer array A.
Find the count of elements whose value is greater than all of its previous elements.

Note: Since there are no elements before first element so it should be considered in our answer.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mx = A[0]
        c = 1
        n = len(A)

        for i in range(1, n):
            num = A[i]

            # If the current number is the greatest we have
            # seen till now, then increase the count
            # and update the max variable
            if num > mx:
                mx = num
                c += 1

        return c
