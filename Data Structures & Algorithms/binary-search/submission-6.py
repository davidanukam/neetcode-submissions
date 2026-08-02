class Solution:
    def search(self, nums: List[int], target: int) -> int:
        front = 0
        end = len(nums) - 1
        
        def binary(nums: List[int], target: int, front: int, end: int) -> int:
            if front <= end:
                mid = (front + end) // 2
                if target == nums[mid]:
                    return mid
                if target > nums[mid]:
                    return binary(nums, target, mid + 1, end)
                else:
                    return binary(nums, target, front, mid - 1)
            return -1
        
        return binary(nums, target, front, end)