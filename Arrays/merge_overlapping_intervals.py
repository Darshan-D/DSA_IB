"""
Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, I):
        res = []

	# Sort the intervals as per their starting pt
        I.sort(key=lambda i: i.start)
        for i in I:
            # If they do not overlap
	    if not res or res[-1].end < i.start:
                res.append(i)
	
            # If they overlap
            else:
                res[-1].end = max(res[-1].end, i.end)

        return res 
