# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from copy import deepcopy
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        non_rev = copy.deepcopy(head)
        new_list = None
        current = head
        count = 0
        while current:
            count+=1
            nextonode = current.next
            current.next = new_list
            new_list = current
            current = nextonode
        
        rev_list = new_list
        

        isthere = True
        while non_rev and rev_list:
            if(non_rev.val != rev_list.val):
                isthere = False
                break
            else:
                non_rev = non_rev.next
                rev_list = rev_list.next
        return isthere