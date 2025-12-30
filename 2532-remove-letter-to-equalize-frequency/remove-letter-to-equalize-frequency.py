'''

You are given a 0-indexed string word, 
consisting of lowercase English letters. 

You need to select one index and remove the letter 

at that index from word so that 
    the frequency of every letter present in word is equal.

Return true 
    if it is possible to remove one letter so that the frequency of all letters in word are equal, 
and false otherwise.

'''

from collections import Counter 

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        for char in word:
            counter[char] -= 1
            counterVals = [v for v in counter.values() if v > 0]
            if len(set(counterVals)) == 1:
                return True
            counter[char] += 1
        return False