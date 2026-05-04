class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        ans = 0
        while ans != 1:
            ans = sum([int(i)**2 for i in str(n)])
            if ans != 1:
                if ans not in seen:
                    seen.append(ans)
                    n = ans
                else:
                    return False
            else:
                break
        return True