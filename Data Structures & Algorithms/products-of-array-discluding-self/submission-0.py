class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_left, pre_right = [1], [1]
        n = len(nums)
        for i in range(1,n):
            pre_left.append(pre_left[i - 1] * nums[i - 1])
            pre_right.append(pre_right[i - 1] * nums[n - i])
        
        res = []

        for i in range(0, n): 
            res.append(pre_left[i] * pre_right[n - 1 - i])

        return res

        
            
