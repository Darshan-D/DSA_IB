"""
Given a binary tree, return the reverse level order traversal of its nodes values. (i.e, from left to right and from last level to starting level).
"""

# There's a better solution than this one, do a regular level order traversal
# instead of printing push it in a list, at last reverse the list and return it

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
        # Store the nodes along with horizontal levels as tuples inside a stack
        stack = [(A,0)]

        # A hash_map to store all the elements at a particular lvl
        # it will have lvl as key and list of elements as value
        hash_map = {}

        # mx_lvl will give us the height of tree
        mx_lvl = 0

        # Do a level order traversal
        while len(stack) > 0:
            root, lvl = stack.pop()

            # Add the current root and level to the hash_map
            if root:
                if lvl not in hash_map:
                    hash_map[lvl] = [root.val]
                else:
                    hash_map[lvl].append(root.val)
                
                # Add its left and right child to the stack
                stack.append((root.left, lvl+1))
                stack.append((root.right, lvl+1))

                # Update the mx_lvl
                mx_lvl = max(mx_lvl, lvl)
        
        res = []

        # Start iterating from the lowest node (?ighest lvl)
        # extract its value from hash_map, 
        # reverse it (since it will have right childs first due to level order traversal, dry run it for yourself to observe it)
        # and store the elements in the res list 
        for i in range(mx_lvl, -1, -1):
            res += hash_map[i][::-1]

        return res

