class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suf = []

        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            pre.append(prod)

        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            suf.insert(0, prod)
        
        output = []
        for i in range(len(nums)):
            if i > 0 and i < len(nums) - 1:
                output.append(pre[i - 1] * suf[i + 1])
            if i == 0:
                output.append(suf[i + 1])
            if i == len(nums) - 1:
                output.append(pre[i - 1])
        
        return output