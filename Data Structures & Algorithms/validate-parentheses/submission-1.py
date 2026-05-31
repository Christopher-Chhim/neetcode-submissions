class Solution:
    def isValid(self, s: str) -> bool:
        # Edge case
        if len(s) % 2 != 0:
            return False
        
        stack = []
        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for i in s:
            if i in pairs:
                if not stack or stack.pop() != pairs[i]:
                    return False
            else:
                stack.append(i)
        return not stack