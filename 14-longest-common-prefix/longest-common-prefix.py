class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        len_strs = [len(string) for string in strs]
        minn = min(len_strs)
        result = []
        for index in range(minn):
            for j in range(1, len(strs)):
                if strs[j][index] != strs[0][index]:
                    return "".join(result)
            result.append(strs[0][index])
        
        return "".join(result)