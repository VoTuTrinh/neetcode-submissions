class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count = {}
        for x in s: 
            count[x] = count.get(x, 0) + 1;
        
        for x in t:
            if x not in count or count[x] == 0:
                return False
            
            count[x] = count.get(x) - 1
        
        return True
        