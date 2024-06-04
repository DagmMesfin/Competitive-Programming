class UndergroundSystem:

    def __init__(self):
        self.check_in = defaultdict(list)
        self.start_destination_times = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_destination = (self.check_in[id][0], stationName)
        delta_time = t - self.check_in[id][1]
        self.start_destination_times[start_destination].append(delta_time)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        start_destination = (startStation, endStation)
        
        time_history = self.start_destination_times[start_destination]
        return sum(time_history)/len(time_history)
        



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)