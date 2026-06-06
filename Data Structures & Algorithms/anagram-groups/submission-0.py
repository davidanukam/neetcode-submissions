class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            sor = "".join(list(sorted(list(s))))
            if sor in ans:
                ans[sor].append(s)
            else:
                ans[sor] = [s]
        return list(ans.values())