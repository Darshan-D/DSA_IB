"""
Given two binary strings, return their sum (also a binary string).
Example:

a = "100"


b = "11"
Return a + b = "111".
"""

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
      carry = 0
      res = ""
      if len(A) > len(B):
        l = len(A)
        B = ('0'*(l-len(B)) + B)
      else:
        l = len(B)
        A = ('0'*(l-len(A)) + A)

      for i in range(l-1, -1, -1):
        sum = int(A[i]) + int(B[i]) + carry
        if sum == 0 or sum == 1:
          res += str(sum)
          carry = 0

        elif sum == 2:
          carry = 1
          res += str(0)

        else:
          carry = 1
          res += str(1) 

      if carry == 1:
        res+=str(1)

      return res[::-1]
