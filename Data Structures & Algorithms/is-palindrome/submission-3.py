class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c.lower() if c.isalnum() else "" for c in s])
        return s == "".join(reversed(list(s)))