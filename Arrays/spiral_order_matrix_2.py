"""
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.
"""

class Solution:
	# @param A : integer
	# @return a list of list of integers
	def generateMatrix(self, A):
        # Generate the matrix with req size and populate with -1
        ans = [[-1 for i in range(A)] for j in range(A)]

        # This are the starting row/col number for each direction
        T = 0   # Top
        L = 0   # Left
        B = A-1 # Bottom
        R = A-1 # Right
        direction = 0   # Increse this by 1, after traversing one dir completely 
        count = 1       # This will give the value of element which we need to put in the matrix

        # While the top - bottom and left - right border
        # have not crossed each other
        while T<=B and R>=L:

            # Go from left to right
            if direction == 0:
                for i in range(L, R+1):
                    ans[T][i] = count
                    count += 1

                # We have traversed one lvl from top, so change its limit
                T += 1

            # Go from top to bottom
            if direction == 1:
                for i in range(T, B+1):
                    ans[i][R] = count
                    count += 1

                # We have traversed one lvl from right, so change its limit
                R -= 1

            # Go from right to left
            if direction == 2:
                for i in range(R, L-1, -1):
                    ans[B][i] = count
                    count += 1

                # We have traversed one lvl from bottom, so change its limit
                B -= 1

            # Go from bottom to top
            if direction == 3:
                for i in range(B, T-1, -1):
                    ans[i][L] = count
                    count += 1

                # We have traversed one lvl from left, so change its limit
                L += 1

            # change the direction value, this will help us determine the next direction
            direction = (direction + 1)%4

        return ans
        
