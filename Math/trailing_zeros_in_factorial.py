"""
Given an integer A, return the number of trailing zeroes in A!.

Note: Your solution should be in logarithmic time complexity.
"""

class Solution:
	# @param A : integer
	# @return an integer
	def trailingZeroes(self, A):
        ans = 1
        i = 1
        count = 0
        
        while ans > 0:
            div = 5**i
            ans = A//div
            count += ans
            i += 1

        return count
