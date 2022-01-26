"""
Find shortest unique prefix to represent each word in the list.
"""

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        
        # Pretty simple, try dry running it once on paper, you will
        # understand the logic
        prefix_dict = {}
        for word in A:
            for i in range(len(word)):
                if word[:i] not in prefix_dict:
                    prefix_dict[word[:i]] = 1
                else:
                    prefix_dict[word[:i]] += 1
        res = []
        for word in A:
            prefix = word
            for i in range(len(word)):
                curr_pref = word[:i]
                if prefix_dict[curr_pref]==1:
                    prefix = curr_pref
                    break
            res.append(prefix)               
        return res