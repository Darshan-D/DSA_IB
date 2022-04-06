"""
Given four positive integers A, B, C, D, determine if there’s a rectangle such that the lengths of its sides are A, B, C and D (in any order).

If any such rectangle exist return 1 else return 0.
"""

# Function to check if the given 
# integers value make a rectangle 
def isRectangle(a, b, c, d): 
      
    # Square is also a rectangle 
    if a == b == c == d: 
        return True
          
    elif a == b and c == d: 
        return True
          
    elif a == d and c == b: 
        return True
          
    elif a == c and d == b: 
        return True
          
    return False
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        if(isRectangle(A,B,C,D)==True):
            return 1
        return 0
