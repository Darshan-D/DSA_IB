"""
Given a large number represent in the form of an integer array A, where each element is a digit.

You have to find whether there exists any permutation of the array A such that the number becomes divisible by 60.

Return 1 if it exists, 0 otherwise.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def divisibleBy60(self, A):
        
        # Edge Case
        if len(A) == 1 and A[0] == 0:
            return 1
        
        sm = sum(A)
        
        # Sum should be divisible by 3,
        # if not digit cant be formed
        if sm%3 != 0:
            return 0
            
        # Array should contain 0 and another even digit
        zero_found = False
        even_found = False
        for num in A:
            if num == 0:
                zero_found = True
                
            elif num%2==0:
                even_found = True
                
            if zero_found and even_found:
                return 1
        
        #print("yello")        
        return 0
            
            
