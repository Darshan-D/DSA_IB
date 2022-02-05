"""
You are given the root of a binary tree A.

You have to find the vertical sum of the tree.

A vertical sum denotes an array of sum of the different verticals of a binary tree,

where the leftmost vertical sum is the first element of the array and rightmost vertical is the last.
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
    def verticalSum(self, A):
        def traverse_tree(root, vertical_lvl, curr_lvl):
            # If node is null, we have came beyond leaf node
            if root is None:
                return vertical_lvl

            # Val of current node
            val = root.val

            # If curr_lvl is in dict, update its sum
            if curr_lvl in vertical_lvl:
                vertical_lvl[curr_lvl] += val

            # Else initialize its sm as the val
            else:
                vertical_lvl[curr_lvl] = val

            # Recursively call for left and right subtrees
            vertical_lvl = traverse_tree(root.left, vertical_lvl, curr_lvl-1)
            vertical_lvl = traverse_tree(root.right, vertical_lvl, curr_lvl+1)

            return vertical_lvl

        # This dictionary will store the sm of all elements with same vertical lvl
        vertical_lvl = {}

        # Root node will be at vertical_lvl 0
        curr_lvl = 0
        vertical_lvl = traverse_tree(A, vertical_lvl, curr_lvl)
        
        # The mx and mn will give us the breath of tree
        mn_lvl = 0
        mx_lvl = 0
        for key in vertical_lvl:
            if key < mn_lvl:
                mn_lvl = key

            elif key > mx_lvl:
                mx_lvl = key

        # To store the result
        res = []

        # Iterate through all the lvls between mx and mn lvl
        for i in range(mn_lvl, mx_lvl+1):
            if i in vertical_lvl:
                sm = vertical_lvl[i]
                res.append(sm)

        return res