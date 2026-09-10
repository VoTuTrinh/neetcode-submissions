# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res

            if not node: 
                return 0

            maxLeft = max(0, dfs(node.left))
            maxRight = max(0, dfs(node.right))
            maxSum = node.val + maxLeft + maxRight

            res = max(maxSum, res)
            
            return node.val + max(maxLeft, maxRight)

        dfs(root)
        return res


        
        
    

    
    
     


    