"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
"""

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        # Base Case
        if len(A) <= 0:
            return A
            
        # Make a new matrix, to store the rotated image
        rot = [[0 for i in range(len(A))] for i in range(len(A))]
        
        # Iterate through the original matrix
        for i in range(len(A)):
            for j in range(len(A)):
                # Populate the new matrix
                rot[j][len(A)-1-i] = A[i][j]
                
        return rot
