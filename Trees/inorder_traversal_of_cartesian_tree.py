"""
Given an inorder traversal of a cartesian tree, construct the tree.

Cartesian tree :  is a heap ordered binary tree, where the root is greater than all the elements in the subtree.

Note: You may assume that duplicates do not exist in the tree.
"""


# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A: list of integers
    # @returns mx: element with maximum value
    # @returns mx_idx: index of maxaimum element
    def find_max(self, A):
        n = len(A)
        mx = float("-inf")
        mx_idx = -1

        for i in range(n):
            if A[i] > mx:
                mx = A[i]
                mx_idx = i

        return mx, mx_idx


	# @param A : list of integers
	# @return the root node in the tree
	def buildTree(self, A):
        # If the len of arr is None, then we have reached a root node
        # return None
        if len(A) < 1:
            return None

        # Find the max element
        mx, mx_idx = self.find_max(A)

        # All the elements before the max element will go in left subtree
        # because inorder traversal is given, so recursively call for left child
        left_root = self.buildTree(A[:mx_idx])

        # All the elements past the max element will go in right subtree
        # recursively call for right child
        right_root = self.buildTree(A[mx_idx+1:])

        # Make the max element as parent node
        parent = TreeNode(mx)

        # Add left and right child to parent node
        parent.left = left_root
        parent.right = right_root

        # Return parent node
        return parent