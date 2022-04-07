"""
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

Example

Input : 4
Output : True  
as 2^2 = 4. 
"""

"""
log video - https://youtu.be/vOEWH8BrPSw
watch the log wala video and usmae yeh logic use kiya h
1. sabko log form mae le liya, usse, yeh equation aise convert ho gayi A**P = N --> PlogA = logN --> P=(logN)/(logA)
2. logA pe iterate karte jao till sqrt(N) [sqrt tak issliye sqrt se aage jayege toh power 1 ya 1 se chota ho jayega]
3. harr ek baar logA ke itereation pe P ke value nikalo
4. uss nikali hui value ko check karo if A**P == 1 ha ya nahi, if hai toh return True(1), else return (0)
"""

class Solution:
	# @param A : integer
	# @return an integer
	def isPower(self, A):
        for i in range(1, int(A**(1/2))+1):
            for j in range(1, int(A**(1/2))+1):
                if i**j == A:
                    return 1
                if i**j > A:
                    break

        return 0
