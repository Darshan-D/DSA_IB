class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        for target in A:
            count = 0
            for num in A:
                if num==target:
                    count += 1
                elif num > target:
                    if (num-B)^target != 0:
                        break
                    else:
                        count += 1
                        
                elif num < target:
                    if (num+B)^target != 0:
                        break
                    else:
                        count += 1
                        
            if count == n:
                return 1
                
        return 0
                    
                    
