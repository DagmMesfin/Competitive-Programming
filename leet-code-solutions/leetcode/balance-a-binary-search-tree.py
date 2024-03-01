# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nums = []

        def traversal(current):
            if current:
                if current.left:
                    traversal(current.left)
                nums.append(current.val)
                if current.right:
                    traversal(current.right)
        
        traversal(root)

        def balancedTree(nums):
            if not nums:
                return None
            mid_pt = len(nums)//2
            new_tree = TreeNode(nums[mid_pt])
            new_tree.left = balancedTree(nums[:mid_pt])
            new_tree.right = balancedTree(nums[mid_pt+1:])
            return new_tree
        
        return balancedTree(nums)
        
        