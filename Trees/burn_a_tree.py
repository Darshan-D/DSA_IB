"""
Given a binary tree denoted by root node A and a leaf node B from this tree.

 It is known that all nodes connected to a given node (left child, right child and parent) get burned in 1 second. Then all the nodes which are connected through one intermediate get burned in 2 seconds, and so on.

You need to find the minimum time required to burn the complete binary tree.
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
    def solve(self, A, B):

        def find_leaf_node(root, target, found):
            if root is None:
                # returning a boolean just to check whether we found the
                # the target or not, it has no use in bfs
                # it will help to stop our search for target further
                return None, False

            if root.val == target:
                return root, True

            if root.left:
                req_node, found = find_leaf_node(root.left, target, found)

            if found:
                # if the boolean is true we stop the recursion (search)
                return req_node, found

            if root.right:
                req_node, found = find_leaf_node(root.right, target, found)

            if found:
                return req_node, found

            return None, False


        # Store the parents of all the nodes using traversal
        # this will help later during bfs
        parents = {}
        q = [A]
        while len(q) > 0:
            root = q.pop(0)
            if root:
                if root.left:
                    parents[root.left] = root
                if root.right:
                    parents[root.right] = root

                q.append(root.left)
                q.append(root.right)


        # A set of visited nodes, will help to not visit the same node
        # again during BFS
        visited = set()

        # Find the leaf node from where we need to burn
        found = False
        burn_from, found = find_leaf_node(A, B, found)


        q = [burn_from]
        t = 0
        visited.add(burn_from)
        while len(q) > 0:
            ln_q = len(q)
            burnt = False
        
            for i in range(ln_q):
                node = q.pop(0)

                # For every node, we can burn left, right and parent
                if node.left and node.left not in visited:
                    q.append(node.left)
                    burnt = True
                    visited.add(node.left)

                if node.right and node.right not in visited:
                    q.append(node.right)
                    burnt = True
                    visited.add(node.right)

                if node in parents and parents[node] not in visited:
                    q.append(parents[node])
                    burnt = True
                    visited.add(parents[node])

            # Increase the time only if we have burnt anything
            if burnt:
                t+=1

        return t