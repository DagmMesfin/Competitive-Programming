# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        arr = []

        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        stk = []

        for i in arr:
            if stk:
                stk.append(gcd(stk[-1],i))
            stk.append(i)


        node = ListNode(stk[0])
        tail = node
        for i in range(1,len(stk)):
            newnode = ListNode(stk[i])
            tail.next = newnode
            tail = tail.next
        
        return node

