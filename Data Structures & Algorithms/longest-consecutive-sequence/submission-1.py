class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}
        nums = list(sorted(nums))
        for i, num in enumerate(nums):
            if num in hash_map: continue
            if num - 1 in hash_map:
                hash_map[num] = hash_map[num - 1] + 1
            else:
                hash_map[num] = 1
        return max(hash_map.values()) if hash_map else 0