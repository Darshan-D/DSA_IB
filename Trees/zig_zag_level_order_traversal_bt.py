"""
Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).
"""


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        # Main Idea of the Solution
        # Do a regular lvl order traversal,
        # but also keep track of the current lvl in the queue
        # if current lvl is even then reverse the current lvl
        
        if A is None:
            return []
        res = []
        q = [[A,1]]
        
        while len(q)>0:
            r = []
            curq = []
            while len(q)>0:
                arr = q.pop(0)
                temp = arr[0]
                hi = arr[1]
                r.append(temp.val)
                if temp.left:
                    curq.append([temp.left, hi+1])
                if temp.right:
                    curq.append([temp.right, hi+1])
            
            if hi%2==0:
                r = r[::-1]
            q = curq
            res.append(r)
        return res