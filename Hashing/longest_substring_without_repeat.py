"""
Given a string,
find the length of the longest substring without repeating characters
"""

class Solution:
    # @param A : string
    # @return an integer

    def lengthOfLongestSubstring(self, A):
        # Sliding Window approach is used along with set, to
	    # track repeating ele
        st_i = 0
        ed_i = 0
        result = 0
        
        n = len(A)
        hash_set = set()
    
        while st_i < n and ed_i < n:
            # When encountered repeating element
    		# remove the element occuring at the
    		# start of the current window
            if A[ed_i] in hash_set:
                hash_set.remove(A[st_i])
                st_i += 1
                
            # Else keep on increasing the current window
            # and adding current elements to the set
            # as well as updating result
            else:
                hash_set.add(A[ed_i])
                ed_i += 1
                result = max(result, ed_i-st_i)
    
        return result
