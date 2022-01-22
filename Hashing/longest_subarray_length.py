"""
Problem Description

Given an integer array A of size N containing 0's and 1's only. 

You need to find the length of the longest subarray having count of 1’s one more than count of 0’s.

Example Input
Input 1:

 A = [0, 1, 1, 0, 0, 1]


Example Output
Output 1:

 5

Example Explanation
Explanation 1:

 Subarray of length 5, index 1 to 5 i.e 1, 1, 0, 0, 1. Count of 1 = 3, Count of 0 = 2.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        # We will store the sum as key value pair
        # key: sum upto that index | value: index
        hash_map = {}

        # Prefix sum
        sm = 0

        # required ans
        max_len = 0

        # Since we need, count of 1s one more than count of 0s
        # if we add 1 on encountering '1' and sub 1 on encountering '0'
        # we will get sum as 1 where count of 1s is one more than count of 0s
        for i in range(len(A)):
            if A[i] == 0:
                sm -= 1
            else:
                sm += 1

            # We found one of the answeres
            # here i + 1 is done since i is 0 based
            # and wont give exact length
            if sm == 1:
                max_len = i + 1

            # Also add the current sm to hash_map
            if sm not in hash_map:
                hash_map[sm] = i

            # If sum-1 is present in the hash_map, it means that
            # after that (hash_map[sum-1]) element we have only added one more '1'
            # untill the current element (basically the count of '1' is one more then it was at the value found at hash_map[sum-1])
            if sm-1 in hash_map:

                # Check if that sub arr len is greater than curr ans
                if i - hash_map[sm-1] > max_len:
                    max_len = i - hash_map[sm-1]

        return max_len