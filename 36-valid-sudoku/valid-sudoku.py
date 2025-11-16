from collections import Counter

class Solution:
    def quickChecker(self, listOfNumbers: List[str]) -> bool:
        pair = Counter(listOfNumbers).most_common(2)
        for x, y in pair:
            if x != '.' and y > 1:
                return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows 
        n = len(board)
        retVal = True
        for i in range(n):
            retVal = retVal and self.quickChecker(board[i]) and self.quickChecker([board[x][i] for x in range(n)])

        for i in range(0,n,3):
            for j in range(0,n,3):
                subset = []
                for k in range(3):
                    for l in range(3):
                        subset.append(board[i + k][j + l])
                retVal = retVal and self.quickChecker(subset)

        
        return retVal