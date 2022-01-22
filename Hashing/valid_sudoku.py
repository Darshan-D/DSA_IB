"""
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

---
CRUX of the problem:
There should not be any repeated elemets within a row and col and within the 9 sub boxes
So simply use hash_map/set to take care of repeated digits 
"""

class Solution:
	# @param A : tuple of strings
	# @return an integer
	def isValidSudoku(self, A):
 
        # Check row wise for repetiton
        # We are also taking care of repetiton in sub boxes here
        # As soon as we get repeated ele we return 0
        for j,row in enumerate(A):
            row_map ={}

            # Since we are travelling horizonatally, at a time, we can fill
            # values in 3 sub boxes, and we reset them after every 3 iterations
            # reseting them after 3 iterations cause height of subboxes are 3
            if j%3 == 0:
                table_A = {}
                table_B = {}
                table_C = {}

            for i,num in enumerate(row):
                if num == ".":
                    continue
                elif num in row_map:
                    return 0
                else:
                    row_map[num] = 1

                # subox 1 Check
                if -1<i<3:
                    if num in table_A:
                        return 0
                    else:
                        table_A[num] = 1

                # subox 2 Check
                if 2<i<6:
                    if num in table_B:
                        return 0
                    else:
                        table_B[num] = 1

                # subox 3 Check
                if 5<i<9:
                    if num in table_C:
                        return 0
                    else:
                        table_C[num] = 1


        # Check column wise for repetiton
        for i in range(9):

            col_map = {}
            
            for j in range(9):
                num = A[j][i]
            
                if num == ".":
                    continue
                elif num in col_map:
                    return 0
                else:
                    col_map[num] = 1

        return 1