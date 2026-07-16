class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        for num in list(sorted(nums)):
            if num in hashmap: continue
            if num - 1 in hashmap:
                hashmap[num] = hashmap[num - 1] + 1
            else:
                hashmap[num] = 1
        return max(hashmap.values()) if hashmap else 0
