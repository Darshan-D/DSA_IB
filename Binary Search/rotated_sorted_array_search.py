"""
Given an array of integers A of size N and an integer B.

array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value B to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        
        if len(A) == 0:
            return None
            
        low = 0
        high = len(A) - 1
        already_sorted = False
        
        while low <= high:
            mid = (low+high)//2
            n = (mid + 1)%len(A)
            p = (mid - 1 + len(A))%len(A)
            
            if A[low] <= A[high]:
                sorted_starts = low
                already_sorted = True
                break
                
            elif A[mid] <= A[n] and A[mid] <= A[p]:
                sorted_starts = mid
                break
                
            elif A[mid] <= A[high]:
                high = mid - 1
                
            elif A[mid] >= A[low]:
                low = mid + 1
        
        if not already_sorted:        
            if B <= A[sorted_starts-1] and B >= A[0]:
                low = 0
                high = sorted_starts - 1
            else:
                low = sorted_starts
                high = len(A) - 1
        else:
            low = 0
            high = len(A) - 1
            
        while low <= high:
            mid = (low+high)//2
            
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                low = mid + 1
            elif A[mid] > B:
                high = mid - 1
                
        return -1
            
