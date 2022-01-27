"""
Given the root of a binary tree A, the value of a target node B, and an integer C, return an array of the values of all nodes that have a distance C from the target node.

You can return the answer in any order.
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
    # @param C : integer
    # @return a list of integers
    def distanceK(self, A, B, C):

        # @param root : node which we will seach for the req target
        # @param target : taget val needed
        # @param found : boolean representing, whether we have found the target or not
        def search(root, target, found):
            if root is None:
                return found

            if root.val == target:
                found = True
                stack.append(root)
                return curr_dist, found

            # append the current node to the stack
            # this will help, as we will have a way to goto the parent
            # of current node while doing dfs
            stack.append(root)
            
            # Goto the left child
            found = search(root.left, target, found)
            if found:
                return curr_dist, found
            
            # Goto the right child
            found = search(root.right, target, found)
            if found:
                return curr_dist, found

            # If not found in either child, then this is not a path
            # to the target so remove it from the stack
            stack.pop()

            return found


        # @param root : node from where we do bfs (go top, left or bottom)
        # @param curr_dist : curr_dist from the target node
        def dfs(root, curr_dist):

            # When distance becomes equal to the target dist
            # append node val to the ans
            if curr_dist == req_dist and root:
                ans.append(root.val)

            # Add current node to the visited set
            visited.add(root)

            curr_dist += 1

            # Go Up
            if len(stack) > 0:
                parent = stack.pop()
                if parent not in visited:
                    dfs(parent, curr_dist)

            if root:
                # Go left
                if root.left not in visited:
                    dfs(root.left, curr_dist)

                # Go right
                if root.right not in visited:
                    dfs(root.right, curr_dist)


        target = B
        req_dist = C
        curr_dist = 0
        ans = []
        stack = []
        found = False

        # First search the target in the tree
        found = search(A, target, found)

        
        # Now run a dfs, for every node
        # We can go top, left and right
        # go into that dir only if we have not visited it before
        # when the distance becomes equal to req dist we stop
        # and add all the elements in the ans
        visited = set()
        curr_dist = 0
        root = stack.pop()  # return the node of the target
        dfs(root, curr_dist)
        return ans