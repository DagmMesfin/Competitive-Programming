# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        listo = []
        currentval = head
        start = head
        i = 1
        starto = head
        while currentval:
            if i>=left and i<=right:
                if i==left:
                    starto = currentval
                listo.append(currentval.val)
            i+=1
            currentval = currentval.next
        if not listo:
            return head
        for i in range(len(listo)):
            starto.val = listo[-1-i]
            starto = starto.next
        
        return start
        
        