"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        # If len of list becomes 0, then we have reached the leaf node
        if len(A) < 1:
            return None

        # Divide the array in 2 parts
        mid = len(A)//2

        # All the elements upto the mid element (excluding mid element)
        # will goto the left subtree
        left_child = self.sortedArrayToBST(A[:mid])

        # The middle element will become parent node
        parent = TreeNode(A[mid])

        # All the elements after the mid element will goto right subtree
        right_child = self.sortedArrayToBST(A[mid+1:])

        # Join the parent with left and right subtree
        parent.left = left_child
        parent.right = right_child
        return parent