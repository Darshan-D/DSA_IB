"""
Find the contiguous subarray within an array, A of length N which has the largest sum.

Input Format:

The first and the only argument contains an integer array, A.
Output Format:

Return an integer representing the maximum possible sum of the contiguous subarray.
"""
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):

        curr_sm = 0
        max_sm = float('-inf')
        
        # Iterate through each element
        for ele in A:

            # Add curr element to curr_sm
            curr_sm += ele
            
            # Update max_sm
            if curr_sm > max_sm:
                max_sm = curr_sm
                
            # If curr_sm becomes -ve reset it
            if curr_sm < 0:
                curr_sm = 0
                
        return max_sm
