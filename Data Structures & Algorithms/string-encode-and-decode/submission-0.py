class Solution:
    delimiter = '#'

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f"{len(s)}#{s}"
        return res


    def decode(self, s: str) -> List[str]:
        res = []
    
        while s:
            length = int(s[0])
            temp = ''
            idx = 0
            for i in range(length):
                temp += s[i+2]
                idx = i
            s = s[idx+3:]
            res.append(temp)

        return res