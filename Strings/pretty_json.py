"""
Given a string A representating json object. Return an array of string denoting json object with proper indentaion.

Rules for proper indentaion:

Every inner brace should increase one indentation to the following lines.
Every close brace should decrease one indentation to the same line and the following lines.
The indents can be increased with an additional ‘\t’
Note:

[] and {} are only acceptable braces in this case.

Assume for this problem that space characters can be done away with.
"""

class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        json = A
        result = []
        multiplier = 0
        i = 0
        
        while i < len(json):
            if json[i] in ['{', '[']:
                result.append('\t' * multiplier + json[i])
                multiplier += 1
                i += 1
            elif json[i] in ['}', ']']:
                multiplier -= 1
                result.append('\t' * multiplier + json[i])
                i += 1
            elif json[i] == ',':
                result[-1]+= ','
                i += 1
            else:
                start = i
                while i < len(json) and json[i] not in ['{', '}', ',', '[', ']']:
                    i += 1
                curr_s = json[start:i]
                result.append('\t' * multiplier + curr_s)
        
        return result
