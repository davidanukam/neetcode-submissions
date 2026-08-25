class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = "".join(list(sorted(s1)))

        w = len(s1)

        l = 0

        for r in range(len(s2)):
            if r - l + 1 == w:
                sub = "".join(list(sorted(s2[l:r + 1])))
                if sub == s1:
                    return True
                l += 1
        
        return False