class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return list(sorted([int(ord(c)) for c in s])) == list(sorted([int(ord(c)) for c in t]))