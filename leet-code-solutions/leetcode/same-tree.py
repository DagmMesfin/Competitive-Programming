# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def double_dfs(current,current1):
            if not current and not current1:
                return True
            if not current or not current1: 
                return False
            if current.val==current1.val and double_dfs(current.left,current1.left) and double_dfs(current.right,current1.right):
                return True
            return False

        return double_dfs(p,q)
        