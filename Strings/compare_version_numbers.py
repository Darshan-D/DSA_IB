"""
Compare two version numbers version1 and version2.

If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
"""

class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def compareVersion(self, A, B):
		# Break the strings into lists, with "." as the seperator
		A_num = A.split(".")
		B_num = B.split(".")
		
		# Conveert them to int
		A_num = [int(i) for i in A_num]
		B_num = [int(i) for i in B_num]

		# To know which one was bigger and smaller
		# Check the full code to know its significance
		# Using dict for this might be an overkill, a varibale could do the job too ig
		hash_map = {}

		# Store which among them is bigger in size
		if len(A_num) < len(B_num):
			smaller = A_num
			bigger = B_num
			hash_map["small"] = "A"
			hash_map["big"] = "B"
		else:
			smaller = B_num
			bigger = A_num
			hash_map["small"] = "B"
			hash_map["big"] = "A"

		# Make size of smaller one equal to bigger one
		# By appending 0s to the smaller one
		diff = len(bigger) - len(smaller)

		for i in range(diff):
			smaller.append(0)

		# Now just compare the number between two lists
		# i.e. Compare the number between the dots
		max_comparisons = len(bigger)
		i=0

		while i < max_comparisons:
			# If the bigger[i] > smaller[i] then we need to know, which
			# string does the bigger represnt is it A or B
			# that's why we used a dict
			if bigger[i] > smaller[i]:
				val = hash_map["big"]
				if val == "A":
					return 1
				else:
					return -1

			# Same explanation as above
			elif smaller[i] > bigger[i]:
				val = hash_map["small"]
				if val == "A":
					return 1
				else:
					return -1

			# If the current elements are equal we cannot 
			# judge the entirity of ver num from this
			# so we cannot return anything here yet
			# we have to goto the next iteration
			elif bigger[i] == smaller[i]:
				ans = 0

			i+=1
		
		# If the code still has not returned anything
		# after coming out of the while loop than it 
		# means that both the versions are the Same
		# hence return 0
		return ans
