class Car:
    speed = 0
    def upSpeed(self, value):
        self.speed += value

        print("현재 속도(Car) : %d km" % self.speed)

class Sedan(Car) :
    def upSpeed(self, value):
       self.speed += value

       if self.speed >= 150:
           self.speed = 150

       print("현재 속도(Sedan) : %d km" % self.speed)

class Truck(Car) :
    pass

sedan1, truck1 = None, None

class Sonata(Sedan):
   pass

truck1 = Truck()
sedan1 = Sedan()
sonata1 = Sonata()

print("트럭 -->", end="")
truck1.upSpeed(200)

print("세단 -->", end="")
sedan1.upSpeed(200)

print("소나타 -->", end="")
sonata1.upSpeed(200)