"""
Given a binary tree A consisting of N nodes, return a 2-D array denoting the vertical order traversal of A.

Go through the example and image for more details.

NOTE:

If 2 or more Tree Nodes shares the same vertical level then the one with earlier occurence in the level-order traversal of tree comes first in the output.
Row 1 of the output array will be the nodes on leftmost vertical line similarly last row of the output array will be the nodes on the rightmost vertical line.
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def verticalOrderTraversal(self, A):

		# O(nodes) time complexity
		# O(width) space complexity

		# Since we will do level order traversal we will need a queue
		# the queue will store a tuple, one value being the node,
		# other being the lvl of that node
		# since we need to get all which are at the same lvl together
        queue = [(A,0)]

		# mx_pos and mx_neg will give us the width of tree
		mx_pos = 0
		mx_neg = 0

		# This map will store all the lvls as key and their respective nodes as values
		hash_map = {}

		# Start lvl order traversal
		while len(queue) > 0:
			root, lvl = queue.pop(0)

			if root is not None:
				val = root.val

				# Add the current value to the hash_map
				if lvl not in hash_map:
					hash_map[lvl] = [val]
				else:
					hash_map[lvl].append(val)

				# Add its left and right child to the queue, along with their respective lvls
				queue.append((root.left, lvl-1))
				queue.append((root.right, lvl+1))

				# Update our mx_neg/mx_pos lvls
				mx_neg = min(mx_neg, lvl)
				mx_pos = max(mx_pos, lvl)


		res = []

		# Iterate through our dic from mx_neg to mx_pos
		# and append values to res
		for i in range(mx_neg, mx_pos+1):
			if i in hash_map:
				res.append(hash_map[i])
		
		return res