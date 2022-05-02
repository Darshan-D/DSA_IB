"""
Given an array of integers A of size N and an integer B.

College library has N bags,the ith book has A[i] number of pages.

You have to allocate books to B number of students so that maximum number of pages alloted to a student is minimum.

A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.

NOTE: Return -1 if a valid assignment is not possible.
"""

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def books(self, A, B):
		def feasible(A,B,mid):
            '''
            This will help us identigy if it is possbile to distribute each student
            a maximum of mid pages. If it is, it will return True

            If after distributing mid pages to all B students we have more pages left, then
            we need more students, in that case we will return False
            '''
			sm = 0
			student = 0
			for i in A:
				if sm + i > mid:
					sm = i
					student += 1
				else:
					sm += i

			return student<B

		# Edge Case
		if B > len(A):
			return -1

		mn = max(A)
		mx = sum(A)
		ans = -1
		while mn <= mx:
			# Mid represnets the mimaximum number of pages we want each student to read
            # We want to minimize mid, i.e minimize the maximum number of pages alloted by a student aka our question
			mid = (mn+mx)//2
			
			# If it is possbile to distribute mid number of pages to a total of B students,
            # then it is one of the possbile answer store it. And since we are minimizing Mid
            # we will move our search space to left, this will reduce the value of mid which is
            # what we want
			if feasible(A,B,mid):
				ans = mid
				mx = mid -1

			# If it is not possbile to distribute mid number of pages to a toatl of B students,
            # i.e we have less students and there are pages left even after distributing them among
            # B students, then we need to increase the number of pages read by each student
            # Thus we move our search space to right
			else:
				mn = mid + 1

		return ans
            
