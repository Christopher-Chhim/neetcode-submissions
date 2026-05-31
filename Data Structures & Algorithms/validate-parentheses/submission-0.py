class Solution:
    def isValid(self, s: str) -> bool:
        # Edge case
        if not s:
            return True

        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in pairs.values():  # Opening bracket
                stack.append(ch)
            elif ch in pairs:  # Closing bracket
                if not stack:
                    return False
                top = stack.pop()
                if top != pairs[ch]:
                    return False

        if stack:
            return False

        return True
