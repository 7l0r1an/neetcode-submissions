class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i  in range(len(strs)):
           res += str(len(strs[i])) + "#" + strs[i]
        return res

    def decode(self, s: str) -> List[str]:
        rezultat = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            cuvant = s[j+1:j+1+length]
            rezultat.append(cuvant)
            i = j + length + 1
        return rezultat