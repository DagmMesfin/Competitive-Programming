# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        listo = []
        current = head
        n = 0
        while current:
            listo.append(current.val)
            current = current.next
            n+=1
        for i in range(n//2):
            if listo[i] != listo[n-i-1]:
                return False
        return True
        

        