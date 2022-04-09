"""
Determine whether an integer is a palindrome. Do this without extra space.
A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed. Negative numbers are not palindromic.
"""

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        
        og_num = A
        new_num = 0
        
        while(A>0):
            rev = A%10
            A = A//10
            new_num = new_num * 10 + rev
        
        if new_num == og_num:
            return 1
        else:
            return 0
