"""

Problem: You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.

f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

---

Main Crux:

Here we have f(i, j) = |A[i] - A[j]| + |i-j|

The 4 possible cases here are:

Case 1:

i>j and A[i] > A[j]:

f(i,j) can be rewritten as: (A[i]+i) - (A[j]+j)

Case 2:

i<j and A[i] < A[j]:

f(i,j) can be rewritten as: (A[j]+j) - (A[i]+i)

Case 3:

i<j and A[i] > A[j]:

f(i,j) can be rewritten as: (A[i] - i) - (A[j] - j)

Case 4:

i>j and A[i] < A[j]:

f(i,j) can be rewritten as: (A[j] - j) - (A[i] - i)

The 4 noticeable things to compute here are:

1. Maximum1 = max(A[i]+i)

2. Minimum1 = min(A[i]+i)

3. Maximum2 = max(A[i]-i)

4. Minimum2 = min(A[i]-i)

The function needs to return max(Maximum1 - Minimum1, Maximum2 - Minimum2)

Because this would go through all the possible cases, find the highest value of the function and return the best values for (A[i]+i) and (A[i]-i), and the max of these 2 would be the answe

"""

class Solution:

    # @param A : list of integers

    # @return an integer

    def maxArr(self, A):

        # Intialize as INT_MAX and INT_MIN

        max1 = -2147483648

        min1 = +2147483647

        max2 = -2147483648

        min2 = +2147483647

    

        for i in range(len(A)):

            # Updating max and min variables

            # as described in algorithm.

            max1 = max(max1, A[i] + i)

            min1 = min(min1, A[i] + i)

            max2 = max(max2, A[i] - i)

            min2 = min(min2, A[i] - i)

        

    

        # Calculating maximum absolute difference.

        return max(max1 - min1, max2 - min2)
