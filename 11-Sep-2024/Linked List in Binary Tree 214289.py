# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # curr_tree = root
        # curr_ll = head

        if not root:
            return False

        def check(ll, tree):

            # print("List", ll)
            # print("Tree", tree)

            if not ll and not tree:
                return True
            
            if not ll and tree:
                return True
            
            if ll and not tree:
                return False

            if ll.val == tree.val:
                return check(ll.next, tree.left) or check(ll.next, tree.right)
            else:
                return False
            

        return check(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)