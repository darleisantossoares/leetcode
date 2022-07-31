# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def bfs(node):

            output = []

            q = collections.deque()

            q.append((node, 0))

            while len(q) > 0:

                n, level = q.popleft()

                if level >= len(output):
                    output.append([])

                output[level].append(n.val)

                if n.left:
                    q.append((n.left, level + 1))

                if n.right:
                    q.append((n.right, level + 1))

            return output

        return bfs(root) if root else []
