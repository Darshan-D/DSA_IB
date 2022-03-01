"""
Given an integer array A of size N.

You need to check that whether there exist a element which is strictly greater than all the elements on left of it and strictly smaller than all the elements on right of it.

If it exists return 1 else return 0.
"""

class Solution:

    def perfectPeak(self, A):
        for i in range(1, len(A)-1):
            restart = False
            #checks if the elements on the right of A[i] are lesser
            for r in range(i+1, len(A)):
                if(A[i] < A[r]):
                    continue
                else:
                    restart = True
                    break
            #checks if the elements on the left are greater
            for l in range(i-1, -1, -1):
                if(A[i] > A[l]):
                    continue
                else:
                    restart = True
                    break
                    
            #checks if restart is true, if it is true, the control is sent back to the outer loop to 
            #check the aforementioned conditions for the next element 
            if restart:
                continue
            return 1
        return 0