"""
Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return a list of list of integers
	def pathSum(self, A, B):

        # @param root: the node of the binary tree
        # @param target: target sum we wanna achieve
        # @param curr_res: list of nodes in the current sm (basically sum of path values)
        # @param curr_sm: total sm of values of path nodes till current node
        # @param res: final list we need
        # @returns res: final list we need
        def solve(root, target, curr_res, curr_sm, res):

            # Check if curr_sm and curr node val gives the target
            # and if the curr node is the lead node
            if curr_sm + root.val == target and root.left is None and root.right is None:
                # Append the curr node to the curr_res
                curr_res.append(root.val)

                # Copy the curr_res to final res
                res.append(curr_res[:])
                return res

            # Update the sm and curr_res
            curr_sm += root.val
            curr_res.append(root.val)

            # Goto left/right subtree only if they exist
            if root.left:
                # Passing the copy of curr_res, since passing it directly
                # makes it pass as a global var and messes up the ans
                res = solve(root.left, target, curr_res[:], curr_sm, res)

            if root.right:
                res = solve(root.right, target, curr_res[:], curr_sm, res)
            
            return res
            

                
        res = []
        curr_res = []
        root = A
        target = B
        curr_sm = 0
        res = solve(root, target, curr_res, curr_sm, res)
        return res