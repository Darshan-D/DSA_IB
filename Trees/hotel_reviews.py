"""
Given a set of reviews provided by the customers for different hotels and a string containing Good Words, you need to sort the reviews in descending order according to their Goodness Value (Higher goodness value first). We define the Goodness Value of a string as the number of Good Words in that string.

NOTE: Sorting should be stable. If review i and review j have the same Goodness Value then their original order would be preserved.

You are expected to use Trie in an Interview for such problems

Example Input
Input 1:

 A = "cool_ice_wifi"
 B = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]


Example Output
Output 1:

 [2, 0, 1]


Example Explanation
Explanation 1:

 sorted reviews are ["cool_wifi_speed", "water_is_cool", "cold_ice_drink"]
"""

class TrieNode:
    def __init__(self, c = None):
        self.char = c
        self.childs = [None]*26
        self.complete = False


    def insert(self, root, word):
        for c in word:
            c_idx = ord(c) - ord('a')

            if root.childs[c_idx] is None:
                root.childs[c_idx] = TrieNode(c)
            
            root = root.childs[c_idx]

        root.complete = True


    def search(self, root, word):
        for c in word:
            c_idx = ord(c) - ord('a')

            if root.childs[c_idx] is None:
                return False
            
            elif root.childs[c_idx] is not None:
                root = root.childs[c_idx]


        if root.complete:
            return True
        else:
            return False


class Solution:
	# @param A : string
	# @param B : list of strings
	# @return a list of integers
	def solve(self, A, B):
        root = TrieNode()
        B = [line.split("_") for line in B]
        A = A.split("_")

        for cool_words in A:
            root.insert(root, cool_words)

        list_a = []
        for line in B:
            cool_words = 0
            for word in line:
                if root.search(root, word):
                    cool_words += 1

            s = " ".join(line)
            list_a.append((s, cool_words))

        list_a = sorted(list_a, key = lambda k : k[1], reverse = True)

        oldIndexes = {}
        B = [" ".join(word) for word in B]
        
        for i,line in enumerate(B):
            oldIndexes[line] = i

        ans = []
        for tuplee in list_a:
            
            line = tuplee[0]
            ans.append(oldIndexes[line])

        return ans