class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        l = 0

        for i, c in enumerate(s):
           
            if c in dic: 
                l = max(dic[c] + 1, l)
            
            dic[c] = i
            res = max(res, i - l + 1)
        return res
