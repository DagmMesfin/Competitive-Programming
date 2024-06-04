# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while True:
            if val > curr.val:
                if not curr.right:
                    return None
                curr = curr.right
            elif val < curr.val:
                if not curr.left:
                    return None
                curr = curr.left
            else:
                return curr
