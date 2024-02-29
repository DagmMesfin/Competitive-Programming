# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        listo = []
        def digit_sum(tree,numo):
            numo+=str(tree.val)
            if not tree.left and not tree.right:
                listo.append(int(numo))
                return
            if tree.left:
                digit_sum(tree.left,numo)
            if tree.right:
                digit_sum(tree.right,numo)
        digit_sum(root,"")

        return sum(listo)
        