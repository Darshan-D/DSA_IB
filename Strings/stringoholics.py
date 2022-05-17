"""
You are given an array A consisting of strings made up of the letters 'a' and 'b' only.
Each string goes through a number of operations, where:

1.  At time 1, you circularly rotate each string by 1 letter.
2.  At time 2, you circularly rotate the new rotated strings by 2 letters.
3.  At time 3, you circularly rotate the new rotated strings by 3 letters.
4.  At time i, you circularly rotate the new rotated strings by i % length(string) letters.


Eg: String is "abaa"




 At time 1, string is "baaa", as 1 letter is circularly rotated to the back

 At time 2, string is "aaba", as 2 letters of the string "baaa" is circularly rotated to the back

 At time 3, string is "aaab", as 3 letters of the string "aaba" is circularly rotated to the back

 At time 4, string is again "aaab", as 4 letters of the string "aaab" is circularly rotated to the back

 At time 5, string is "aaba", as 1 letters of the string "aaab" is circularly rotated to the back
After some units of time, a string becomes equal to its original self.
Once a string becomes equal to itself, it's letters start to rotate from the first letter again (process resets). So, if a string takes t time to get back to the original, at time t+1 one letter will be rotated and the string will be its original self at 2t time.
You have to find the minimum time, where maximum number of strings are equal to their original self.
As this time can be very large, give the answer modulo 109+7.
"""

from fractions import gcd

def lcm(x, y):
    return x * y // gcd(x, y)
    
class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        arr=[]
        for i in range(len(A)):
            if A[i]=='a'*len(A[i]) or A[i]=='b'*len(A[i]):
                arr.append(1)
            else:
                j=1
                while(True):
                    if ((j*(j+1))/2)%len(A[i])==0:
                        arr.append(j)
                        break
                    j+=1
        
        ans=arr[0]
        for i in range(1,len(arr)):
            ans=lcm(ans,arr[i])    
        return ans%(1000000000+7)
