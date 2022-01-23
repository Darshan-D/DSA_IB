"""
Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.

Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp'

Note:  All inputs will be in lower-case.

Example :

Input : cat dog god tca
Output : [[1, 4], [2, 3]]
"""

class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers

    # O(m*nlogn) Solution
    def anagrams(self, A):
        A = list(A)
        
        # Sort every string within the list
        for i in range(len(A)):
            A[i] = "".join(list(sorted(list(A[i]))))
        lmap = {}
        
        # Iterate through the list of strings
        # when encountered same string append the index
        for i in range(len(A)):
            if A[i] in lmap:
                lmap[A[i]].append(i+1)
            else:
                lmap[A[i]] = [i+1]

        # Return the values of dict (all the indices)
        return list(lmap.values())