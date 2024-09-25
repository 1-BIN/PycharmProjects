class Animal:
    def __init__(self, name):
        self.name  = name
    def speak(self):
        pass
    def move(self):
        print("move move!!")

class Dog(Animal):  #상속 받음, 다중 상속 가능
    def __init__(self, name, breed):
        # super 부모 클래스
        super().__init__(name)
        self.breed = breed
    def speak(self):    #오버라이딩
        print("bark bark!!")
dog1 = Dog("라이코스", "닥스훈트")
dog2= Dog("바미", "보더콜리")
print(dog1.name)
print(dog2.name)
dog1.speak()
dog2.move()