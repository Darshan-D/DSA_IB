"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
"""

def isvalid(A):
	for num in A.split('.'):
		if num == "" or len(num) > 3 or int(num) > 255 or int(num) < 0 or(len(num) - len(str(int(num))) > 0):
			return False;
	return True;


def generator(ans, A, pos, dots):
    if dots == 3:
        if isvalid(A):
            # print("appending",A)
        	ans.add(A)
    else:
    	for ind in range(pos, len(A)):
    		temp = A[:ind]+"."+A[ind:]
    		if isvalid('.'.join(temp.split('.')[:-1])):
		        generator(ans, temp, pos+2, dots+1)

            
class Solution:
	
	def restoreIpAddresses(self, A):
        ans = set()
        generator(ans, A, 1, 0)
        return sorted(ans)
