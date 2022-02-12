"""
Given two equally sized 1-D arrays A, B containing N integers each.

A sum combination is made by adding one element from array A and another element of array B.

Return the maximum C valid sum combinations from all the possible sum combinations.
"""
from heapq import heappush, heappop

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        n = len(A)
        
        # Sort the arrays in descending order so that max sm value
        # will occur by adding elements from begining
        A.sort(reverse=True)
        B.sort(reverse=True)
        
        # Sum up the first elements of both arrays and them
        # into the heap, along with their indices 
        # (store this 3 as tuples i.e sum, A_idx, B_idx)
        h = [(-(A[0]+ B[0]), 0, 0)]

        # A set to not check for the same combination twice
        # contains A_idx and B_idx as tuples
        visited = {(0, 0)}

        # ans list
        ans = []
        
        # While we have not got the required number of sum combinations
        while len(ans) < C:
            # Remove element from top of the heap
            popped, i, j = heappop(h)
            ans.append(-popped)
        
            # Check if the diagonal elements are visited
            # if not add it to the heap, and visited set
            if (i+1, j) not in visited:
                heappush(h, (-(A[i+1]+B[j]), i+1, j))
                visited.add((i+1, j))
        
            if (i, j+1) not in visited:
                heappush(h, (-(A[i]+B[j+1]), i, j+1))
                visited.add((i, j+1))
        
        return ans