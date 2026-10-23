class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []
        if not len(digits):
            return res
        
        def dfs(dex, s):
            for letter in nums[digits[dex]]:
                next_s = s + letter
                if dex == len(digits) - 1:
                    res.append(next_s) if next_s not in res else None
                else:
                    dfs(dex + 1, next_s)
        
        dfs(0, "")

        return res