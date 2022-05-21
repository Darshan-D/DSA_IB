"""
Given a string A of parantheses  ‘(‘ or ‘)’.

The task is to find minimum number of parentheses ‘(‘ or ‘)’ (at any positions) we must add to make the resulting parentheses string valid.

An string is valid if:

Open brackets must be closed by the corresponding closing bracket.
Open brackets must be closed in the correct order.
"""
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack = []

        for c in A:
            if c == "(":
                stack.append("(")

            elif c == ")":
                # If there is nothing in the stack
                if len(stack) < 1:
                    stack.append(")")

                # If the last element in the stack is opening parent
                # then we found a pair and destroy them
                elif stack[-1] == "(":
                    stack.pop()

                # IF the last element in the stack is a closing parent
                # then we just add them, cant do much
                else:
                    stack.append(")")

        return len(stack)
