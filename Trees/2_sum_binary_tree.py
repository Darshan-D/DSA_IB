"""
Given a binary search tree A, where each node contains a positive integer, and an integer B, you have to find whether or not there exist two different nodes X and Y such that X.value + Y.value = B.

Return 1 to denote that two such nodes exist. Return 0, otherwise
"""



# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        s_left = [A]
        while s_left[-1].left is not None:
            s_left.append(s_left[-1].left)

        s_right = [A]
        while s_right[-1].right is not None:
            s_right.append(s_right[-1].right)

        while s_left and s_right and s_left[-1].val < s_right[-1].val:
            if s_left[-1].val + s_right[-1].val < B:
                u = s_left.pop()
                u = u.right
                if u is not None:
                    s_left.append(u)
                    while s_left[-1].left is not None:
                        s_left.append(s_left[-1].left)
            elif s_left[-1].val + s_right[-1].val > B:
                u = s_right.pop()
                u = u.left
                if u is not None:
                    s_right.append(u)
                    while s_right[-1].right is not None:
                        s_right.append(s_right[-1].right)
            else:
                return 1
                
        return 0
                