"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified. You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

Pad extra spaces ' ' when necessary so that each line has exactly L characters. Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. For the last line of text, it should be left justified and no extra space is inserted between words.

Your program should return a list of strings, where each string represents a single line.

Example:

words: ["This", "is", "an", "example", "of", "text", "justification."]


L: 16.



Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Note: Each word is guaranteed not to exceed L in length. 
"""

class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        if A==[]:
            return ""
            
        ret = []
        string = ""
        A.append("")
        j=0
        for i in A:
            i = i.strip()
            if i == "" or len(i)+len(string)>=B:
                string = string.strip()
                length_of_string = len(string)-j+1
                num_of_spaces = j-1
                extra_space = B - length_of_string
                string = string.split()
                if num_of_spaces != 0:
                    spaces = extra_space//num_of_spaces
                    remainder_space = extra_space%num_of_spaces
                    k = 0
                    while(remainder_space>0):
                        string[k] = string[k]+" "
                        remainder_space -= 1
                        k+=1
                    string = (" "*spaces).join(string)
                else:
                    spaces = extra_space
                    string = " ".join(string)
                    string += " "*spaces
                    remainder_space = 0
                ret.append(string)
                string = i
                j=1
            else:
                string += " "+i
                string = string.strip()
                j+=1
        ret[-1] = " ".join(ret[-1].split())
        ret[-1] += " "*(B - len(ret[-1]))
        if ret[0]=="":
            ret = ret[1:]
        return (ret)
