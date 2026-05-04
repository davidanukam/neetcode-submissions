class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i, num in enumerate(bin(n)[2:]):
            if (n >> i) & 1:
                res |= (1 << (31 - i))
        return res