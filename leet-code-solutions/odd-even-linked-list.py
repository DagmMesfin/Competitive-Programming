# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        even = []
        odd = []
        i = 1
        while head:
            if i%2 == 0:
                even.append(head.val)
            else:
                odd.append(head.val)
            i+=1
            head = head.next
        odd.reverse()
        even.reverse()
        answero = ListNode(odd.pop())
        temp = answero
        while odd:
            newnode = ListNode(odd.pop())
            temp.next = newnode
            temp = temp.next
        while even:
            newnode = ListNode(even.pop())
            temp.next = newnode
            temp = temp.next
        return answero
            




        