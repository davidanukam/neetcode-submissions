class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return False
        
        head = 0
        tail = -1

        t = ""
        for c in s:
            if c.isalnum():
                t += c.lower()

        if t == "" and len(s) > 0:
            t = " "

        while head > tail:
            if t[head] != t[tail]: return False
            head += 1
            tail -= 1
            if head > len(t) - 1: return True
        return True