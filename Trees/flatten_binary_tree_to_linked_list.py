"""
Given a binary tree, flatten it to a linked list in-place.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):

        def dfs(root):
            if not root:
                return None

            # Flatten the left subtree
            leftTail = dfs(root.left)

            # Flatten the right subtree
            rightTail = dfs(root.right)

            # If there is a left subchild
            # then add its flatten list to the
            # right of current parent
            # and connect the current right child
            # to the tail of this flattend list
            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None

            # Return the tail of the current list
            # with the order of pref as rightTail > leftTail > root
            last = rightTail or leftTail or root
            return last

        dfs(A)
        return A