"""
Given an array A , representing seats in each row of a stadium. You need to sell tickets to B people.

Each seat costs equal to the number of vacant seats in the row it belongs to. The task is to maximize the profit by selling the tickets to B people.
"""

import heapq

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        heap = []
        for ele in A:
            heapq.heappush(heap, -ele)
        
        # Remove the largest element
        # Decrease the value of largest element
        # and add it to the heap
        # Decrease the value of req tickets by 1
        ans = 0
        while B:
            smallest = heapq.heappop(heap)
            ans += -smallest
            smallest -= -1
            heapq.heappush(heap, smallest)
            B -= 1

        return ans