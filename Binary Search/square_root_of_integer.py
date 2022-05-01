"""
Given an integer A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.

NOTE: Do not use sort function from standard library. Users are expected to solve this in O(log(A)) time.
"""

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        
        if A < 2:
            return A
            
        else:
            low = 1
            high = A // 2
            while low<=high:
                
                mid =(low+high)//2
                sqr = mid*mid
                
                if sqr <= A:
                    low = mid + 1
                    ans = mid
                    
                elif sqr > A:
                    high = mid - 1
                    
            return ans
