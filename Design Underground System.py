class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.travel_t = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        dep_station, dep_time = self.checkin[id]
        if (dep_station,stationName) not in self.travel_t:
            self.travel_t[(dep_station,stationName)] = [t - dep_time, 1]
        else:
            self.travel_t[(dep_station,stationName)][0] += t - dep_time
            self.travel_t[(dep_station,stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_t[(startStation , endStation)]
        return total_time/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
