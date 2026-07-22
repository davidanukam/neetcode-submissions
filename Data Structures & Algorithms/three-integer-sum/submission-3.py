class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = list(sorted(nums))
        output = []
  
        for i in range(len(nums)):
            target = nums[i]
            p1 = 0
            p2 = len(nums) - 1

            while p1 < p2:
                if p1 == i:
                    p1 += 1
                    continue
                if p2 == i:
                    p2 -= 1
                    continue
                if nums[p1] + nums[p2] == -target:
                    triplet = list(sorted([nums[p1], nums[p2], target]))
                    if triplet not in output:
                        output.append(triplet)
                    p1 += 1
                    p2 -= 1
                elif nums[p1] + nums[p2] < -target:
                    p1 += 1
                elif nums[p1] + nums[p2] > -target:
                    p2 -= 1
                else:
                    p1 += 1
                    p2 -= 1
        
        return output