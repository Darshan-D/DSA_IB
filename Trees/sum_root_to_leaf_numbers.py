"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers % 1003.
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def sumNumbers(self, A):
		# @param root: current node of the tree
		# @param curr_str: number made till now
		# @param running_sm: sum of paths till now
		# @returns running_sm: sum of paths till now
		def solve(root, curr_str, running_sm):

			# Update the curr_str with new node val
			curr_str += str(root.val)

			# If the node has left child then recursively call for it
			if root.left:
				running_sm = solve(root.left, curr_str[:], running_sm)
				
			# If the node has right child then recursively call for it
			if root.right:
				running_sm = solve(root.right, curr_str[:], running_sm)
				
			# If node has no childs then its a leaf node and we need to update our running_sm
			elif not root.left and not root.right:
				running_sm += int(curr_str)

			# return the running_sm
			return running_sm


		curr_str = ""
		running_sm = 0
		total = solve(A, curr_str, running_sm)
		return total%1003