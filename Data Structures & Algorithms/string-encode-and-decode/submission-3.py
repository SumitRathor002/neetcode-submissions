class Solution:
    delimiter = '#'

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f"{len(s)}#{s}"
        
        # print(res)
        return res


    def decode(self, s: str) -> List[str]:
        res = []
    
        while s:
            # print(s)
            length = ''
            idx = 0
            while True:
                if s[idx] == '#':
                    break
                length += s[idx]
                idx += 1
            
            dig_length = len(length)
            length = int(length)
            temp = ''
            idx = 0
            if length == 0:
                s = s[2:]
                res.append('')
                continue

            for i in range(length):
                temp += s[i+dig_length+1]
                idx = i
            s = s[idx+dig_length+2:]
            res.append(temp)

        return res