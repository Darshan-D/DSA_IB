"""
Merge k sorted linked lists and return it as one sorted list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        # Defining heap
        l=[]
        # Appending first node of every ll to the heap
        # along with index of that ll
        for i in range(len(A)):
            l.append([A[i].val,A[i]])

        # Heap sort the heap
        heapq.heapify(l)

        # max value of int
        int_max=float("inf")

        # Dummy head node
        head=ListNode(None)

        # Start making the ll
        curr=head
        while l[0][0]!=int_max:
            # Remove the smallest element from the heap
            top=heapq.heappop(l)

            # Get its node
            temp=top[1]

            # If current removed node is pointing to another node in the ll
            # then add it to the list
            if temp.next is not None:
                heapq.heappush(l,[temp.next.val,temp.next])
            
            # Else add max int val to the list
            else:
                heapq.heappush(l,[int_max,0])
            
            # Attach the removed node to the current node
            curr.next=temp

            # Update the current node
            curr=temp

        # return the head of the ll we made
        return head.next 