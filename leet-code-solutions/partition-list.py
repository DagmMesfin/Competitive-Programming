# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        before_x = []
        after_x = []
        i = 1
        while head:
            if head.val < x:
                before_x.append(head.val)
            else:
                after_x.append(head.val)
            i+=1
            head = head.next
        before_x.reverse()
        after_x.reverse()
        answero = None
        if before_x:
            answero = ListNode(before_x.pop())
        elif after_x:
            answero = ListNode(after_x.pop())
        temp = answero
        while before_x:
            newnode = ListNode(before_x.pop())
            temp.next = newnode
            temp = temp.next
        while after_x:
            newnode = ListNode(after_x.pop())
            temp.next = newnode
            temp = temp.next
        return answero
        