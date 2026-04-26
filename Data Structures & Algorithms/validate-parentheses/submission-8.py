class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        f = ["(", "{", "["]
        b = [")", "}", "]"]
        for c in s:
            if c in f:
                stack.append(b[f.index(c)])
            if c in b:
                if len(stack) > 0:
                    if stack[-1] != c:
                        return False
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False