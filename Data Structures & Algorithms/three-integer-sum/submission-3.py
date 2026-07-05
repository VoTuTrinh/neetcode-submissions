class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums);
        n = len(nums)
        res = set()

        for i, x in enumerate(sorted_nums[0: n - 2]): 
            l, r = i + 1, n - 1
            target = 0 - x
            while l < r: 
                if sorted_nums[l] + sorted_nums[r] > target: 
                    r -= 1
                elif sorted_nums[l] + sorted_nums[r] < target:
                    l += 1
                else:
                    res.add((x, sorted_nums[l], sorted_nums[r]))
                    l += 1
                    r -= 1

        return [list(i) for i in res]
        

