"""
Given a numeric string A representing a large number you need to find the next smallest palindrome greater than this number.
"""

'''
Simple Funda
1. Make the string palindrome, using L and R pointer, run them till L>R or R<L
2. Check if the palindromic string is greater than og string --> if so return that
3. Take the middle of the string and increase the number
3a.     If the middle number is 9, make it 0 and increase the next and prev number by 1 (prev number is also increased to keep it a palindrome)
3aa.        if there are no next and prev number insert 1 at idx 0 and make the last number as 1
'''

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        # Handle the nine situation
        def handle_nines(num_list, L, R):
            #  If both L and R poining at the same pos
            if L == R:
                # Make that 0, since its 9
                num_list[L] = 0

                # Check if the prev and next number are within the limits
                if L - 1 >= 0 and L + 1 <= len(num_list) - 1:
                    # If the prev number is also 9, call this same function with ptrs L-1, L+1
                    # Increasing the ptrs is the reason below else condition is not hit
                    if num_list[L-1] == 9:
                        num_list = handle_nines(num_list, L-1, L+1)
                        return num_list

                    # If they are not 9, simply increase them by 1
                    else:
                        num_list[L-1] += 1
                        num_list[L+1] += 1
                        return num_list
                
                # This case is not hit, check line 25 for the reason
                else:
                    print("out bounds L==R 9")

            # If L and R are pointing at different position
            else:

                # Since they are 9, make them 0
                num_list[L] = 0
                num_list[R] = 0

                # Check if their previous and next idx are within the limits
                if L-1 >= 0 and R + 1 <= len(num_list) - 1:
                    # If the prev number is also 9, call this same function with ptrs L-1, R+1
                    if num_list[L-1] == 9:
                        num_list = handle_nines(num_list, L-1, R+1)
                        return num_list

                    # If they are not 9, simply increase them
                    else:
                        num_list[L-1] += 1
                        num_list[R+1] += 1
                        return num_list

                # If they are out of bounds, add '1' at idx '0' and make the last elemet as 1
                else:
                    if L-1 == -1 and R+1 == len(num_list):
                        num_list.insert(0,1)
                        num_list[-1] = 1
                        return num_list

                    # This else wont be hit, just for sanity check, you can try with different cases
                    # Most of the code will get terminated when we append 1 at the begging and make
                    # the last idx val as 1
                    else:
                        print("out of bounds L!=R 99", L, R, num_list)

        og_num = A

        # Convert num to list inorder to do manipulations
        num_list = [int(i) for i in A]

        # EDGE CASES
        if len(num_list) < 2:
            if num_list[0] < 9:
                return str(num_list[0]+1)
            else:
                return '11'
        
        # Start by making the list a pallindrome
        L = 0
        R = len(num_list) - 1
        while L <= R and R >= L:
            num_list[R] = num_list[L]
            L += 1
            R -= 1

        # Convert list to str
        new_num = "".join(str(e) for e in num_list)

        # Check if the the new_num > og_num
        if int(new_num) > int(og_num):
            return new_num

        # If not, make the pointers go back to their last valid 
        # state before the loop terminated
        else:
            L -= 1
            R += 1

            # Keep on doing this while new_num <= og_num
            while int(new_num) <= int(og_num):

                # If both ptrs are pointing at the same thing increase by 1
                if L == R:
                    # If its 9, we need to handle the nines
                    if num_list[L] == 9:
                        num_list = handle_nines(num_list, L, R)
                    
                    # Else increase it
                    else:
                        num_list[L] += 1
                
                # If they are pointing at different position
                else:
                    # If either of those ptrs are 9, we need to handle the nines
                    if num_list[L] == 9 or num_list[R] == 9:
                        num_list = handle_nines(num_list, L, R)
                    
                    # Else increase it
                    else:
                        num_list[L] += 1
                        num_list[R] += 1

                new_num = "".join(str(e) for e in num_list)

            return new_num
