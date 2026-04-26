class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [i, seen[diff]] if i <= seen[diff] else [seen[diff], i]
            seen[num] = i
        return []