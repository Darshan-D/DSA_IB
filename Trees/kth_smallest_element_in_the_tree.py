"""
Given a binary search tree, write a function to find the kth smallest element in the tree.
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param arr : list of all the elements
    # @param curr : curret root node
    # @return arr : list of all the elements
    def inorderTraversal(self, arr, curr): 
        if curr is None:
            return arr

        if curr.left:
            arr = self.inorderTraversal(arr, curr.left)
        
        arr.append(curr.val)
        
        if curr.right:
            arr = self.inorderTraversal(arr, curr.right)

        return arr


	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
        arr = []
        curr = A
        arr = self.inorderTraversal(arr, curr)
        return arr[B-1]