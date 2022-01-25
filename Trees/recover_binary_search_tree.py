"""
Two elements of a binary search tree (BST) are swapped by mistake.

Tell us the 2 values swapping which the tree will be restored
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
    def recoverTree(self, A):
    
            def inorder(node, li):
    
                if node.left:
    
                    inorder(node.left,li)
    
                li.append(node.val)
    
                if node.right:
    
                    inorder(node.right,li)
    
            
            # To not use extra space, simulate the array using a previous pointer
            # If any element is smaller than prev element, then that element is one
            # of the swapped element, similarly find the second one
            li = []
    
            inorder(A,li)
    
            sli = sorted(li)
    
            for i,j in zip(li,sli):
    
                if i!=j:
    
                    return sorted([i,j]) 
    
    
            return []
