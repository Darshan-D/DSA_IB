"""
You are given an array of N integers, A1, A2 ,..., AN and an integer B. Return the of count of distinct numbers in all windows of size B.

Formally, return an array of size N-B+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

NOTE:  if B > N, return an empty array.
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        n = len(A)

        if B > n:
            return []
        
        # dic will store all the elements in the curr window along with its number of occurence
        # and store them as key value pairs
        dic = {}

        # dic will always hold values such that their counts sum up to B
        res = []
        for i in range(n):
            # insert the curr ele in the dic
            if A[i] not in dic:
                dic[A[i]] = 1

            # if its already present update, its count
            else:
                dic[A[i]] += 1
                
            # after the first window we start to remove from dic
            if i >= B:
                
                # Goto the element which will be removed from the window
                # Check if its occurence in the curr window

                # If it was 1, then delete it
                if dic[A[i - B]] == 1:
                    del dic[A[i - B]]

                # Else reduce it by 1
                else: 
                    dic[A[i - B]] -= 1

            # after the first window we start to append to result
            if i + 1 >= B:
                res.append(len(dic))

        return res