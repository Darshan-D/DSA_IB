"""
You are given a 1D integer array B containing A integers.

Count the number of ways to split all the elements of the array into 3 contiguous parts so that the sum of elements in each part is the same.

Such that : sum(B[1],..B[i]) = sum(B[i+1],...B[j]) = sum(B[j+1],...B[n]) 
"""

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        # sum up all the numbers in the arr
        total = sum(B)

        # Check if they are divisible by 3 (since we want to divide it in 3 parts)
        if total % 3 == 0:
            # Each part should sum upto this target
            target = total // 3

        # If they cant be split then return 0
        else:
            return 0
            
        ans = 0
        f = 0
        s = 0
        for i in range(A - 1):
            # Take the running sum
            s += B[i]

            # If sm is equals to twice the target, we found one set of partition
            if s == 2 * target:
                ans += f

            # If sm is equal to the target, we found one part of partition
            if s == target:
                f += 1

        return ans
