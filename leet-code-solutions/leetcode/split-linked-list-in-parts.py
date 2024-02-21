# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        N = 0
        while curr:
            N+=1
            curr = curr.next
        print(N)
        ans = []
        curr = head
        moves = N//k 
        fmr = N%k
        rem = N
        for i in range(1, k+1):
            ans.append(curr)
            prev = ListNode()
            movo = moves+0
            if i<=fmr:
                movo+=1
            for i in range(movo):
                prev = curr
                curr = curr.next
            prev.next = None

        return ans


        