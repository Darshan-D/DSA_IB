"""
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        # Since the numbers will be in the range from 1 to size of len(A) - 1
        temp = [0]*len(A)

        for i in A:
            # If the val at that idx is already 1, then that num is repeated
            if temp[i-1]:
                return i
              
            # If the value is not repeated, then change value at that idx to 1
            else:
                temp[i-1] = 1

        # If no duplicates found return -1
        return -1
