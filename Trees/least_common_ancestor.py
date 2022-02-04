"""
Find the lowest common ancestor in an unordered binary tree given two values in the tree.

Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w in a tree or directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:

    def find_ancestors(self, A, val, arr):
        # If the current node is None, then the 
        # element is not in the tree
        if not A:
            found = False
            return arr, found

        # Append the current node val to the path
        arr.append(A.val)

        # Req val is found
        if A.val == val:            
            found = True
            return arr, found

        # Search on left sub tree
        arr, found = self.find_ancestors(A.left, val, arr)

        # If not found in left sub tree then search in right sub tree
        if not found:
            arr, found = self.find_ancestors(A.right, val, arr)

        # If not found in either, then, pop the current node from the path,
        # since none of its child has the value and return to prev recursion call
        if not found:
            arr.pop(-1)
            return arr, found
            
        return arr, found

	# @param A : root node of tree
	# @param B : integer
	# @param C : integer
	# @return an integer
	def lca(self, A, B, C):
        lca = -1

        # Lists to store the path to required nodes
        arr1 = []   # Path for Node 1
        arr2 = []   # Path for Node 2
        
        # Find the path to Node 1
        arr1, found1 = self.find_ancestors(A, B, arr1)
        
        # Find the path to Node 2
        arr2, found2 = self.find_ancestors(A, C, arr2)

        # If either path is not found, return -1
        if not found1 or not found2:
            return -1

        # Iterate through both the paths, and keep on
        # updating the lca till the elements from both the
        # path are equal, as soon as they become unequal
        # breakout from the path
        for i in range(min(len(arr1), len(arr2))):
            if arr1[i] == arr2[i]:
                lca = arr1[i]
            else:
                break

        return lca