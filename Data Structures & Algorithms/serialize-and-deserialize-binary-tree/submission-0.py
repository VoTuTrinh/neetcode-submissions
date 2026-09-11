# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        values = []
        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                values.append("#")
                return
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(values)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        i = 0

        def dfs():
            nonlocal i

            if i >= len(values):
                return None

            value = values[i]
            i += 1

            if value == "#":
                return None

            node = TreeNode(int(value))
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()




