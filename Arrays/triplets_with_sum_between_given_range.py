class Solution:
    def solve(self, A):
        # Take the first three numbers as triplets
        a, b, c = float(A[0]), float(A[1]), float(A[2])
        
        # Start iterating from the fourth element
        for i in range(3, len(A)):

            # If the current triplet satisfies the req cond
            if 2 > a + b + c > 1:
                return 1

            # If the sum is greater than 2, then replace the biggest
            # element from the triplet, with current element
            elif a + b + c > 2:
                x = max(a, b, c)
                if a == x:
                    a = float(A[i])
                elif b == x:
                    b = float(A[i])
                else:
                    c = float(A[i])

            # If the sum is less than 1, then replace the smallest
            # element from the triplet, with current element
            else:
                x = min(a, b, c)
                if x == a:
                    a = float(A[i])
                elif x == b:
                    b = float(A[i])
                else:
                    c = float(A[i])

        # Updates made in the last iteration needs to be checked
        if 2 > a + b + c > 1:
            return 1
        return 0
