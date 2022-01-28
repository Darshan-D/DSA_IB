"""
Given two Binary Trees A and B, you need to merge them in a single binary tree.

The merge rule is that if two nodes overlap, then sum of node values is the new value of the merged node.

Otherwise, the non-null node will be used as the node of new tree.
"""

class Solution:
    def solve(self, A, B):
        # Pointers for 2 trees
        t1 = A
        t2 = B

        # If one of the tree is empty, return another tree
        if (not t1):
            return t2
        if (not t2):
            return t1

        # If both overlap, add them
        # we are making the final tree into the first tree
        t1.val += t2.val

        # Recursively go to the left and right of both trees
        t1.left = self.solve(t1.left, t2.left)
        t1.right = self.solve(t1.right, t2.right)

        # Return the ans tree
        return t1
        