"""
Say you have an array, A, for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.

You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):
        n = len(A)
        profit = 0

        if n < 2:
            return 0
        
        # Stock Price on previous day
        pp = A[0]

        for i in range(1,n):
            cp = A[i]       # Current Price
            pp = A[i-1]     # Previous Price

            # If currently stock price is more than prev day
            # then assume that stock was purchased on prev day
            # and sell the stock today
            if cp > pp:
                profit += cp - pp

        return profit
