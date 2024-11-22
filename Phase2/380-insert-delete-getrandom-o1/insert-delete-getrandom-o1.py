class RandomizedSet:
    #  the prblem is that randset us not random when it is poping
    def __init__(self):
        self.randomset = {}
        self.data = []
        self.index = 0
        

    def insert(self, val: int) -> bool:
        if val in self.randomset:
            return False
        
        self.randomset[val] = self.index
        self.data.append(val)
        self.index += 1
        
        return True

        
        

    def remove(self, val: int) -> bool:
        if val not in self.randomset:
            return False
        
        ind = self.index -1
        x = self.data[ind]

        self.data[ind],self.data[self.randomset[val]] = self.data[self.randomset[val]],self.data[ind]
        self.randomset[x] = self.randomset[val]
        self.data.pop()
        del self.randomset[val]
        self.index -= 1
        return True
    



        

    def getRandom(self) -> int:

        randomindex = random.randint(0,self.index - 1)

        return self.data[randomindex]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()