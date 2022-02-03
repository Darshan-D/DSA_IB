"""
Given a binary tree, return the preorder traversal of its nodes’ values.
Using recursion is not allowed.
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def preorderTraversal(self, A):
        # Will store the preorderTraversal
        res = []

        # Stack to keep track of parents
        stack = [A]
        
        while len(stack) > 0:
            root = stack.pop()

            # If root is not None
            if root:
                # Since its preoder we append the root value first
                res.append(root.val)

                # Since we are using stack, last one will be removed first,
                # and after root we need left child so we will insert it
                # after the right child
                stack.append(root.right)
                stack.append(root.left)

        return res