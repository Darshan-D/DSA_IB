"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

NOTE : The path has to end on a leaf node.
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
    def minDepth(self, A):
        # If the root node does not have any one child, then we dont want
        # the func to return '1' as min depth, hence we check for None
        if A==None:
            return float('inf')

        # And we check from parent recursion call only, that whether it is
        # a leaf node or not, instead of actually going into the recursion call
        # of the node which is None, this again helps with the scenario explained above
        if A.left==None and A.right==None:
            return 1

        # Similar to max depth question, we use min, instead of max
        return 1 + min(self.minDepth(A.left),self.minDepth(A.right))