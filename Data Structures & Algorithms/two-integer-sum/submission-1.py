class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(0, len(nums)): 
            remain = target - nums[i]
            if remain in hash: 
                return [hash.get(remain), i]

            hash[nums[i]] = i
        
        return []