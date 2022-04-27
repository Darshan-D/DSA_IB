"""
Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given integar B in array A.

Your algorithm’s runtime complexity must be in the order of O(log n).

Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].
"""

class Solution:
    
    def bs(self, arr, tg, big):
        low = 0
        high = len(arr) - 1
        index = - 1
        
        while low <= high:
            mid = (low+high)//2
            
            if arr[mid] == tg:
                index = mid
                if big:
                    low = mid + 1
                if not big:
                    high = mid - 1
                    
            elif arr[mid] > tg:
                high = mid - 1
                
            elif arr[mid] < tg:
                low = mid + 1
                
        return index
        
    def searchRange(self, A, B):
        first_index = self.bs(A, B, True)
        second_index = self.bs(A, B, False)
        return [second_index, first_index]
