"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
"""



# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):

        # If there are no existing intervals
        if len(intervals) == 0:
            return [newInterval]
            
        # Add the current interval in the final ans
        result = []
        result.append(newInterval)
        
        # Check if the intervals overlap
        for i in range(0,len(intervals)):
        
            a = result.pop()
            b = intervals[i]

            # New interval starts after the end of current interval
            if a.start > b.end:
                result.append(b)
                result.append(a)

            # New interval starts before the start of current interval
            elif a.end < b.start:
                result.append(a)
                result.append(b)

            # In the case when they overlap
            else:
                # Start should be the minimum of both intervals
                start = min(a.start, b.start)

                # End should be the maximum of both intervals
                end = max(a.end, b.end)

                # Add the new interval with updated start and end in the result list
                result.append(Interval(start, end))
            
        return result