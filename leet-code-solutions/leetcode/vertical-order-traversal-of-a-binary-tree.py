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
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = defaultdict(list)
        res = []
        if not root:
            return []

        def depth_finder(tree,depth,pos):
            if not tree:
                return
            arr[pos].append((tree.val,depth))
            if tree.left:
                depth_finder(tree.left,depth+1,pos-1)
            if tree.right:
                depth_finder(tree.right,depth+1,pos+1)
        
        depth_finder(root,0,0)

        for k,cols in sorted(arr.items(), key = lambda l:l[0]):
            cols.sort(key=cmp_to_key(self.mycmp))
            print(cols)
            cols = [cols[i][0] for i in range(len(cols))]
            print(cols)
            res.append(cols)

        return res
