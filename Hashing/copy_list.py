"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or NULL.

Return a deep copy of the list.
"""


# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        # O(N) time and space complexity

        # Make a dict to store old nodes as keys and new nodes as values
        # We take the first pass to make this dictionary
        # in the second pass we set the pointers
        oldTocopy = {None:None}

        # First Pass, copy the LL and make new nodes
        # while storing the old and new mapping
        curr = head
        while curr:
            new = RandomListNode(curr.label)
            oldTocopy[curr] = new
            curr = curr.next

        # Second pass, set the pointers
        curr = head
        while curr:
            new = oldTocopy[curr]
            new.next = oldTocopy[curr.next]
            new.random = oldTocopy[curr.random]
            curr = curr.next

        # Returning the new head
        return oldTocopy[head]