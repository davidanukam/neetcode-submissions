from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def binary(h: int, front: int, end: int, k: int) -> int:
            if front <= end:
                mid = (front + end) // 2
                hours_taken = 0
                for x in piles:
                    hours_taken += ceil(x / mid)
                if hours_taken <= h:
                    return binary(h, front, mid - 1, mid)
                else:
                    return binary(h, mid + 1, end, k)
            else:
                return k

        return binary(h, 1, max(piles), max(piles))