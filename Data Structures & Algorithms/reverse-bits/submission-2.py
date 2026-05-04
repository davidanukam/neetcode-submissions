class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i, num in enumerate(bin(n)[2:]):
            bit = (n >> i) & 1
            if bit:
                res |= (1 << (31 - i))
        return res