"""
You are given a string, S, and a list of words, L, that are all of the same length.

Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

Example :

S: "barfoothefoobarman"
L: ["foo", "bar"]
You should return the indices: [0,9].
"""

class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        # Store all the strings of B in a map, along with their freq
        L = {}
        num_words = 0
        res = []

        for i in B:
            if L.get(i):
                L[i]+=1
            else:
                L[i]=1
            num_words += 1
        
        # We'll iterate through A, with step size equal to length of word(L)
        # and do a sub loop (with step size of L as well) and check if the word appears
        # in the map, if it does decrese the req count, else break out of the sub loop
        # if the count reaches 0, then we have found all the required words 
        i = 0
        j = len(B[0])-1
        temp_num = num_words
        temp_L = dict(L)

        while j<len(A):
            temp_i = i
            
            while j<len(A):
                if temp_L.get(A[i:j+1]) and temp_num>0:
                    temp_num -=1
                    temp_L[A[i:j+1]]-=1
                    i+=len(B[0])
                    j+=len(B[0])
                    if temp_num == 0:
                        res.append(temp_i)
                        break
                else:
                    break

            i = temp_i+1
            j = i+len(B[0])-1
            temp_num = num_words
            temp_L = dict(L)
        return res
