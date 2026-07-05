class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}

        for i, x in enumerate(numbers): 
            need = target - x

            if need in dic: 
                
                return [dic[need] + 1, i + 1 ]
            
            dic[x] = i
        
        return []