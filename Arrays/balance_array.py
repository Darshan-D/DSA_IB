"""
Given an integer array A of size N. You need to count the number of special elements in the given array.

A element is special if removal of that element make the array balanced.

Array will be balanced if sum of even index element equal to sum of odd index element.
"""



class Solution:
    # @param A : list of integers
    # @return an integer
    
    def solve(self, A):
        n = len(A)
        # store sum of all the elements at even and odd digits respectively
        even = 0
        odd = 0
        i = 0
        while i<n:
            if i%2==0:
                odd += A[i]
            else:
                even += A[i]
            i += 1
        
        ans = 0     
        x = 0   # Store the sum of new elements at even place
        y = 0   # Store the sum of new elements at odd place
        i = 0
        
        while i<n:
            if i%2==0:
                odd -= A[i]
            else:
                even -= A[i]
                
            # If the sum of prev odd/even and new pdd/even is same, array is balanced
            if odd+x == even+y:
                ans += 1
                
            if i%2==0:
                y += A[i]
            else:
                x += A[i]
            i += 1
            
        return ans
                
                
