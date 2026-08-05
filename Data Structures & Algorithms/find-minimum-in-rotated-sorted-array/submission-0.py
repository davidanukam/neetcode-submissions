class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary(front: int, end: int, mini: int):
            if front <= end:
                mid = (front + end) // 2
                if nums[mid] < mini:
                    mini = nums[mid]
                if nums[mid] > nums[end]:
                    return binary(mid + 1, end, mini)
                else:
                    return binary(front, mid - 1, mini)
            else:
                return mini
        
        return binary(0, len(nums) - 1, nums[0])