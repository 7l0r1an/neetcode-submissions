class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for cuv in strs:
            cheie ="".join(sorted(cuv))
            if cheie in d:
                d[cheie].append(cuv)
            else:
                d[cheie] = [cuv]
        return list(d.values())
        