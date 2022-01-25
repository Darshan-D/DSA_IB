"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest number in the BST, and so on.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Try to optimize the additional space complexity apart from the amortized time complexity.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.stack = []

        # Goto the leftmost child and save all the parents
        # on its way inside a stack
        self.gotoLeft(self.root)

    # @param curr, root node, whoes left most child we will visit
    def gotoLeft(self, curr):
        # While curr exist, visit the leftmost child
        # while storing all the parents on its way inside the stack
        while curr:
            self.stack.append(curr)
            curr = curr.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        # If our stack becomes empty, then we have traversed the whole tree
        if len(self.stack) > 0:
            return True
        
        return False

    # @return an integer, the next smallest number
    def next(self):
        # If there are more values
        if self.hasNext():

            # Remove the first one from the stack
            # It is the current req ans
            ans = self.stack.pop()

            # If the curr has a right child
            curr = ans.right
            if curr:
                # Visit and store all its leftside children
                self.gotoLeft(curr)

            return ans.val
        

        

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
