"""
Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:

A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index).
"""

class Solution:
	# @param A : string
	# @return a strings
	def longestPalindrome(self, A):
        s = A
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            
            # For odd palindromes -- assuming this as the middle, we'll expand later on towards left and right
            l, r = i,i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                # if its bigger than the current palindrome
                if r - l + 1 > resLen:
                    res = s[l: r+1]
                    resLen = r - l + 1

                # Expanding towards left and right
                l -= 1
                r += 1
                
                
            # For even palindromes
            l, r = i, i+1
            
            while l>= 0 and r < len(s) and s[l] == s[r]:
                
                # if its bigger than current palindrome
                if r - l + 1 > resLen:
                    res = s[l: r+1]
                    resLen = r - l + 1
                    
                l -= 1
                r += 1
                
        return res
