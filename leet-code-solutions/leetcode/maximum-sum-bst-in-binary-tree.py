# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0

        def helper(root):
            nonlocal res
            if not root:
                return [0, float("-inf"), float("inf")]

            leftsum, leftmax, leftmin = helper(root.left)
            rightsum, rightmax, rightmin = helper(root.right)

            if root.left:
                if root.left.val < root.val and leftmax < root.val:
                    left = leftsum
                else:
                    left = float("-inf")
            else:
                left = 0

            if root.right:
                if root.right.val > root.val and rightmin > root.val:
                    right = rightsum
                else:
                    right = float("-inf")
            else:
                right = 0
            
            mino = min(rightmin,leftmin)
            maxo = max(rightmax,leftmax)

            res = max(left+right+root.val, res)

            return [left+right+root.val, max(root.val, maxo), min(root.val, mino)]
        
        helper(root)

        return res


            
                
            