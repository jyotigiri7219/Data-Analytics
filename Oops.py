class Factory:
    def __init__(self,matrial,cycle,hero): #self is paeameter Factory to location call
        self.matrial =  matrial
        self.cycle =  cycle
        self.hero =  hero
        #print("this is a constructor use the")


obj = Factory("big cycle",2,3) # object created
obj2 = Factory("small cycle",4,5)

print(obj.matrial,obj2.matrial)