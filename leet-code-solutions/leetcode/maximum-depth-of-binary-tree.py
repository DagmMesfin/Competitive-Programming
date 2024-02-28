# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        def depth_finder(tree,depth):
            if not tree:
                return depth
            depth+=1
            return max(depth_finder(tree.left,depth),depth_finder(tree.right,depth))
        
        return depth_finder(root,0)
        