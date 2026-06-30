class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs: 
            key = [0] * 26
            for x in s: 
                i = ord(x) - ord('a')
                key[i] += 1
            dic[tuple(key)].append(s)
        return list(dic.values())