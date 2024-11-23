class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.checkout = {}
        self.avg = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        if id not in self.checkin:
            self.checkin[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkin:
            st_station,st_time = self.checkin[id]

            if (st_station,stationName) not in self.avg:
                self.avg[(st_station,stationName)]  = [t-st_time]
            else:
                self.avg[(st_station,stationName)].append(t - st_time)
            
            del self.checkin[id]

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        values = self.avg[startStation,endStation]
        return sum(values)/len(values)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)