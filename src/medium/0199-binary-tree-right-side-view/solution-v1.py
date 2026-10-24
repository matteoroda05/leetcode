# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = []
        result = []
        curH, maxH = 0, -1
        visited = set()
        node = root

        while curH >= 0:
            stack.append(node)
            visited.add(node)
            if curH > maxH:
                result.append(node.val)
                maxH = curH

            if node.right and node.right not in visited:
                node = node.right
                curH += 1
            elif node.left and node.left not in visited:
                node = node.left
                curH += 1
            else:
                stack.pop(-1)
                node = stack.pop(-1) if stack else None
                curH -= 1

        return result