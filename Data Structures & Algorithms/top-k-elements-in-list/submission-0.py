class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {}
        for num in nums:
            if num in buckets:
                buckets[num] += 1
            else:
                buckets[num] = 1
        return list(sorted(buckets.keys(), key=lambda x: buckets[x], reverse=True))[:k]