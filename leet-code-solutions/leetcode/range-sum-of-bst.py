# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []

        def traversal(current):
            if current:
                if current.left:
                    traversal(current.left)
                res.append(current.val)
                if current.right:
                    traversal(current.right)
        
        traversal(root)
        
        return sum(res[res.index(low):res.index(high)+1])