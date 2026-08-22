class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        output = 0
        sub = ""
        for letter in s:
            if len(sub):
                if letter in sub:
                    count -= sub.index(letter) + 1
                    sub = sub[sub.index(letter) + 1:]
            sub += letter
            count += 1
            output = max(output, count)
        return output
