"""
Given a sorted array A containing N integers both positive and negative.

You need to create another array containing the squares of all the elements in A and return it in non-decreasing order.

Try to this in O(N) time.
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
       
        n =len(A)
        # Initialize two pointers,
        # one at the start and one at the end
        i=0
        j=n-1
        res=[]
        while i<=j:
            # Append the square which is bigger
            # and increment its ptr
            if A[i]*A[i] >=A[j]*A[j]:
                res.append(A[i]*A[i])
                i+=1
            else:
              res.append(A[j]*A[j])
              j-=1
        
        # Since we need ans in ascending order,
        # return reversed array 
        return res[::-1]
