"""
Given an sorted array A of size N. Find number of elements which are less than or equal to B.

NOTE: Expected Time Complexity O(log N)
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # Basically we have to find the last occurence of B
        def bs(A,B):
            start = 0
            end = len(A) - 1
            found = False

            # Do Binary Search for the last occurence
            while end>=start:
                mid = start + (end-start)//2

                # If found update the idx var to the last
                # found value of B
                if A[mid] == B:
                    found = True
                    idx = mid
                    start = mid + 1

                elif A[mid] > B:
                    end = mid - 1

                elif A[mid] < B:
                    start = mid + 1

            # If B is found return it's last found idx
            if found:
                return idx

            # If not then mid will point to the nearest value to B
            else:
                # If the value pointed by mid is greater than B
                # Then we cannot count from there, we need to take
                # a step back and count
                if A[mid] > B:
                    return mid - 1

                # If value pointed by mid is less than B
                # Than we can count from there itself
                return mid
        
        # Edge Case ---
        if A[0] > B:
            return 0

        # Do the binary search
        idx = bs(A,B)

        # Since the index of array starts from 0
        # we need to add 1 to get the ans
        return idx + 1
