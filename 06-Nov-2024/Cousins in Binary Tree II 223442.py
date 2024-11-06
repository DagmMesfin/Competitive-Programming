# Problem: Cousins in Binary Tree II - https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.val = 0

        que = deque([root])
        pat_tot = defaultdict(int)

        while que:
            node_arr = []
            total_sum = 0
            for _ in range(len(que)):

                node = que.popleft()
                node_arr.append(node)

                if node.left:
                    que.append(node.left)
                    pat_tot[node]+=node.left.val
                    total_sum+=node.left.val
                
                if node.right:
                    que.append(node.right)
                    pat_tot[node]+=node.right.val
                    total_sum+=node.right.val
                
            for node in node_arr:
                if node.left:
                    node.left.val = total_sum - pat_tot[node]
                if node.right:
                    node.right.val = total_sum - pat_tot[node]
                    
        return root