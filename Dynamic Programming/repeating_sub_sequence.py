"""
Given a string A, find length of the longest repeating sub-sequence such that the two subsequence don’t have same string character at same position,

i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.

NOTE: Sub-sequence length should be greater than or equal to 2.
"""
# Basically LCS explained

# * Each LCS iteration in the loop is testing a sub sequence
# * Sub sequence at 0,0 is made by taking 2 full strings into consideration
# * max() condition is basically, if the two characters are not same, which one should i pick to keep the sum max
# similarly go for min() whereever min is required (not that sure about this point)

class Solution:
	# @param A : string
	# @return an integer
	def anytwo(self, A):
		# Retruns int
		# 0 - There is no repetition
		# 1 - There is repetition

		dp = [[0 for j in range (len(A) + 1)] for i in range (len(A) + 1)]

		for i in range(len(A) - 1, -1, -1):
			for j in range(len(A) - 1, -1, -1):

				# Handling the condition, "any i’th character in the two subsequences 
				# shouldn’t have the same index in the original string" by simply doing i!=j

				if A[i] == A[j] and i != j:
					dp[i][j] = 1 + dp[i+1][j+1]
				else:
					dp[i][j] = max(dp[i][j+1], dp[j][i+1])


		# To understand this refer the note before problem constrains
		if dp[0][0] < 2:
			return 0
		else:
			return 1
