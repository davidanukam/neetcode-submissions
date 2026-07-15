class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        num_prods = []
        for num in nums:
            num_prods.append(prod)
            prod *= num

        prod = 1
        rev_num_prods = []
        for num in list(reversed(nums)):
            rev_num_prods.append(prod)
            prod *= num
        
        output = []
        for i, num in enumerate(num_prods):
            output.append(num_prods[i] * rev_num_prods[len(rev_num_prods) - 1 - i])
        
        return output