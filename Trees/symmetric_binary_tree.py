"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
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
	def isSymmetric(self, A):

        # @param l_root: left child of the parent
        # @param r_root: right child of the parent
        # @return an integer 1/0 on whether its symmetric or not 
        def check(l_root, r_root):
            # If both the roots are None
            if l_root is None and r_root is None:
                return 1

            # If only one of the root is None
            elif l_root is None and r_root is not None or r_root is None and l_root is not None:
                return 0

            # If their value is equal, check for subtrees
            elif l_root.val == r_root.val:
                # Left child of left node should be equal to right child of right node and vice versa
                # since we are checking for symmetricity hence it is inverted
                return check(l_root.left, r_root.right) and check(l_root.right, r_root.left)


            # If they are not equal, then its not symmetric
            else:
                return 0


        return check(A.left, A.right)
