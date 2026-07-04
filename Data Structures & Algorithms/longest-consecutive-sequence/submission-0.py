class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = defaultdict(set)
        max = 0
        for x in nums: 
            if x in dic:
                continue
            dic[x] = set({x})
            if (x - 1) in dic: 
                dic[x] = dic[x] | dic[x - 1]
                dic[x - 1] = dic[x]
            if (x + 1) in dic: 
                dic[x] = dic[x] | dic[x + 1]
                dic[x + 1] = dic[x] 
            

        for x in nums: 
            dic[x] = set({x})
            if (x - 1) in dic: 
                dic[x] = dic[x] | dic[x - 1]
            if (x + 1) in dic: 
                dic[x] = dic[x] | dic[x + 1]

            if len(dic[x]) > max:
                max = len(dic[x])
    
        return max
            