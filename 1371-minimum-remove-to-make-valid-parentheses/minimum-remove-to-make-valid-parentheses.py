'''
input: List[str]

Given a string s of '(' , ')' and lowercase English characters.

Your task is to 
    remove the **minimum** number of parentheses ( '(' or ')', 
    in any positions ) so that the resulting parentheses string 
    is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
    - It is the empty string, contains only lowercase characters, or
    - It can be written as AB (A concatenated with B), where A and B are valid strings, or
    - It can be written as (A), where A is a valid string.

Doubts:
    Can we assume strings are always well formed? -> yes
    And we can return any valid string 

Modified Soln:
    Stack = []
    invalidCount = set()
    # We will literate over the string 
    for idx, ele in enumerate(s):
        if ele == "(":
            stack.append(idx)
        elif ele == ")" and stack and s[stack[-1]] == "(":
            stack.pop()
        else:
            invalidCount.add(idx)
    
    invalidCount.update(stack)

    return [for i in ]

'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalidCount = set()
        # We will literate over the string 
        for idx, ele in enumerate(s):
            if ele.isalpha():
                continue
            elif ele == "(":
                stack.append(idx)
            elif ele == ")" and stack and s[stack[-1]] == "(":
                stack.pop()
            else:
                invalidCount.add(idx)
        
        invalidCount.update(stack)

        return "".join([s[i] for i in range(len(s)) if i not in invalidCount])
        