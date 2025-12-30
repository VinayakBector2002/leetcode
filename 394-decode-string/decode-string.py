'''
input and output -> str
Given an encoded string, return its decoded string.

The encoding rule is: 
    k[encoded_string], 
    where the encoded_string inside the **square brackets** is being repeated exactly k times. 
    Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; 
    there are no extra white spaces, 
    square brackets are well-formed, etc. 

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Solution:
    # Stack impl 
    stack = []

    For each character in word
        if char not ] then add to stack
            alnum | [
        else
            to get (rev) encoded string -> while stack until top = [: pop
            stack.pop() -> [
            to get (rev) k string -> while stack until not num or not stack: pop
            add/extend [k * encoded string] to stack 
            continue
3[a] 2[bc]
stack - 3
stack - 3[
stack - 3[a    
4th-> stack - aaa
stack - aaa2
'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if not char == "]":
                stack.append(char)
                continue
            # case where char == "]"
            encodedString = []
            
            while stack and stack[-1] != "[":
                encodedString.append(stack.pop())
            # top of stack is open bracket [
            stack.pop()
            encodedString[::-1]
            k = []

            while stack and stack[-1] in list("0123456789"):
                k.append(stack.pop())

            k = int("".join(k[::-1]))
            transformedString = k * encodedString
            stack.extend(transformedString[::-1])
        
        return "".join(stack)