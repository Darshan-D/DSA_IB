"""
Given a string A consisting of lowercase characters.

You have to find the number of substrings in A which starts with vowel and end with consonants or vice-versa.

Return the count of substring modulo 109 + 7.
"""


"""
SOLUTION APPROACH

Example: “aba”

approach: Take the count of both vowel and consonants using a for loop.

now iterate over each char of string, whenever you find a vowel, the number of substrings that can be formed is equal to the number of consonants.so add count of consonants to answer. similarly, when you get consonants add the count of vowels to the answer.

explanation:

In “aba”, count of vowel=2, count of consonants=1,answer=0;

for iteration i=0, we found ‘a’, which is a vowel so we need consonant to make substring. here there is only one consonant so we will add 1 to the answer. and decrease the count of vowel by 1 as it is used.

count of vowel=1,count of consonants=1, answer=1;

for iteration i=1, we found ‘b’, which is consonant so add count of vowel to the answer. and decrease the count of consonants by 1;

count of vowel=1, count of consonants=0,answer=2;

for the last iteration, we will again get vowel but the answer remains the same as the count of consonants is 0,

so final answer is 2;

write code yourself!!
"""


class Solution:
    # @param A : string
    # @return an integer
    def isVowel(self, letter):
        set1 = {'a', 'e', 'o', 'i', 'u'}
        return (letter in set1)
    
    def solve(self, A):
        
        count = 0
        consoCount = 0; vowelCount = 0
        for letter in A:
            if self.isVowel(letter):
                count += consoCount # consider all previous conso as start, and this vowel as end
                vowelCount += 1
            else:
                count += vowelCount # consider all previous vowels as start, and this conso as end
                consoCount += 1
            
        return count%(10**9 + 7)
