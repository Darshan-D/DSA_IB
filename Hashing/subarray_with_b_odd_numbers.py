"""
Problem Description

Given an array of integers A and an integer B.

Find the total number of subarrays having exactly B odd numbers.
"""


# O(N) time and O(1) Space Complexity Solution
# Basic CRUX - Sliding Window / Two Pointer Apporach
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        def find(A, B):
            """
            To find number of subarrays having utmost B odd numbers
            
            Args:
            A - list of integers
            B - Upper limit of odd numbers we can have in subarray
            
            Ret:
            tot_sub_arr - total number of subarray satisfying above condition
            """
            
            # Initialize the window
            ws = 0
            we = 0
            n = len(A)
            
            # Total odd numbers in the current window, and 
            # total sub arrays satisfying given condition
            odd_num = 0
            tot_sub_arr = 0

            # Keep on expanding the window
            while we < n:
                if A[we]%2 != 0:
                    odd_num += 1
                    
                # When number of odd element inc above threshold
                # decrese the size of the window
                while odd_num > B and ws <= we:
                    if A[ws]%2 != 0:
                        odd_num -= 1
                    ws += 1

                tot_sub_arr += we - ws + 1
                we += 1

            return tot_sub_arr
            
        # Find subarrays having utmost B odd numbers
        # subtract it with subarrays having utmost B-1 odd numbers
        # this will give the desired result
        res = find(A, B) - find(A,B-1)
        return res
        
        