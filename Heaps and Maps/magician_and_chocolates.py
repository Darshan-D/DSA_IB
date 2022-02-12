"""
Given N bags, each bag contains Bi chocolates. There is a kid and a magician. In one unit of time, kid chooses a random bag i, eats Bi chocolates, then the magician fills the ith bag with floor(Bi/2) chocolates.

Find the maximum number of chocolates that kid can eat in A units of time.

NOTE: 

floor() function returns the largest integer less than or equal to a given number.
Return your answer modulo 109+7
"""

# Base Idea
# Even though kid is picking the chocolate bags at random, since we 
# need to find maximum number of choclates kid can eat, we will always
# consider the scenario where picks the bag with maximum choclates

from heapq import heappush, heappop

class Solution:
	# @param A : integer
	# @param B : list of integers
	# @return an integer
	def nchoc(self, A, B):
        # Add all the elements from B into a max heap
        heap = []
        for num in B:
            # Taking -ve of num, since we want to make max heap
            heappush(heap, -num)

        # Final ans, this will store maximum choclates that can be eaten
        tot_chocolates = 0

        # Till the number of times kid can eat choclates
        while A > 0:
            A-=1

            # Assume that the kid will pick the bag with maximum choclates
            # we do this since we need to find maximum number of choclates a 
            # kid can eat in A units of time

            # Hence we remove from top of our heap
            # (taking the neg, since we inserted them as -ve)
            curr_bag_chocolates = -1 * heappop(heap)

            tot_chocolates += curr_bag_chocolates

            # Magician fills the bag with floor(Bi/2)
            curr_bag_chocolates = curr_bag_chocolates // 2

            # Add this back to the heap
            heappush(heap, -curr_bag_chocolates)

        # Remember to return as modulo
        return tot_chocolates%1000000007
