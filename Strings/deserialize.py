"""
You are given a string A which is a serialized string. You have to restore the original array of strings.

The string in the output array should only have lowercase english alphabets.

Serialization: Scan each element in a string, calculate its length and append it with a string and a element separator or deliminator (the deliminator is ~). We append the length of the string so that we know the length of each element.

For example, for a string 'interviewbit', its serialized version would be 'interviewbit12~'.
"""


class Solution:
    # @param A : string
    # @return a list of strings
    def deserialize(self, A):
        ans = []
        curr_str = ""
        string_started = False
        for c in A:
            if 96 < ord(c) < 123:
                curr_str+=c
                string_started = True

            elif string_started:
                ans.append(curr_str)
                curr_str = ""
                string_started = False

        if len(curr_str) > 1:
            ans.append(curr_str)

        #print(ans)
        return ans
