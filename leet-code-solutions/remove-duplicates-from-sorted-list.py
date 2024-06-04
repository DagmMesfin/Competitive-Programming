# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            seto = set()
            sortedList = ListNode(head.val)
            temp = sortedList
            seto.add(head.val)
            while head.next:
                head = head.next
                if head.val not in seto:
                    seto.add(head.val)
                    newnode = ListNode(head.val)
                    temp.next = newnode
                    temp = temp.next
                else:
                    continue
        else:
            sortedList = None
        return sortedList
                
