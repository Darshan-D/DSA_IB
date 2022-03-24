"""
Given an unsorted integer array, find the first missing positive integer.
"""
class Solution:
    # @param a : list of integers
    # @return an integer
    def firstMissingPositive(self, a):
      for i in range(len(a)):
          v = a[i]
          
          while 0 < v < len(a)+1 and a[v-1] != v:
              tmp = a[v-1]
              a[v-1] = v
              v = tmp
              
      for i,x in enumerate(a):
          if x != i+1:
              return i+1
      return len(a)+1
       
