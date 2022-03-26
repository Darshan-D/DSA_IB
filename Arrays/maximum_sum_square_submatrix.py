"""
Given a 2D integer matrix A of size N x N find a B x B submatrix where B<= N and B>= 1, such that sum of all the elements in submatrix is maximum.
"""

"""
The basic idea of solving this is

From the original matrix we will start adding every B elements in each row and store it in the add_mat
add_mat will have dimensions (len(A) x (len(A) - B + 1)) .. (rows x cols)

We will Populate the add_mat using the approach mentioned above (line 4)
Now we have the sum of all the colums of all the possible BxB matrix

We will take the transpose of add_mat_t to use the same logica as in line 4 to get the sum of all possible cols
From the add_mat_t we will start adding every B elements in each row and check if its greater than mx_sm
if so update it!

at last return mx_sm
"""
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        # This is the maximum sum, which we will return at last
        mx_sm = float('-infinity')

        row = len(A)
        col = row - B + 1
        add_mat = [[0 for i in range (col)] for j in range (row)]

        # Populate the add_mat matrix
        # We will start adding every B elements in each row and store it in the add_mat
        i = 0           # To take care of the rows
        j = 0           # To take care of the cols
        col_s = 0       # It will give starting index of the col to add
        col_e = B - 1   # It will give ending index of the col to add
        

        # Iterate through each row
        while i < row:
            # Iterate through each col
            while j < col:

                # Take the sum of every B elements
                curr_sm = sum(A[i][col_s:col_e+1])

                # Store the sum in add_mat
                add_mat[i][j] = curr_sm
                col_s += 1
                col_e += 1
                j += 1

            j = 0
            col_s = 0
            col_e = B - 1
            i+=1

        # Take the transpose of add_mat so we can use the same logic as above
        # to sum up the elements
        add_mat_t = [[0 for i in range(row)] for j in range(col)]

        for i in range(len(add_mat)):
            for j in range(len(add_mat[0])):
                add_mat_t[j][i] = add_mat[i][j]

        # Extract the ans
        # Start adding every B elements in add_mat_t and store the maximum sm  
        i = 0           # To take care of row
        j = 0           # To take care of col
        col_s = 0       # It will give starting index of the col to add
        col_e = B - 1   # It will give ending index of the col to add

        # Same logic as previous while loop
        while i < len(add_mat_t):
            while j<len(A) - B + 1:
                curr_sm = sum(add_mat_t[i][col_s:col_e+1])

                if curr_sm > mx_sm:
                    mx_sm = curr_sm

                j+=1
                col_s += 1
                col_e += 1

            j = 0
            col_s = 0
            col_e = B - 1
            i += 1

        return mx_sm
