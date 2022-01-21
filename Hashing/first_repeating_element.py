"""
Given an integer array A of size N, find the first repeating element in it.

We need to find the element that occurs more than once and whose index of first occurrence is smallest.

If there is no repeating element, return -1.
"""

class Solution:
    # @param A : list of integers
    # @return an integer

    def solve(self, A):
        freq = {}
        ans = -1
        ans_idx = float("inf")

        for i,num in enumerate(A):
            if num in freq:
                # Since we need to find the smallest idx
                # of the repeating number, hence do all this
                idx = freq[num][1]
                if idx<ans_idx:
                    ans = num
                    ans_idx = idx

            else:
                # Storing the index as well, since we need to
                # find the first repeated number as per the index
                freq[num] = (1, i)


        return ans