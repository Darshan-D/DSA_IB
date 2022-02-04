"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree.
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, A, B):
        # If either of the array becomes empty
        # we have reached the lead node
		if len(A) < 1 or len(B) < 1:
			return None

        # The first value pointed by the preorder will be the root of the tree
		root = TreeNode(A[0])

        # Find this root within inorder traversal 
        # (this can be speed up by using a hash map, with element value as key and its index as value of the map)
		mid = B.index(A[0])

        # All the elements to the left of root within inorder will goto left subtree
        root.left = self.buildTree(A[1:mid+1], B[:mid])

        # All the elements to the right of root within inorder will goto right subtree
		root.right = self.buildTree(A[mid+1:], B[mid+1:])

		return root
