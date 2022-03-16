"""
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.

If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.
"""

class Solution:
    def nextPermutation(self, A):
        n = len(A)
        ind = -1
        
        # Find the index from where we can turn around
        for i in range(0,n-1):
            if A[i]<A[i+1]:
                ind = i
                
        # If no such indx found, return the the arr in sorted form
        if ind == -1:
            return sorted(A)

        # Find the element from the remaming part which is greater than turn around ele
        # once found swap them
        for j in range(n-1,ind,-1):
            if A[j]>A[ind]:
                A[ind],A[j] = A[j],A[ind]
                break

        # Return the arr with the elements from turn around idx in reversed form 
        # This is done because we have to find the "next" permutation
        return A[:ind+1]+list(reversed(A[ind+1:]))


