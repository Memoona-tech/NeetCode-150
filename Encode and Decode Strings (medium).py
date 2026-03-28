🔒 Premuim problem on LC
# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

       # " 5#Hello 5#World "

    def decode(self, s: str) -> List[str]:
        res, currSt = [], 0
        
        while currSt < len(s):
            j = currSt
            while s[j] != '#':
                j += 1
            length = int(s[currSt:j])
            word = s[j+1: j+1+length]
            res.append(word)

            currSt = j+1+length
        return res
