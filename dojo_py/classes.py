class Robot:

    def __init__(self,given_name,given_color,given_weight):
        self.name=given_name
        self.color=given_color
        self.weight=given_weight


    def introduce_self(self):
        print (f"my name is {self.name}")



r1=Robot("Tom", "red", 40)
r2=Robot("Jerry", "blue", 30)
# print(r1.introduce_self())



class Person:
    def __init__(self, name, personality, isSitting, robotOwned) -> None:
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
        self.robotOwned = robotOwned

    def sit_down(self):
        self.isSitting = True


    def stand_up(self):
        self.isSitting = False


p1 = Person("Alice", "Aggressive", False, r2)
p2 = Person("Becky", "Talkative", True, r1)




print(f"Hello {p1.name}, are you sitting?  : {p1.isSitting}")
p1.sit_down()
print(f"How about now? : {p1.isSitting}")
p2.robotOwned.introduce_self()

print("")

print(f"Hello {p2.name}, are you standing?  : {p2.isSitting}")
p2.stand_up()
print(f"How about now? : {p2.isSitting}")

p1.robotOwned.introduce_self()