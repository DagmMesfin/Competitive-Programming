# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        arr = [[-1]*n for i in range(m)]

        yStart, yEnd = -1, m
        xStart, xEnd = -1, n

        y, x = 0, 0

        direction = 0

        while head:
            arr[y][x] = head.val

            if direction == 0:
                if x+1 == xEnd:
                    direction += 1
                    yStart = y
                    y += 1
                else: x+=1

            elif direction == 1:
                if y+1 == yEnd:
                    direction += 1
                    xEnd = x
                    x -= 1
                else: y+=1

            elif direction == 2:
                if x-1 == xStart:
                    direction += 1
                    yEnd = y
                    y -= 1
                else: x-=1

            elif direction == 3:
                if y-1 == yStart:
                    direction = 0
                    xStart = x
                    x += 1
                else: y-=1

            head = head.next
            
        return arr