"""
Given a positive integer A, return its corresponding column title as appear in an Excel sheet.
"""

class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        s=''
        while(A):
            A=A-1# because we are adding int equivalent of A in next line i.e if n==1 next line will #print 'A'
            s=s+chr((A%26)+ord('A'))
            A=int(A/26)
        return(s[::-1])
            
            
            
            
            
