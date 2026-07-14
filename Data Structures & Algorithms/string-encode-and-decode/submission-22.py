class Solution:
    def encode(self, strs: List[str]) -> str:
        output = []
        for s in strs:
            output.append(str(len(s)))
            output.append("#")
            output.append(s)
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        output = []
        while True:
            num = 0
            num_str = ""
            for c in s:
                if c.isnumeric():
                    num_str += c
                    continue
                break
            if len(num_str) == 0: break
            num = int(num_str)
            s = s[len(num_str) + 1:]
            word = ""
            for i in range(num):
                word += s[i]
            output.append(word)
            s = s[len(word):]
            if len(s) <= 0:
                break
        return output