"""
Given a binary tree, return the Postorder traversal of its nodes values.

NOTE: Using recursion is not allowed.
"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        result = []; 
        d = [A]
        while d:
            node = d.pop()
            if node:
                result.append(node.val)
                d.append(node.left)
                d.append(node.right)
        return result[::-1]