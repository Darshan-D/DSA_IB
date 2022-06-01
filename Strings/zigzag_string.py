"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R
And then read line by line: PAHNAPLSIIGYIR

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
"""

class Solution:
# @param A : string
# @param B : integer
# @return a strings
    def convert(self, A, B):
        if B==1 or B==0:
            return A
        idx=range(B)
        ans=''
        for i in idx:
            even=0
            jmpidx=i
            while jmpidx<len(A):
                ans+=A[jmpidx]
                if i==0:
                    #even wale upar jaate h and odd wale neeche
                    jmpidx+=(B-i-1)+(B-i-2)+1
                elif i==B-1:
                    jmpidx+=(B-1)+(B-2)+1
                else:
                    if even:
                        jmpidx+=(i+(i-1)+1)
                        even=0
                    else:
                        jmpidx+=((B-i-1)+(B-i-2)+1)
                        even=1
        return ans     
