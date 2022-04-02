"""
Given an array of all positive integers and an element “x”. 

You need to find out whether all array elements can be made equal or not by performing any of the 3 operations: add x to any element in array, subtract x from any element from array, do nothing.

This operation can be performed only once on an element of array.
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        for target in A:
            count = 0
            for num in A:
                if num==target:
                    count += 1
                elif num > target:
                    if (num-B)^target != 0:
                        break
                    else:
                        count += 1
                        
                elif num < target:
                    if (num+B)^target != 0:
                        break
                    else:
                        count += 1
                        
            if count == n:
                return 1
                
        return 0
                    
                    
