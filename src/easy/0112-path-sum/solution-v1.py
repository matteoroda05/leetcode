# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSumBFS(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False

        fifoQ = deque()
        fifoQ.append((root, 0))

        def isLeaf(node: TreeNode):
            return (not node.left) and (not node.right)

        while fifoQ:
            cur, cursum = fifoQ.popleft()
            cursum += cur.val
            if cursum == targetSum and isLeaf(cur):
                return True

            if cur.left: fifoQ.append((cur.left, cursum))
            if cur.right: fifoQ.append((cur.right, cursum))
        
        return False
    
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False

        fifoQ = deque()
        fifoQ.append((root, 0))

        def isLeaf(node: TreeNode):
            return (not node.left) and (not node.right)

        while fifoQ:
            cur, cursum = fifoQ.pop()
            cursum += cur.val
            if cursum == targetSum and isLeaf(cur):
                return True

            if cur.left: fifoQ.append((cur.left, cursum))
            if cur.right: fifoQ.append((cur.right, cursum))
        
        return False