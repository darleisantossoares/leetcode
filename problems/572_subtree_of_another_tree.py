# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def is_equal(node1, node2):

            if node1 is None and node2 is None:
                return True

            if node1 is None and node2 is not None:
                return False

            if node1 is not None and node2 is None:
                return False

            if node1.val == node2.val:
                return is_equal(node1.left, node2.left) and is_equal(node1.right, node2.right)
            else:
                return False

        if is_equal(root, subRoot):
            return True

        if root is None:
            return False


        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
