# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prev = head
        actual = head
        i = 1
        if not temp:
            return None
        if not temp.next:
            return head
        while temp.next:
            temp = temp.next
            i += 1
        
        if k > i:
            k = k%i
        elif k == i or k==0:
            return head
        if k == 0:
            return head
        
        k0 = 0
        while prev and k0 < i-k-1:
            prev = prev.next
            k0+=1
        
        actual = prev.next
        prev.next = None
        temp.next = head
        return actual