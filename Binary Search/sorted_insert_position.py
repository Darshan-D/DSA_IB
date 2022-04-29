"""
Given a sorted array A and a target value B, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        def bs(A, B):
            low = 0
            high = len(A) - 1

            while low <= high:

                mid = (low+high)//2

                if A[mid] == B:
                    return mid, True
                elif A[mid] > B:
                    high = mid - 1
                else:
                    low = mid + 1

            return mid, False

        mid, found = bs(A,B)
        
        if found or A[mid]>B:
            return mid
        
        return mid+1
            
        
