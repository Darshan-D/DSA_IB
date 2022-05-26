"""
Given a string A.

Return the string A after reversing the string word by word.

Input 1:
    A = "the sky is blue"
Output 1:
    "blue is sky the"

Input 2:
    A = "this is ib"
Output 2:
    "ib is this"
"""
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        word_list = []
        ms = ""
        word = ""
        check = False
        
        for i in range(len(A)):
            if A[i] != " ":
                word+=A[i]
                check = True
                
            elif A[i] == " " and i!= len(A) - 1 and A[i+1] == " ":
                continue
        
            elif A[i] == " " and check:
                word_list.append(word)
                word = ""
            
        if len(word) > 0:
            word_list.append(word)
        
        for i in range(len(word_list)-1, -1, -1):
            if i == 0:
                ms += word_list[i]
            else:
                ms += word_list[i] + " "
            
        return ms
