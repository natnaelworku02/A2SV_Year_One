class Robot:

    def __init__(self, width: int, height: int):
        self.width=width
        self.height=height
        self.pos=[0,0]
        self.dir="East"

    def step(self, num: int) -> None:
        calculation =(2 * self.width) + (2 * self.height) - 4
        num=num% calculation
        for i in range ( num ):
            if self.pos==[0,0]:
                self.dir = "East"
            elif self.pos == [self.width - 1,0]:
                self.dir = "North"
            elif self.pos == [self.width - 1,self.height - 1]:
                self.dir = "West"
            elif self.pos == [0,self.height - 1]:
                self.dir = "South"

            if self.dir == "East":
                self.pos[0] += 1
            elif self.dir == "West":
                self.pos[0] -= 1
            elif self.dir == "North":
                self.pos[1] += 1
            elif self.dir == "South":
                self.pos[1] -= 1
        if self.pos == [0,0]:
            self.dir = "South"

    def getPos(self) -> List[int]:
        return self.pos
        

    def getDir(self) -> str:
        return self.dir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()