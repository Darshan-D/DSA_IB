"""
Problem Description

The count-and-say sequence is the sequence of integers beginning as follows: 
1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11. 11 is read off as two 1s or 21.
21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2, the sequence is 11.
"""

class Solution:
	# @param A : integer
	# @return a strings
	def countAndSay(self, A):
		def count(prev):
			# Base Case
			if len(prev) == 1:
				return "1"+prev

			# Store the first digit
			curr_temp = prev[0]
			count = 0
			ans = ""
			for i in range(len(prev)):
				# Count how many digits which are contiguous are same
				if prev[i] == curr_temp:
					count += 1

				# Update stuff when they stop being same
				else:
					ans += str(count) + curr_temp
					curr_temp = prev[i]
					count = 1

			# Remeber exit conditions correctly
			# what if even for the last iteration
			# we are within if statement and we did
			# not get the opportunoity to update the 
			# ans variable, so we write it outside as well
			ans += str(count) + curr_temp
			return ans


		# Base Conditions
		if A==0:
			return ""

		elif A==1:
			return 1

		# Initialize the prev variable for A=1
		# start solving from A=2
		prev = "1"
		i=2
		while i <= A:
			new_ans = count(prev)
			prev = new_ans
			i+=1

		return int(new_ans)
