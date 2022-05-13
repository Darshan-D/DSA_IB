"""
Given the array of strings A, you need to find the longest string S which is the prefix of ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

For Example: longest common prefix of "abcdefgh" and "abcefgh" is "abc".
"""

class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
        ans = ""
        i = 0
        min_len = float("inf")
        for word in A:
            if len(word) < min_len:
                min_len = len(word)
                template = word

        count = 0
        n = len(A)
        while i < min_len:
            curr = template[i]
            count = 0
            for word in A:
                if word[i] == curr:
                    count += 1

            if count == n:
                ans += curr

            else:
                return ans

            i+=1

        return ans
