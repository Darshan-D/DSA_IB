"""
You are given two positive numbers A and B. You need to find the maximum valued integer X such that:

X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1
For example,

A = 30
B = 12
We return
X = 5
"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        def gcd(A,B):
            if B == 0:
                return A
            else:
                return gcd(B, A%B)
                
        if gcd(A,B)==1:
            return A
        else:
            return self.cpFact(A//gcd(A,B),B)
