"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.
"""

class Solution:
    # @param numerator : integer
    # @param denominator : integer
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        n = numerator
        d = denominator
        if n % d == 0:
            return str(n//d)
        # Deal with negatives
        if (abs(n)/n) * (abs(d)/d) < 0:
            res = '-'
            n = abs(n)
            d = abs(d)
        else:
            res = ''
        # Integer part
        res = res + str(n//d) + '.'
        n = n % d
        # Start point of the "list"
        frem = n
        srem = n
        firstTime = True
        while frem != 0 and not (firstTime == False and frem == srem):
            firstTime = False
            srem = (srem * 10) % d
            frem = (frem * 10) % d
            if frem:
                frem = (frem * 10) % d
        # The fast pointer encounters a remainder of 0, so no cycle in the "list"
        if frem == 0:
            res += str((n * 10) // d)
            rem = (n * 10) % d
            while rem:
                res += str((rem * 10) // d)
                rem = (rem * 10) % d
            return res
        else:
            # Find the start point of the cycle, meanwhile, generate the non recurring part
            srem = n
            while frem != srem:
                res += str((srem * 10) // d)
                srem = (srem * 10) % d
                frem = (frem * 10) % d
            res += '('
            # Generate the recurring part
            firstTime = True
            while not (firstTime == False and srem == frem):
                firstTime = False
                res += str((srem * 10) // d)
                srem = (srem * 10) % d
            res += ')'
            return res