"""
Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.

NOTE:

A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.
"""

def binarySearch(Arr,target) :
    start, end = 0, len(Arr)-1
    while start <= end :
        mid = (start + end) // 2
        if Arr[mid] == target :
            return mid
        elif Arr[mid] < target :
            start = mid + 1
        else :
            end = mid - 1;
    return -1

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        start=0
        end=len(A)-1

        while start<end:
            mid=(start+end)//2
            if A[mid-1]<A[mid] and A[mid]<A[mid+1]:
                start=mid+1
            elif A[mid-1]>A[mid] and A[mid]>A[mid+1]:
                end=mid-1
            else:
                break
                
        A1=A[:mid+1]
        A2=A[mid+1:][::-1]
        a=binarySearch(A1,B)
        if a!=-1:
            return a
        a=binarySearch(A2,B)
        if a!=-1:
            return len(A)-1-a
        return -1