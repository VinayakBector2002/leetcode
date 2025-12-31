from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        numberStack = [""]
        operationStack = []

        def apply():
            sOp = int(numberStack.pop())
            fOp = int(numberStack.pop())
            ops = operationStack.pop()
            if ops == "+":
                numberStack.append(fOp + sOp)
            elif ops == "-":
                numberStack.append(fOp - sOp)
            elif ops == "*":
                numberStack.append(fOp * sOp)
            elif ops == "/":
                numberStack.append(int(fOp / sOp))
            return
            
        for character in s:
            if character == " ":
                continue
            elif character.isdigit():
                numberStack[-1] = numberStack[-1] + character
            else:
                while operationStack and (operationStack[-1] in "*/" or (operationStack[-1] in "+-" and character in "+-")):
                    apply()
                operationStack.append(character)
                numberStack.append("")
        
        while operationStack:
            apply()
        
        return int(numberStack[-1])