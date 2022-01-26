"""
Given two integer array A and B, you have to pick one element from each array such that their xor is maximum.

Return this maximum xor value.
"""

class  TrieNode:
    def __init__(self):
        self.children = {}
        self.leaf   = 0

class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def insert(self, x):

        root = self.root

        for i in range(31, -1, -1):
            
            index = self.check(x, i)
            if index not in root.children:
                root.children[index] = self.get_node()
            root = root.children.get(index)
        
        root.leaf = True

    def check(self, x, i):

        if( (x&(1<<i)) != 0 ):
            return True
        else:
            return False

    def findXor(self, x):
        
        root = self.root
        ans = 0

        for i in range(31, -1, -1):

            f = self.check(x, i)
            index = f^1
            if index not in root.children:
                root = root.children.get(index^1)
            else:
                ans = ans + (1 << i)
                root = root.children.get(index)
        
        return ans
    
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        global trie
        trie=Trie()
        ans=0
        for a in A:
            trie.insert(a)
        for b in B:
            ans=max(ans,trie.findXor(b))
        return ans