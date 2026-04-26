class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += f"{len(s)}#" + "".join(s)
        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        while len(s) > 0:
            c = s
            dis = s[0:c.index("#")]
            num = 0
            if dis.isnumeric():
                num = int(dis)
            else:
                break
            start = c.index("#") + 1
            end = c.index("#") + num + 1
            output.append(c[start:end])
            s = c[end:]
        return output
                
