"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Given s = "Hello World",


return 5 as length("World") = 5.

Please make sure you try to solve this problem without using library functions.
"""

class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLastWord(self, A):
		
		i = 0
		lenght = 0

        # Since we are not allowed to use library functions, here's me finding its lenght
		try:
			while A[i]:
				lenght += 1
				i += 1
		except:
			pass

		ans_len = 0
		word_started = False

		for i in range(lenght-1, -1, -1):
			if A[i] == " " and word_started:
				return ans_len
			elif A[i] != " ":
				ans_len += 1
				word_started = True

		return ans_len
