class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for i in range(len(nums)):
            temp_subset = subsets.copy()
            for subset in subsets:
                temp = subset.copy()
                temp.append(nums[i])
                if temp not in temp_subset:
                    temp_subset.append(temp)
            subsets = temp_subset
        
        return subsets