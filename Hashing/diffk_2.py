"""
Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Example :

Input :

A : [1 5 3]
k : 2
Output :

1
as 3 - 1 = 2
"""

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
		
        # Similar approach as 2_Sum

		hash_set = set()

        for i in A:
            if i-B in hash_set or i+B in hash_set:
                return 1
            else:
                hash_set.add(i)
        
        return 0