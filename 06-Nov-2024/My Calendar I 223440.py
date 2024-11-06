# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.booking = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        self.booking.add((startTime,1))
        self.booking.add((endTime,-1))
        res = 0
        op = 0
        for event in self.booking:
            op += event[1]
            res = max(res,op)
        if res>=2:
            self.booking.remove((startTime,1))
            self.booking.remove((endTime,-1))
            return False
        return True
        



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)