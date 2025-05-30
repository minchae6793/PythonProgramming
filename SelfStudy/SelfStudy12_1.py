class Car :
    color = ""
    speed = 0

    def upSpeed(self, value):

        if self.speed >= 150:
            self.speed = 150

        else:
            self.speed += value

    def downSpeed(self, value):
        self.speed -= value

    def printMessage(self) :
        print("시험 출력이다.")

myCar = Car()
myCar.color = "빨강"
myCar.speed = 0

myCar2 = Car()
myCar2.color = "파랑"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "노랑"

myCar.upSpeed(30)
print("자동차의 색상은 %s 이고, 현재 속도는 %d km 입니다." % (myCar.color, myCar.speed))

myCar2.upSpeed(60)
print("자동차의 색상은 %s 이고, 현재 속도는 %d km 입니다." % (myCar2.color, myCar2.speed))

myCar3.upSpeed(0)
print("자동차의 색상은 %s 이고, 현재 속도는 %d km 입니다." % (myCar3.color, myCar3.speed))