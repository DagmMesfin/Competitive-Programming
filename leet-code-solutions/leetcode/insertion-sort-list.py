# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head

        while current:
            second = current.next
            while second:
                if second.val < current.val:
                    second.val,current.val = current.val,second.val
                second = second.next
            current = current.next
        
        return head
        