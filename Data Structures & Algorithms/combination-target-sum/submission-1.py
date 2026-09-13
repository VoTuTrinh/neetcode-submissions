class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtracking(start, total):

            if total  == target:
                result.append(path.copy())
                return 

            if total > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                total += nums[i]
                backtracking(i, total)
                total -= nums[i]
                path.pop()
            
        backtracking(0, 0)

        return result

                
            
        
        