"""
Input Format

The only argument given is integer A.
Output Format

Return a string denoting roman numeral version of A.
Constraints

1 <= A <= 3999
For Example

Input 1:
    A = 5
Output 1:
    "V"

Input 2:
    A = 14
Output 2:
    "XIV"
"""


class Solution:
	# @param A : integer
	# @return a strings
	def intToRoman(self, A):
		dec_num = [1, 4, 5, 9, 10, 40, 50, 90, 100,400,500,900,1000]
		roman_num = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]

		curr_ans = ""
		rem_num = A
		while rem_num != 0:
			for i in range(len(dec_num)-1,-1,-1):
				dec = dec_num[i]
				if rem_num - dec > -1:
					rem_num -= dec
					curr_ans += roman_num[i]
					break
			
		return curr_ans
