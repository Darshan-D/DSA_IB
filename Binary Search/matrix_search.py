"""
Given a matrix of integers A of size N x M and an integer B.

Write an efficient algorithm that searches for integar B in matrix A.

This matrix A has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.
"""

# To solve this problem
# 1. Find the row where B might be present
# 2. Find B in that row

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        
        def bs(A,B):
            start = 0
            end = len(A) - 1
            found = False
            
            while end>=start:

                mid = start + (end-start)//2

                if A[mid] == B:
                    found = True
                    return mid, found
                
                elif A[mid] > B:
                    end = mid - 1

                elif A[mid] < B:
                    start = mid + 1

            # If not found, then mid will point to the nearest value
            # Check if the val pointed by mid is bigger
            # If so decrease it by 1, it will give the postion
            # where B should have been
            if A[mid] > B:
                return mid - 1, found
            return mid, found

        
        # Make an array which contains first element of the rows
        row_arr = []
        for i in range(len(A)):
            row_arr.append(A[i][0])

        # Try to figure out in which row B will be present
        row_num, found = bs(row_arr, B)
        possible_row = A[row_num]

        # Once found that row, seach for B
        idx,found = bs(possible_row, B)
        if found:
            return 1
        return 0
