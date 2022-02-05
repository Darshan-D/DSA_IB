"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree.
"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        # If both the arrays become empty, then we have reached the end of tree
        if len(A) < 1 and len(B) < 1:
            return None

        # Last ele of post order will become the root
        root = TreeNode(B[-1])

        # Find the root element in inorder arr, this will give left and right sub tree 
        idx_inorder = A.index(B[-1])
        
        # Recursively call for left and right trees
        root.left = self.buildTree(A[:idx_inorder], B[:idx_inorder])
        root.right = self.buildTree(A[idx_inorder+1:], B[idx_inorder:-1])

        return root
        