"""
Input Format

The only argument given is string A.
Output Format

Return an integer which is the integer verison of roman numeral string.
For Example

Input 1:
    A = "XIV"
Output 1:
    14
"""

class Solution:
	# @param A : string
	# @return an integer
	def romanToInt(self, A):
        dec_num = [1, 4, 5, 9, 10, 40, 50, 90, 100,400,500,900,1000]
	    	roman_num = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        should_check = ["I","X","C"]
        next_should = ["IV","IX","XL","XC","CD","CM"]

        num = 0
        i = 0
 
        while i < len(A):
            curr_char = A[i]
 
            if curr_char in should_check:
                n_cc = A[i:i+2]
                if n_cc in next_should:
                    idx = roman_num.index(n_cc)
                    num += dec_num[idx]
                    i += 2
                    continue
            
            idx = roman_num.index(curr_char)
            num += dec_num[idx]
            i+=1

        return num
