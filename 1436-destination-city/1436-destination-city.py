class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        HashMap = {}
        for i in range(len(paths)):
            HashMap[paths[i][0]] = paths[i][1]
        dest = paths[0][0]
        while(True):
            try:
                dest = HashMap[dest]
            except KeyError:
                return dest
        