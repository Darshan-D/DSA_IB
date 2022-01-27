"""
Given a Binary Tree A containing N nodes.

You need to find the path from Root to a given node B.
"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def preorderTraversal(self, path, curr, B, found):
        
        # If we have reached the end, return the curr path and found status
        if curr is None:
            return path, found
        
        # Add the current node to the path
        path.append(curr.val)

        # If the current node is the target
        # return the path and found as True
        if curr.val == B:
            found = True
            return path, found
        
        # Else goto the left child
        path, found = self.preorderTraversal(path, curr.left, B, found)
        if found:
            return path, found

        # If not in left child, goto right child
        path, found = self.preorderTraversal(path, curr.right, B, found)
        if found:
            return path, found

        # Both the left and right child does not have target so remove current node
        # from the path
        path.pop(-1)
        return path, found


    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        path = []
        curr = A
        found = False
        path, found = self.preorderTraversal(path, curr, B, found)
        return path