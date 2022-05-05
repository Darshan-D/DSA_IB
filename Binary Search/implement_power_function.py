"""
Implement pow(x, n) % d.
In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative. In other words, make sure the answer you return is non negative.
"""

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        
        if x==0:
            return 0
        elif x==1:
            return 1
        elif n==0:
            return 1
            
        elif n%2 == 0:
            np = n//2
            ans = self.pow(x, np, d)
            return (ans*ans)%d
        else:
            np = (n-1)//2
            ans = self.pow(x, np, d)
            return (ans*ans*x)%d
