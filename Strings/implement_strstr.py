"""
Implement strStr().

strstr - locate a substring ( needle ) in a string ( haystack ).

"""
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        if len(A) == 1 and len(B) == 1:
            if A[0] == B[0]:
                return 0
            else:
                return -1
                
        if len(A) < 1 or len(B) < 1:
            return -1

                
        return A.find(B)
