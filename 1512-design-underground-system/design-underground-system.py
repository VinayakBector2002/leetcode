class UndergroundSystem:

    def __init__(self):
        self.track = {} # id : (startStation, startTime)
        self.avgTime = {} # (startStation,EndStation) : (totalTime, totalN)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.track[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startingStation, statingTime  = self.track[id]
        key = (startingStation, stationName)
        current = self.avgTime.get(key, (0,0))
        self.avgTime[key] = (current[0] + (t - statingTime), current[1] + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        current = self.avgTime[(startStation, endStation)]
        return float(current[0]) / current[1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)