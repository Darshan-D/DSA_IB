"""
Given a binary tree A with N nodes.

You have to remove all the half nodes and return the final binary tree.

NOTE:

Half nodes are nodes which have only one child.
Leaves should not be touched as they have both children as NULL.
"""


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def solve(self, A):

        def recurse(A):
            # If we have reached a leaf
            if A is None or (A.left is None and A.right is None):
                return A

            # If either child is absent
            if A is not None and (A.left is None or A.right is None):

                # If right is absent
                if A.right is None and A.left:
                    A = recurse(A.left)

                # If left is absent
                elif A.left is None and A.right:
                    A = recurse(A.right)


            # If both are present
            else:
                A.left = recurse(A.left)
                A.right = recurse(A.right)
            
            return A
        
        A = recurse(A)
        return A