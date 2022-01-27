"""
Given a binary tree, determine if it is height-balanced.

Height-balanced binary tree  : is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        
        # @param root: root of the tree
        # @param not_balanced: number of unbalanced subtrees
        def height(root, not_balanced):
            if root is None:
                return 0, not_balanced

            left_height, not_balanced = height(root.left, not_balanced) 
            right_height, not_balanced = height(root.right,not_balanced)

            left_height += 1
            right_height += 1

            # Check if the subtree is unbalanced
            if abs(left_height - right_height) > 1:
                not_balanced += 1

            # return the max of left tree and right tree as the height
            return max(left_height, right_height), not_balanced


        not_balanced = 0
        left_height, not_balanced = height(A.left, not_balanced) 
        right_height, not_balanced = height(A.right, not_balanced)
        
        # If number of not_balanced subtrees become greater than 0
        # then the tree is not balanced
        if not_balanced:
            return 0

        # Check for balance in left and right subtree of root node
        elif abs(left_height - right_height) > 1:
            return 0

        # If everything passes, then its balanced
        return 1
        
