class UndergroundSystem:

    def __init__(self):
        self.checkedIn={}
        self.checkedOut=defaultdict(int)
        self.count=defaultdict(int)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id]=[t,stationName]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.checkedOut[(self.checkedIn[id][1],stationName)]+=t-self.checkedIn[id][0]
        self.count[(self.checkedIn[id][1],stationName)]+=1
        self.checkedIn.pop(id)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        data_set=(startStation,endStation)
        if data_set in self.checkedOut:
            return self.checkedOut[data_set]/self.count[data_set]
        # for key,value in self.checkedOut.items():
        #     if key[1]==endStation and key[0]==startStation:
        #         return value/self.count[key]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)