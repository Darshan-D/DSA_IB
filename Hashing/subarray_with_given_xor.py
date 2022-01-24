"""
Given an array of integers A and an integer B.

Find the total number of subarrays having bitwise XOR of all elements equals to B.
"""

# O(N) time & space complexity
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        running_xor = 0
        hash_map = {}
        count = 0

        for num in A:
            running_xor ^= num

            if B^running_xor in hash_map:
                count += hash_map[B^running_xor]

            if running_xor == B:
                count += 1

            if running_xor in hash_map:
                hash_map[running_xor] += 1
            else:
                hash_map[running_xor] = 1


        return count