# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def same_tree(p,q):
            if not p and not q:
                return True 

            if (p and not q) or (q and not p):
                return False

            if p.val != q.val:
                return False

            return same_tree(p.left,q.left) and same_tree(p.right,q.right)

        return same_tree(p,q)