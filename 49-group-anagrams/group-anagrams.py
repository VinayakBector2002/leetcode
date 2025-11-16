class Solution:
    def getAscii(self, string: str) -> Tuple[str]:
        plane = [0] * 26
        for char in string:
            plane[ord(char) - ord('a')] += 1
        return tuple(plane)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        clts = defaultdict(list)
        for string in strs:
            clts[self.getAscii(string)].append(string)
        return list(clts.values())