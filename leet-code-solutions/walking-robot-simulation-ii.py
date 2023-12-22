class Robot:

    def __init__(self, width: int, height: int):
        self.car_point = ["East", "North", "West", "South"]
        self.dir = 0 # gets the direction from self.car_point (for easy manipulation)
        self.pt = [0,0]
        self.tot_step = 2*(width+height) - 4
        self.dimension = [width, height]


    def step(self, num: int) -> None:
        num %= self.tot_step

        #checks if the truncated steps = 0 and it is at its initial point to face south.
        if num == 0 and self.pt == [0,0]:
            self.dir = 3
        
        #it will do the iteration of steps till the remaining steps runs out
        while num > 0:
            increment = 0
            if self.dir == 0: #East direction iteration
                if num+self.pt[0] >= self.dimension[0]:
                    increment = self.dimension[0] - self.pt[0] - 1
                    self.pt[0]+=increment
                    self.dir = 1
                    num-=increment
                else:
                    self.pt[0]+=num
                    break

            if self.dir == 1: #North direction iteration
                if num+self.pt[1] >= self.dimension[1]:
                    increment = self.dimension[1] - self.pt[1] - 1
                    self.pt[1]+=increment
                    self.dir = 2
                    num-=increment
                else:
                    self.pt[1]+=num
                    break

            if self.dir == 2: # West direction iteration
                if self.pt[0]-num < 0:
                    increment = self.pt[0]
                    self.dir = 3
                    num-=increment
                    self.pt[0] = 0
                else:
                    self.pt[0]-=num
                    break

            if self.dir == 3: #south direction iteration
                if self.pt[1] - num < 0:
                    increment = self.pt[1]
                    self.dir = 0
                    num-=increment
                    self.pt[1] = 0
                else:
                    self.pt[1]-=num
                    break

    def getPos(self) -> List[int]:
        return self.pt
        

    def getDir(self) -> str:
        return self.car_point[self.dir]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()