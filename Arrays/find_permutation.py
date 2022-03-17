"""
Given a positive integer n and a string s consisting only of letters D or I, you have to find any permutation of first n positive integer that satisfy the given input string.

D means the next number is smaller, while I means the next number is greater.

Notes

Length of given string s will always equal to n - 1
Your solution should run in linear time and space.
Example :

Input 1:

n = 3

s = ID

Return: [1, 3, 2]

"""

'''
Basic Idea ...

when n = 4 and s=IDI
arr = [1,2,3,4]
d_count = 1                 // total 'D's in the s
i_count = 4 - (4 - 1) + 1
        = 4 - 3 + 1
        = 2                 // start pointer for when we encounter 'I'

s_idx = d_count             // it will start our ans arr

current situation and pointers
arr = [1,2,3,4]
       | | |
       d s i                // d = d_count | s = s_idx | i = i_count

ans = [2,_,_,_]

now iterate through the string
if we encounter 'I', Append the element pointed by i_count and increase i_count
if we encounter 'D', Append the element pointed by d_count and decrease d_count

bazinga we solved it!!
'''

class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    
    def findPerm(self, A, B):
        s = A
        n = B
        arr = [i for i in range(1,n+1)]

        d_count = 0
        i_count = 0

        # Find the number of D's
        for c in s:
            if c == 'D':
                d_count += 1

        # i_count now points to the first element which we have to pick
        # incase we encounter I
        i_count = len(s) - (len(s) - d_count) + 1


        # Edge Case - 1
        # If there are no I, then we need to return arr in rev order
        if i_count == 0 or i_count > len(s):
            return arr[::-1]

        
        # Edge Case - 2
        # If there are no D, then we need to return arr in same order
        elif d_count == 0:
            return arr

        # Make an empty ans arr
        ans = [None for i in range(n)]
        
        # The s_idx is the index of first arr
        s_idx = d_count

        # d_count now points to the first element which we have to pick
        # incase we encounter D
        d_count -= 1

        i = 1
        j = 0

        # Append the element with the s_idx at the start of ans
        ans[0] = arr[s_idx]

        # Loop through the given string
        while i < n:
            # If I is encountered, add the element which is pointed by i_count
            # increase the i_count counter
            if s[j] == 'I':
                ans[i] = arr[i_count]
                i_count += 1

            # If D is encountered, add the element which is pointed by d_count
            # decrease the d_count counter
            elif s[j] == 'D':
                ans[i] = arr[d_count]
                d_count -= 1

            j+=1
            i+=1

        return ans  
