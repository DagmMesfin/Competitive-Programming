class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        counterdistance = 0
        clockdistance = 0
        if destination > start:
            for i in range(start, destination):
                clockdistance += distance[i]
            j = start
            while(j+len(distance) != destination):
                j-=1
                counterdistance += distance[j]
        elif start > destination:
            for i in range(destination, start):
                clockdistance += distance[i]
            j = destination
            while(j+len(distance) != start):
                j-=1
                counterdistance += distance[j]
        else:
            return 0
        return counterdistance if counterdistance < clockdistance else clockdistance
        
        