"""
You are given a preorder traversal A, of a Binary Search Tree.

Find if it is a valid preorder traversal of a BST
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # O(N) space and time complexity Solution

        # Use stack to keep track of next greater element
        stack = []
        root = float("-inf")

        for num in A:
            # If the num is greater than element in the stack
            # remove all the prev elements which are smaller than num
            # also keep on updating the root as the last removed element
            while len(stack) > 1 and num > stack[-1]:
                root = stack.pop()

            # If root becomes greater than it does not make a valid bst
            if root > num:
                return 0

            # Add current element to the stack
            stack.append(num)

        return 1
