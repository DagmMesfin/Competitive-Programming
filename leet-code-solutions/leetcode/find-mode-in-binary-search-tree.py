# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = Counter()
        ans = []
        def traversal(current, maxo):
            if current:
                if current.left:
                    traversal(current.left,maxo)
                res[current.val]+=1
                if current.right:
                    traversal(current.right,maxo)
        
        traversal(root,0)
        maxo = max(res.values())
        for k,v in res.items():
            if v == maxo:
                ans.append(k)
        return ans


    