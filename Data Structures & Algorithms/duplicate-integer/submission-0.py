class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for x in nums:
            if x in count:
                return True
            count[x] = 1
        return False


        