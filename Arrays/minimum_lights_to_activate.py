class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        def recurse(li, ui, curr_x, A, B, count):
            # Base conditions

            # Curr_x goes out of bounds --lower end
            if curr_x < 0:
                return -1

            # Curr_x goes out of bounds --upper end, and ui not satisfied
            elif curr_x >= len(A) and ui <= len(A) - 2:
                return -1

            # Curr_x goes out of bounds --upper end, ui satisfied
            elif curr_x >= len(A) and ui >= len(A):
                count += 1
                return count

            # All lights are on
            if ui >= len(A) and A[curr_x] == 1:
                count += 1
                return count

            # If curr_x cant be turned on,
            # check for the prev one
            if A[curr_x] == 0:
                curr_x -= 1
                new_li = curr_x - B + 1
                new_ui = curr_x + B - 1

                # new x's li and ui are greater than and less than 
                # curr li then its invalid else valid
                if new_li < li and new_ui > li:
                    li = new_li
                    return recurse(li, ui, curr_x, A, B, count)
                else:
                    return -1

            # If it can be turned on
            else:
                count += 1
                li = ui + 1
                curr_x = li + B - 1
                ui = curr_x + B - 1
                return recurse(li, ui, curr_x, A, B, count)

        # If B > len(A) then turning on
        # any one light will do the job
        if B > len(A):
            return 1

        # Else start with making the li as 0
        # find the curr_x as per li and B
        # find the ui as per curr_x
        # once found check if that light can be turned on
        # if it can update li = ui + 1, calculate new curr_x and ui accordingly
        # if it cant be turned on, check for prev curr_x
        li = 0
        curr_x = li + B - 1
        ui = curr_x + B - 1
        count = 0
        return recurse(li, ui, curr_x, A, B, count)