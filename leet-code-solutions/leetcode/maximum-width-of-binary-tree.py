# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        arr = defaultdict(list)

        def pos_holder(tree,depth,pos):
            if not tree:
                return
            arr[depth].append(pos)

            pos_holder(tree.left,depth+1,pos*2)
            pos_holder(tree.right,depth+1,pos*2+1)
        
        pos_holder(root,0,0)

        maxwidth = 0


        for vals in arr.values():
            vals.sort()
            maxwidth = max(maxwidth, abs(vals[-1]-vals[0])+1)
  
        return maxwidth