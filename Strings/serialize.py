"""
You are given an array A of strings and we have to serialize it and return the serialized string.

Serialization: Scan each element in a string, calculate its length and append it with a string and a element separator or deliminator (the deliminator is ~). We append the length of the string so that we know the length of each element.

For example, for a string 'interviewbit', its serialized version would be 'interviewbit12~'.
"""

class Solution:
    # @param A : list of strings
    # @return a strings
    def serialize(self, A):
        ans = ""
        for word in A:
            n = len(word)
            ans+=word+str(n)+"~"

        return ans
