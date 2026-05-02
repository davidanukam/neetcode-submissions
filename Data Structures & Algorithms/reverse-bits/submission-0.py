class Solution:
    def reverseBits(self, n: int) -> int:
        num = ["0" for _ in range(32 - len(bin(n)[2:]))]
        num.extend([str(i) for i in bin(n)[2:]])
        return int("".join(list(reversed(num))), 2)