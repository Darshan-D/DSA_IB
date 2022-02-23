"""
You are given a binary string A(i.e. with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised.

If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
"""
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):

        # Convert string to arr
        # put 1, when encoutered a 0, put -1 when encoutered 1
        # we do this since we want maximum 0s, and minumum 1s
        # this is due to the fact that we are going to flip elements
        # and make all the 0s as 1s, hence we need more 0s in og array
        arr = [1 if i == '0' else -1 for i in A]
        
        max_so_far = float('-inf')
        curr_max = 0
        res = []
        start = 0
        
        # simple kadane's algo
        for i in range(len(A)):
            curr_max += arr[i]
            
            if curr_max > max_so_far and curr_max >= 0:
                max_so_far = curr_max
                res = [start + 1, i + 1]

            if curr_max < 0:
                curr_max = 0
                start = i + 1
        
        return res
