class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      hash = {}

      for i, value in enumerate(nums):
        if target - value in hash:
            return [hash.get(target - value), i]  
        hash[value] = i