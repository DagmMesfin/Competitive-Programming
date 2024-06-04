class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        boats = 0
        L = 0
        R = len(people) - 1
        while L<=R:
            if people[L]+people[R] <= limit:
                L+=1
                R-=1
            else:
                R-=1
            boats+=1
        return boats
        