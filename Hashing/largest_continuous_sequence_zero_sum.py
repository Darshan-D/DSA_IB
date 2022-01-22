"""
Find the largest continuous sequence in a array which sums to zero.

Example:


Input:  {1 ,2 ,-2 ,4 ,-4}
Output: {2 ,-2 ,4 ,-4}
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers

    def lszero(self, A):
        # Map to store values
        # key: sum | value: index at which we got that sum
        mp = {0:-1}

        # Prefix sum
        s = 0
        start = end = 0
        
        for i in range(len(A)) :
            s += A[i]
            
            # If we had found this sum earlier
            # then it means all the elements after
            # that last index sum upto 0 till the current index
            # (watch ref video if you didn't get above pt)
            if s in mp :

                # Check if the length of current sub arr will be bigger
                if i - mp[s] > end - start :
                    start = mp[s]
                    end = i 
            
            # If not in hash_map then add it
            else :
                mp[s] = i
        
        # return the subarray based on indexes
        return A[start+1:end+1]