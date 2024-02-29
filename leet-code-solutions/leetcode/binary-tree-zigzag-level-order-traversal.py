# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mycmp(self,a, b): 
        if a[1] > b[1]: 
            return 1
        elif a[1] == b[1]:
            if a[0] > b[0]:
                return 1
            elif a[0] < b[0]:
                return -1
            else:
                return 0
        elif a[1] < b[1]: 
            return -1
        else: 
            return 0
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = defaultdict(list)
        res = []
        if not root:
            return []

        def pos_holder(tree,depth):
            if not tree:
                return
            arr[depth].append(tree.val)
            if tree.left:
                pos_holder(tree.left,depth+1)
            if tree.right:
                pos_holder(tree.right,depth+1)
        
        pos_holder(root,0)

        for k,cols in sorted(arr.items()):
            if k%2 == 1:
                cols.reverse()
                
            res.append(cols)

        return res