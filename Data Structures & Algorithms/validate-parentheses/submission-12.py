class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")" : "(", "}" : "{", "]" : "["}
        for c in s:
            if c in list(hashmap.values()):
                stack.append(c)
            else:
                if len(stack):
                    if stack[-1] == hashmap[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return True if not len(stack) else False