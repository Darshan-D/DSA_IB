"""
Given a string A and integer B, remove all consecutive same characters that have length exactly B.
"""

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        if len(A) < 1:
            return A
            
        if len(A) < B:
            return A
            
        new_str = A
        st_i = 0
        c = 1
        prev_c = A[0]
        
        for curr_i in range(1, len(A)):
            if A[curr_i] == prev_c:
                c += 1
                end_i = curr_i
            else:
                st_i = curr_i
                c = 1
                prev_c = A[curr_i]
            if c == B:
                rm_c = A[end_i]
                
                # Will fail for test case
                #a = abcaa, b = 2
                new_str = new_str.replace(rm_c, "")
                
        return new_str
        
