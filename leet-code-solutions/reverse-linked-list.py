class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        current = head

        while current:
            nextnode = current.next
            current.next = new_list
            new_list = current
            current = nextnode
        return new_list