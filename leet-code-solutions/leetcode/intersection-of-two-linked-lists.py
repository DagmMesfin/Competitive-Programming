# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seto = set()
        curr = headA
        while curr:
            seto.add(curr)
            curr = curr.next
        curr = headB
        while curr and (curr not in seto):
            curr = curr.next
        return curr
