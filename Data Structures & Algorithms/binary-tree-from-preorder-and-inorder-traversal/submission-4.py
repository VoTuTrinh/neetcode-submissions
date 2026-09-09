# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Lưu vị trí của từng node trong inorder
        inorder_index = {
            value: index
            for index, value in enumerate(inorder)
        }

        preorder_index = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_index

            # Đoạn inorder không còn phần tử
            if left > right:
                return None

            # Phần tử tiếp theo trong preorder là root
            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)

            # Tìm vị trí root trong inorder
            middle = inorder_index[root_value]

            # Xây cây con bên trái trước, rồi cây con bên phải
            root.left = build(left, middle - 1)
            root.right = build(middle + 1, right)

            return root

        return build(0, len(inorder) - 1)

