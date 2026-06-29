class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            sortedStr = ''.join(sorted(s))
            dic[sortedStr].append(s)
        
        return list(dic.values())