class Gadget:
    def __init__(self,name,power,function):
        self.name=name
        self.power=power
        self.function=function
    def use_gadget(self):
        print(f'Gadget: {self.name} | Power: {self.power} | Function: {self.function}')
        print(f'Doraemon uses {self.name} -> {self.function}!')
g1 = Gadget("Anywhere Door", 95, "Travel anywhere instantly")
g2 = Gadget("Time Machine", 100, "Travel through time")
g3 = Gadget("Bamboo Copter", 80, "Fly in the sky")
g1.use_gadget()
g2.use_gadget()
g3.use_gadget()
