"""
Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        # O(N*N) time complexity
        # Dict with index pairs of every unique sum (key is sum, values are indexes)
        pairsSum={}
        equals=[]

        for i in range(len(A)):
            for j in range(i+1,len(A)):
                s=A[i]+A[j]
                if s in pairsSum:
                    # Only append unique pairs
                    if i not in pairsSum[s][-1] and j not in pairsSum[s][-1]:
                        pairsSum[s].append([i,j])
                else:
                    pairsSum[s]=[[i,j]]

                # Only append indexes when length of indexes reach 2
                # 3rd or 4th will not be lexicographically smaller, so ignore
                if len(pairsSum[s])==2:
                    equals.append(pairsSum[s][0]+pairsSum[s][1])
                    
        equals=sorted(equals)
        return equals[0]