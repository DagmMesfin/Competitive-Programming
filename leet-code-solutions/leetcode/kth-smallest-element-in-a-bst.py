# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def traversal(current):
            if current:
                if current.left:
                    traversal(current.left)
                res.append(current.val)
                if current.right:
                    traversal(current.right)
        
        traversal(root)

        return res[k-1]