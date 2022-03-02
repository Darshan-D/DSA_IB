"""
Given an index k, return the kth row of the Pascal's triangle.

Input : k = 3


Return : [1,3,3,1]

Note: k is 0 based. k = 0, corresponds to the row [1]. 

Note: Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):

        # Initialize for base cases
        if A == 0:
            return [1]
        if A == 1:
            return [1,1]

        if A == 2:
            return [1,2,1]

        
        row_arr = [1,2,1]
        
        # Basic Idea - To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1
        # where A' represents previous row
        for i in range(3, A+1):

            # First element of pascal's triangle will always be 1
            curr_row = [1]
            for j in range(1,i):
                # Add jth and (j-1)th val from prev row 
                curr_val = row_arr[j] + row_arr[j-1]

                # Append it to current row
                curr_row.append(curr_val)

            # Last element of pascal's triangle will always be 1
            curr_row.append(1)

            # Update row_arr
            row_arr = curr_row

        return row_arr