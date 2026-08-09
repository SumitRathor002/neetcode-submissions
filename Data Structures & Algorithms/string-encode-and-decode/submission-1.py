class Solution:
    delimiter = '#'

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f"{len(s)}#{s}"
        
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        res = []
    
        while s:
            print(s)
            length = int(s[0])
            temp = ''
            idx = 0
            if length == 0:
                s = s[2:]
                res.append('')
                continue
            for i in range(length):
                temp += s[i+2]
                idx = i
            s = s[idx+3:]
            res.append(temp)

        return res