"""
Given the position of a Bishop (A, B) on an 8 * 8 chessboard.

Your task is to count the total number of squares that can be visited by the Bishop in one move.

The position of the Bishop is denoted using row and column number of the chessboard.
"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        og_x = A
        og_y = B
        p_moves = 0

        curr_x = og_x
        curr_y = og_y

        # Squares possible in the top left
        while curr_x > 1 and curr_y > 1:
            p_moves += 1
            curr_x -= 1
            curr_y -= 1

        curr_x = og_x
        curr_y = og_y

        # Squares possible in the bottom right
        while curr_x < 8 and curr_y < 8:
            p_moves += 1
            curr_x +=1
            curr_y +=1

        curr_x = og_x
        curr_y = og_y

        # Squares possible in the top right
        while curr_x < 8 and curr_y > 1:
            p_moves += 1
            curr_x += 1
            curr_y -= 1

        curr_x = og_x
        curr_y = og_y
        # Squares possible in the bottom left
        while curr_x > 1 and curr_y < 8:
            p_moves += 1
            curr_x -= 1
            curr_y += 1

        return p_moves