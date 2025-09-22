#Im Folgenden wird ein Auto modelliert

class car:
    def __init__(self):
        self.brand = None
        self.horse_pwr = None
        self.color = None

#1. Objekt
car1 = car()
car1.brand = "Mercedes"
car1.horse_pwr = 250
car1.color = "red"

#2. Objekt 
car2 = car()
car2.brand = "BMW"
car2.horse_pwr = 210
car2.color = "black"

car3 = car1             #car3 nimmt Referenz auf car1

print(car1)             #es werden nicht die einzelnen Attribute ausgegeben sondern die Adresse, wo die Information abgelegt ist
print(car2)
print(car3)
print(car1.horse_pwr)
print(car3.horse_pwr)       #car3 hat damit den gleichen Wert wenn es um das Attribut horse_pwr geht