"""
Given a string A consisting of lowercase characters.

We need to tell minimum characters to be appended (insertion at end) to make the string A a palindrome.
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        '''
        The plan
        1. Start iterating from the end of the string, add one character to the current string at the end of every iteration
        2. Check if the current string is a palindrome
            2a. If it is, then the number of characters to be appended is len(tot_string) - len(curr_string)
            2b. If its not, add another character to the curr string and check again
        '''

        A_rev = A[::-1]

        # Base Case - Already a palindrome
        if A == A_rev:
            return 0

        n = len(A)
        i = n-1
        j=0
        curr_string = ""
        palindrome_check = ""
        ans = float("inf")
        #print(A, A_rev)
        while i>=0:
            curr_string = A[i] + curr_string
            palindrome_check += A_rev[j]
            #print(curr_string, palindrome_check)
            
            # Check if the curr_string is a pallindrome
            if curr_string == palindrome_check:
                to_be_appended = n - len(curr_string)
                if to_be_appended < ans:
                    ans = to_be_appended
            
            i-=1
            j+=1

        return ans
