class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def travel(i, summ, p):
            if summ == target:
                output.append(p.copy())
                return
            
            for j in range(i, len(nums)):
                if summ + nums[j] > target:
                    return
                p.append(nums[j])
                travel(j, summ + nums[j], p)
                p.pop()

        nums.sort()
        travel(0, 0, [])

        return output