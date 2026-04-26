class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c not in p:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if p[c] != stack[-1]:
                    return False
                stack.pop()
            
        return True if len(stack) == 0 else False