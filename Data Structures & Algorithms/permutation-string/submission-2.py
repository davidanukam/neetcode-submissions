class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w = len(s1)

        count1 = {}

        for letter in s1:
            count1[letter] = 1 + count1.get(letter, 0)
        
        count2 = {}

        l = 0
        for r in range(len(s2)):
            found = True
            count2[s2[r]] = 1 + count2.get(s2[r], 0)
            if r - l + 1 == w:
                for key, value in count2.items():
                    if key not in count1:
                        found = False
                        break
                    else:
                        if value != count1[key]:
                            found = False
                            break
                if found:
                    return True
                else:
                    # Not a permutation
                    if count2[s2[l]] - 1 == 0:
                        count2.pop(s2[l], None)
                    else:
                        count2[s2[l]] -= 1
                    l += 1
        
        return False

