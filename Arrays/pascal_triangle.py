"""
Given numRows, generate the first numRows of Pascal's triangle.
"""

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        # Base Cases
        if A < 1:
            return None
            
        elif A == 1:
            return [[1]]
            
        elif A == 2:
            return [[1], [1,1]]
            
        # Seeds to start making pascals triangle from third row
        final_arr = [[1], [1,1]]    # Answer array
        prev_arr = [1,1]            # Previous row of pascals triangle
        #temp = [1]                  
        
        for i in range(3, A+1):
            temp = [1]              # First element of current row
            
            
            # To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.
            for j in range(1, i):
                if j >= len(prev_arr):
                    temp.append(1)
                else:
                    temp.append(prev_arr[j-1]+prev_arr[j])
                    
            final_arr.append(temp)
            prev_arr = temp
            
        return final_arr
