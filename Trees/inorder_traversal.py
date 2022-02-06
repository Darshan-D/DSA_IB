"""
Given a binary tree, return the inorder traversal of its nodes values.
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    def doit(self, curr, ans):
        if not curr:
            return ans

        
        ans = self.doit(curr.left, ans)
        ans.append(curr.val)
        ans = self.doit(curr.right, ans)
        return ans


	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):
        ans = []
        ans = self.doit(A, ans)
        return ans