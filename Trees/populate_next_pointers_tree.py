"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
"""

# The trick to do it in constant extra space is to use the next pointers we have been building
# to do the level order traversal instead of using queue


# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def connect(self, root):
        curr = root

        # Will help to goto the next level of the tree
        next_level_start = None

        # Will store the node whoes 'next' we have to set
        prev_child = None

        while curr is not None:
            # If left child exist
            if curr.left is not None:
                # point the prev_child to this left child
                if prev_child is not None:
                    prev_child.next = curr.left

                # if the prev child was None, then left child will be at the next level
                # (dry run it, it will make more sense)
                else:
                    next_level_start = curr.left

                # now prev_child will store the curr.left because, now we want to
                # set the next of this child
                prev_child = curr.left

            # Same logic we used for left child
            if curr.right is not None:
                if prev_child is not None:
                    prev_child.next = curr.right
                else:
                    next_level_start = curr.right
                prev_child = curr.right

            # Use the next pointers we had set to traverse to the next node
            # of the same level
            curr = curr.next 

            # If the next is not None, then it means there are more nodes in the 
            # current level so continue
            if curr is not None:
                continue

            # Else the level is complete
            # Update curr to next level's starting node
            # and reset everything else
            curr = next_level_start
            next_level_start = None
            prev_child = None