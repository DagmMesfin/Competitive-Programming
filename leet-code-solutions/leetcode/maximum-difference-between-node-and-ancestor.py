# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        listo = []
        max_diff = 0
        def min_max(tree,maxo,mino):
            mino = min(mino,tree.val)
            maxo = max(maxo,tree.val)
            if not tree.left and not tree.right:
                listo.append((mino,maxo))
                return
            if tree.left:
                min_max(tree.left,maxo,mino)
            if tree.right:
                min_max(tree.right,maxo,mino)
        min_max(root,float("-inf"),float("inf"))

        for i in range(len(listo)):
            max_diff = max(max_diff,listo[i][1]-listo[i][0])
        
        return max_diff


