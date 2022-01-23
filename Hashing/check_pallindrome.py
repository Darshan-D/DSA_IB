"""
Given a string A consisting of lowercase characters.

Check if characters of the given string can be rearranged to form a palindrome.

Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.
"""


# O(N) time and space complexity
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # Make hash_map to count freq of each character
        hash_map = {}
        for c in A:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1

        if len(A)%2 != 0:
            odd = True
        else:
            odd = False

        odd_characters = 0

        # Each character can appear even number of times
        # and atmost 1 character can appear odd number of times (provided len of original string is odd)
        for key in hash_map:
            if hash_map[key] % 2 == 0:
                continue
            else:
                odd_characters += 1

        if odd_characters > 1:
            return 0
        elif odd_characters == 1 and odd:
            return 1
        elif odd_characters == 1 and not odd:
            return 0
        elif odd_characters == 0 and odd:
            return 0
        elif odd_characters == 0 and not odd:
            return 1