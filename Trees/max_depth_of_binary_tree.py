"""
Given a binary tree, find its maximum depth.

The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.
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
	def maxDepth(self, A):
        # If we hav reached a root node, the lvl will be 0
        if not A:
            return 0

        # Recurisvely call for left and right subtree, take the max of them and add 1
        return 1 + max(self.maxDepth(A.left), self.maxDepth(A.right))
        