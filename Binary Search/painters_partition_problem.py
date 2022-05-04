"""
Given 2 integers A and B and an array of integars C of size N.

Element C[i] represents length of ith board.

You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters available and each of them takes B units of time to paint 1 unit of board.

Calculate and return minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of board.

2 painters cannot share a board to paint. That is to say, a board
cannot be painted partially by one painter, and partially by another.
A painter will only paint contiguous boards. Which means a
configuration where painter 1 paints board 1 and 3 but not 2 is
invalid.
Return the ans % 10000003
"""

class Solution:
	# @param A : integer - number of painters
	# @param B : integer - Time required to paint one borad
	# @param C : list of integers - Boards arr
	# @return an integer
	def paint(self, A, B, C):
		def possible(modi_fied_arr,  A, mid):
			painter = 1
			curr_time = 0
			for req_time in modi_fied_arr:
				if painter > A:
					return False
				
				if curr_time + req_time > mid:
					curr_time = req_time
					painter += 1
				
				else:
					curr_time += req_time
				
			return True


		modi_fied_arr = [i*B for i in C]
		
		low = max(modi_fied_arr)
		high = sum(modi_fied_arr)
		ans = 0
		
		while high>=low:
			mid = (high+low)//2

			if possible(modi_fied_arr, A, mid):
				ans = mid
				high = mid - 1
			else:
				low = mid + 1

		return ans%10000003
