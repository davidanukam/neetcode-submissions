class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        long = s if len(s) > len(t) else t
        other = t if long == s else s
        for c in long:
            if long.count(c) != other.count(c):
                return False
        return True