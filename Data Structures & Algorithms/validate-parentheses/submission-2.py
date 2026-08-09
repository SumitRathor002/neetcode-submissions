class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        brackets = {
            # '(': ')',
            # '[': ']',
            # '{': '}'
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for char in s:
            if char in brackets and stack and brackets[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char) 
        
        return not bool(stack)