"""
You are in an infinite 2D grid where you can move in any of the 8 directions

 (x,y) to 
    (x-1, y-1), 
    (x-1, y)  , 
    (x-1, y+1), 
    (x  , y-1),
    (x  , y+1), 
    (x+1, y-1), 
    (x+1, y)  , 
    (x+1, y+1) 
You are given a sequence of points and the order in which you need to cover the points.. Give the minimum number of steps in which you can achieve it. You start from the first point.
"""

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        
        total_steps = 0
        
        if len(A) <= 1 or len(B) <= 1:
            return 0
        
        # Since the order of traversal to the final destination is alredy given
        # we just have to calculate distance between 2 points and keep on adding them

        # Iterate through the grid
        for i in range(len(A) - 1):

          # Extract co-ordinates
          x1, y1 = A[i], B[i]
          x2, y2 = A[i+1], B[i+1]
        
          # The max of X and Y will give us the no. of steps to take
          # to traverse to curr destination
          X = abs(x1 - x2)
          Y = abs(y1 - y2)
          
          step_taken = max(X, Y)
          total_steps += step_taken
          
        return total_steps
