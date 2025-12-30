class UndergroundSystem:
    def __init__(self):
        # single responsibility
        self.currentCustomers = {} # userId : (startionStart, startTime)
        self.stationStats = {} # (stationStart, stationEnd) : (cumTime, cumCount)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.currentCustomers:
            # this is invalid
            return 
        
        self.currentCustomers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.currentCustomers:
            # this is invalid 
            return 
        startionStart, startTime = self.currentCustomers[id]
        key = (startionStart, stationName)
        currentStats = self.stationStats.get(key, (0,0))
        self.stationStats[key] = (currentStats[0] + (t-startTime), currentStats[1] + 1)
        del self.currentCustomers[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        currentStats = self.stationStats[(startStation, endStation)]
        return float(currentStats[0])/currentStats[1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)