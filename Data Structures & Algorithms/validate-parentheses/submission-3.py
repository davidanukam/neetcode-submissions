class Solution:
    def isValid(self, s: str) -> bool:
        data = {")" : "(", "}" : "{", "]" : "["}
        l = []

        if len(s) % 2 != 0: return False

        for b in s:
            if b in ["(", "{", "["]:
                l.append(b)
            if b in [")", "}", "]"]:
                if len(l) == 0: return False
                if data[b] != l.pop(): return False
        return True if len(l) == 0 else False