"""
Given a string A with lowercase english alphabets and you have to return a string in which, with each character its frequency is written in adjacent.
"""

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        hash_map = {}
        for c in A:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1

        ans = ""

        for c in A:

            if c in hash_map:
                ans += c + str(hash_map[c])
                hash_map.pop(c)

        return ans
