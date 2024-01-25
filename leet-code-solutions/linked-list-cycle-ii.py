# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        thereAcycle = False
        if not head:
            return None
        tortoise = head
        rabbit = head
        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next.next
            if(tortoise == rabbit):
                thereAcycle = True
                break
        if not thereAcycle:
            return None
        else:
            tortoise = head
            while tortoise != rabbit:
                tortoise = tortoise.next
                rabbit = rabbit.next
        return rabbit

        