"""
Given a matrix of integers A of size N x M in which each row is sorted.

Find an return the overall median of the matrix A.
"""
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def findMedian(self, A):
		arr = []
		for i in range(len(A)):
			for j in range(len(A[0])):
				arr.append(A[i][j])


		arr.sort()
		med_idx = len(arr)//2
		return arr[med_idx]
