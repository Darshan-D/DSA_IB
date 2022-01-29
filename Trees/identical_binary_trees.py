"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : root node of tree
	# @return an integer
	def isSameTree(self, A, B):

        # If both the nodes are None, return true
        if A is None and B is None:
            return 1

        # If one of the node is None, return false
        elif A is None and B is not None or B is None and A is not None:
            return 0

        # If both nodes have equal value then only check for its kids
        if A.val == B.val:
            # Check if left and right subtree are equal
            if self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right):
                return 1

            else:
                return 0
        
        # If not equal then return false
        return 0
            