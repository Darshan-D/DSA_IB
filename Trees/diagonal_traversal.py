"""
Consider lines of slope -1 passing between nodes.

Given a Binary Tree A containing N nodes, return all diagonal elements in a binary tree belonging to same line.
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
        # We will store all the left childs in this queue
        queue = [A]

        # To store our results
        res = []

        # While we have more roots to traverse
        while len(queue) > 0:
            
            # Remove first element from the bottom of the queue
            root = queue.pop(0)

            # While the root is not None
            while root:

                # Store the left child of root in queue
                if root.left:
                    queue.append(root.left)
                
                # Store the current val in results
                res.append(root.val)

                # Goto the right child of the current root
                root = root.right

        return res