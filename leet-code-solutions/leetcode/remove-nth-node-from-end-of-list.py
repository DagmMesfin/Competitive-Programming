
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head and not head.next:
            return None
        temp = head
        count = 0
        while temp and temp.next:
            temp = temp.next
            count+=1
        k = count-n
        if k<0:
            head = head.next
            return head
            
        prev = head
        for i in range(k):
            prev = prev.next
        prev.next = prev.next.next
        return head
