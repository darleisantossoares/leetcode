# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        answer = float('-inf')

        def traverse_inorder(node, height):

            nonlocal answer

            if node is None:
                answer = max(answer, height - 1)
                return

            traverse_inorder(node.left, height + 1)
            traverse_inorder(node.right, height + 1)

        traverse_inorder(root, 1)

        return answer
