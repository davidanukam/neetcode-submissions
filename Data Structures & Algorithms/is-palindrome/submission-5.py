class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        end = len(s) - 1

        while front != end and front < len(s) - 1 and end > 0:
            if not s[front].isalnum():
                front += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[front].lower() == s[end].lower():
                front += 1
                end -= 1
            else:
                return False
        return True