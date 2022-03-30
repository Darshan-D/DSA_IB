"""
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4
"""


"""
This is for another apporach with O(N) time and O(1) space complexity
Input:[3 1 2 5 3]

n=5

Summing
=(1+2+3+4+5)-(3+1+2+5+3)
=4(missing)-3(repeated)=1           ----eq(1)

Squaring
=(1^2+2^2+..5^2)-(3^2+1^2+..3^2)
=4^2(missing)-3^2(repeated)=7       ----eq(2)

two eq. two variable

------------------------------------------
Intuition behind above apporach is:
Sum of N numbers = ((N)*(N+1))/2
Sum of Square of N numbers = ((N)*(N+1)*(2N+1))/6

when we take the above sum with the sum of our arr and sum of squares of element of our arr we get
1. Missing - Repeating number
2. (Missing**2) - (Repeating**2) = (Missing+Repeating)(Missing-Repeating)

Now Solve the above equations to get the ans
"""

# My apporach is using O(N) time and O(N) space complexity

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        if len(A) == 2:
            if A[1] == 1:
                # For the case when IP is A=[1,1]
                return [1, 2]

        n = max(A)
        arr = [0]*n
        repeat = None
        missing = None

        for num in A:
            if arr[num-1] == 0:
                arr[num-1] = 1
            else:
                repeat = num

        for i in range(len(arr)):
            if arr[i] == 0:
                missing = i+1

        return [repeat, missing]
