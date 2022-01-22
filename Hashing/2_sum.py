"""
Problem Description

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based. Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer`Preformatted text`
    # @return a list of integers
    def twoSum(self, A, B):
        # Store the values in hash_map
        hash_map = {}

        # represent the first and second index which sums upto target
        st = 0
        ed = 0

        for i,num in enumerate(A):
            # since a+b=t so a=b-t
            # so if we found b-t, we have got the req ans
            if B-num in hash_map:
                    st = hash_map[B-num] + 1
                    ed = i + 1
                    return [st, ed]
    
            elif num not in hash_map:
                hash_map[num] = i

        # No ans found ret empty arr
        return []
