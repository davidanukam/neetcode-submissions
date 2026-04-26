class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        while first <= last:
            mid = (first + last) // 2
            if nums[mid] == target: return mid
            if target < nums[mid]:
                last = mid - 1
            if target > nums[mid]:
                first = mid + 1
        return -1
