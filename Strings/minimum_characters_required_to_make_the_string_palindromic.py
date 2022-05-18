"""
Given an string A. The only operation allowed is to insert  characters in the beginning of the string.

Find how many minimum characters are needed to be inserted to make the string a palindrome string.
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        left = 0
        right  = len(A)-1
        ans = 0
        while(left<right):
            print("---")
            print(A[left], A[right], ans)
            print(left, right)
            if (A[left] == A[right]):
                print("equal")
                left = left+1
                right = right-1
            elif (left == 0):
                print("left = 0")
                ans = ans+1
                right = right-1
            else:
                print("else part")
                ans = ans+left
                left = 0
        return ans
