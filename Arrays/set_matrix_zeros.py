"""
Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.
"""
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, a):
        m,n = len(a), len(a[0])

        # To track the col and row which we have set to 0
        j_done = set()
        i_done = set()
        add_i = False
    
        for i in range(m):
            for j in range(n):
                # Note row/col of every ele which is 0
                if a[i][j] == 0:
                    j_done.add(j)
                    i_done.add(i)
                  
        for i in range(m):
            for j in range(n):
                # While going over it again, if we are in the row/col which had 0,
                # set that element to 0
                if j in j_done or i in i_done:
                    a[i][j] = 0
    
        return a
        
