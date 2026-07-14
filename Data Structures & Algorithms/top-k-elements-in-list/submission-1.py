class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = nums.count(num)
        return list(sorted(hashmap, reverse=True, key=lambda x: hashmap[x]))[:k]