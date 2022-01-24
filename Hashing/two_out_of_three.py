"""
Given are Three arrays A, B and C.

Return the sorted list of numbers that are present in atleast 2 out of the 3 arrays.
"""


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        A = set(A)
        B = set(B)
        C = set(C)
        ans = set()

        max_len = max(len(A), len(B), len(C))
        if len(A) == max_len:
            big_set = A
            second_big = max(len(B), len(C))
            if len(B) == second_big:
                mid_set = B
                small_set = C
            else:
                mid_set = C
                small_set = B

        elif len(B) == max_len:
            big_set = B
            second_big = max(len(A), len(C))
            if len(A) == second_big:
                mid_set = A
                small_set = C
            else:
                mid_set = C
                small_set = A

        else:
            big_set = C
            second_big = max(len(B), len(A))
            if len(B) == second_big:
                mid_set = B
                small_set = A
            else:
                mid_set = A
                small_set = B

        for ele in big_set:
            if ele in small_set:
                ans.add(ele)
            elif ele in mid_set:
                ans.add(ele)

        for ele in mid_set:
            if ele in small_set:
                ans.add(ele)
        ans = list(ans)
        ans.sort()
        return ans