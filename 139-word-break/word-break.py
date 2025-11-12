'''
input: Given a string s and a dictionary of strings wordDict 

return: true 

if given string s
    can be segmented into  
    space-separated sequence of one or more!!! dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

"leetcode"
l   ["l"]
    e   ["le"]
        ["l", "e"]: Only create a new segment if we find the last segment in dict

Recursion : index, Segment
    Base 
    if index >= n
    Inductive
    Add to segement 
        if found then send new segement to index + 1
        else segement + s[index]

s = "leetcode", wordDict = ["leet","code"]
s[:4] + s[4:]
s = "leetcode", wordDict = ["leet","codes", "leetcode"]
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)

        if s in wordDict:
            return True
        
        @cache
        def find_next_segment(start, end):
            if end == n and s[start:end] in wordDict:
                return True
            if end >= n:
                return False
            
            result = False
            new_segment = s[start:end+1]
            if new_segment in wordDict:
                result = result or find_next_segment(end+1, end+1)
            return result or find_next_segment(start, end + 1)


        return find_next_segment(0, 0)
        