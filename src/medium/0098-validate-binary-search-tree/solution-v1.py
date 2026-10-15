# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        
        def validate(root: TreeNode | None, lBound: int | None, rBound: int | None) -> bool:
            if not root:
                return True
            if lBound is not None and root.val <= lBound:
                return False
            if rBound is not None and root.val >= rBound:
                return False

            return validate(root.left, lBound, root.val) and validate(root.right, root.val, rBound)
        
        return validate(root, None, None)