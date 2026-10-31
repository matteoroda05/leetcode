# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.k = k
        def findK (root: Optional[TreeNode]) -> int | None:
            past = [] #stack
            visited = set() 
            cur = root
            while cur.left:
                past.append(cur)
                cur = cur.left

            #cur now is the k=1 smallest of this branch
            visited.add(cur)
            self.k -=1
            
            if self.k == 0:
                return cur.val

            while len(past) > 0:
                if cur.right and cur.right not in visited:
                    visited.add(cur.right)
                    res = findK(cur.right)
                    if res is not None:
                        return res
                cur = past.pop(-1)
                self.k-=1
                if self.k == 0:
                    return cur.val
            if cur.right:
                return findK(cur.right)
            return None
        
        return findK(root)


    def kthSmallestDfs(self, root: Optional[TreeNode], k: int) -> int:
            self.rank = 0
            self.result = None
            def dfs(root: Optional[TreeNode]) -> None:
                if not root or self.result:
                    return

                dfs(root.left)
                self.rank += 1
                if self.rank == k:
                    self.result = root.val
                dfs(root.right)
            dfs(root) 
            return self.result