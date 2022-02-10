"""
Given two integers arrays A and B of size N each.

Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B.
"""

from queue import PriorityQueue

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):

        # Sort the two arrs so that, their  biggest elements
        # are at the end of list
        A.sort()
        B.sort()
    
        # Implement the max heap, this will store the bigger elements
        # on top and will help to return the element in descending order
        # as required in the question
        pq = PriorityQueue()
    
        # A set to store all the visited indexes 
        s = set()
        
        n = len(A)
        
        # Since both arrs are sorted, one of the element which will be maximum for sure
        # is the one made by adding the last elements of both arrs together
        # Add that to the heap along with indexes of arr A and arr B, which made that sum
        pq.put((-1*(A[n-1]+B[n-1]), (n-1, n-1)))

        # Add the indices whose sum we took in the set
        s.add((n-1, n-1))

        # Will store all the results we need
        res = list()
        
        # Iterate N number of times, since we need N maximum element
        for k in range(n):
            # Get the top value of the heap
            value = pq.get()

            # Split it into its components viz.
            # sum, index in A, index in B (which made that sum)
            sum_, i, j = value[0], value[1][0], value[1][1]

            # Add this sum to the result list
            res.append(-1*sum_)

            # Take a sm of left diagonal elements
            idx_pair1  = (i-1, j)
            pair1 = (-1*(A[i-1]+B[j]), idx_pair1)

            # If indices not in the set, add them in the set
            # also update the heap
            if idx_pair1 not in s:
                s.add(idx_pair1)
                pq.put(pair1)
            

            # Do the same for right diagonal elements
            idx_pair2  = (i, j-1)
            pair2 = (-1*(A[i]+B[j-1]), idx_pair2)
            if idx_pair2 not in s:
                s.add(idx_pair2)
                pq.put(pair2)
            
        return res