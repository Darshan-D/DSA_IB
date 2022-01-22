"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a = b = c = d)
The solution set must not contain duplicate quadruplets.
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        
        # O(N * Log(N))
        # Sorting it out since we gonna use two pointer approach
        A.sort()
        result = set()
        
        # O(N ^ 2) Time
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                lo, hi = j + 1, len(A) - 1
                
                # O(N) Time
                # Basic 2 pointer approach
                while lo < hi:
                    x = A[i] + A[j] + A[lo] + A[hi]
                    
                    if x == B:
                        result.add((A[i], A[j], A[lo], A[hi]))
                        hi -= 1
                        lo += 1

                    elif x > B:
                        hi -= 1
                    else:
                        lo += 1

        return sorted(result)