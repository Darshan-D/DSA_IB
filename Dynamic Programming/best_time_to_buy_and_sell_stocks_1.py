"""
Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Return the maximum possible profit.
"""

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):
        n = len(A)
        if n < 2:
            return 0

        # Make a suffix array, denoting the max value present to the right of current array
        suff_arr = [0]*n
        suff_arr[-1] = A[-1]
        for i in range(n-2,-1,-1):
            suff_arr[i] = max(A[i], suff_arr[i+1])

        mx_profit = 0

        # Now just find the pair with maximum difference
        for i in range(n):
            mx_profit = max(mx_profit, suff_arr[i] - A[i])

        return mx_profit
