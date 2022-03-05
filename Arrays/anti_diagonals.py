"""
Give a N*N square matrix, return an array of its anti-diagonals. 

Input:

1 2 3
4 5 6
7 8 9
Return the following:
[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]
"""

# Basic Funda
# For every diagonal, the next element will be at pos i+=1 and j-=1

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):

        N = len(A)

        # Edge cases
        if N == 1:
            return [A[0]]

        elif N < 1:
            return [[]]

        ans = []

        # For non initial seed
        m = 0

        # The number of diagonals which can be made for a given N
        limit = N + (N-1)

        k = 0
        
        while k < limit:
            
            # If we are traversing the first row
            # Give initial seed and use basic funda 
            if k < N:
                i = 0
                j = 0 + k
                curr_ans = []
                while i >= 0 and j >= 0:
                    curr_ans.append(A[i][j])
                    i += 1
                    j -= 1
            
            # When we have completed traversing the first row
            # Use different seed and use basic funda
            else:
                i = 1 + m
                j = N - 1
                curr_ans = []
                while i < N and j < N:
                    curr_ans.append(A[i][j])
                    i += 1
                    j -= 1
                
                m += 1

            ans.append(curr_ans)
            k += 1

        return ans
