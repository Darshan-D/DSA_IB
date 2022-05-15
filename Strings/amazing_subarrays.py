"""
You are given a string S, and you have to find all the amazing substrings of S.

Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

Input

Only argument given is string S.
Output

Return a single integer X mod 10003, here X is number of Amazing Substrings in given string.
Constraints

1 <= length(S) <= 1e6
S can have special characters
Example

Input
    ABEC

Output
    6

Explanation
	Amazing substrings of given string are :
	1. A
	2. AB
	3. ABE
	4. ABEC
	5. E
	6. EC
	here number of substrings are 6 and 6 % 10003 = 6.
"""

'''
My Solution Approach: (Main crux is at pt 5)

1. Find all the indexes of vowels
2. Say for eg, string is ABEC, the indexes of vowels are [0,2]
3. Now the total number of substrings that can be made with vowel at index 0
   is len(string) - vowel string (its kind of obvious once you think about it)
4. For vowel_idx 0, the possible substrings are: A, AB, ABE, ABEC i.e 4-0=4
5. Basically, we once we found the vowel, we can keep adding one character and 
   make new string till we reach the end of the string. Repeat the same process
   for next vowel
'''


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
        vowel_idx = []
        for i,c in enumerate(A):
            if c in vowels:
                vowel_idx.append(i)

        total = 0
        N = len(A)
        for num in vowel_idx:
            total += N - num

        return total%10003
