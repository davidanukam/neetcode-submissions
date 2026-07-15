class Solution:
    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += f"{len(s)}#{s}"
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        while len(s):
            c = s
            dis = c[0:s.index("#")]
            if dis.isnumeric():
                num = int(dis)
            start = s.index("#") + 1
            end = s.index("#") + 1 + num
            output.append(c[start:end])
            s = c[end:]
        return output