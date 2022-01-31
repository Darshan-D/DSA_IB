"""
Given a binary tree A of integers. Return an array of integers representing the right view of the Binary tree.

Right view of a Binary Tree: is a set of nodes visible when the tree is visited from Right side.
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
    def solve(self, A):

        # @param root: current root of the tree
        # @param res: list of values which will come in the right_view
        # @param curr_lvl: curr_lvl/depth where we are in the tree
        # @param mx_lvl: max lowest lvl till where we have reached
        # @return res: list of values in the right_view
        # @return mx_lvl: max lowest lvl till where we have reached
        def right_view(root, res, curr_lvl, mx_lvl):

            # If the current node is null, then return the values
            if not root:
                return res, mx_lvl
            
            # If the curr_lvl is greatest i.e the first time we have came to this depth
            # then current value will come in right_view
            if curr_lvl > mx_lvl:
                res.append(root.val)
                mx_lvl = curr_lvl

            # Recrusively call on right sub tree first (since we want to print right view)
            # then call on left sub tree
            res, mx_lvl = right_view(root.right, res, curr_lvl+1, mx_lvl)
            res, mx_lvl = right_view(root.left, res, curr_lvl+1, mx_lvl)
            return res, mx_lvl

        res = []
        curr_lvl = 0
        mx_lvl = -1
        res, mx_lvl = right_view(A, res, curr_lvl, mx_lvl)
        return res
