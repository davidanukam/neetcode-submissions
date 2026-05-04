class Solution:
    def countBits(self, n: int) -> List[int]:
        # 4 = 100
        o = []
        for i in range(0, n + 1):
            o.append(bin(i)[2:].count("1"))
        return o