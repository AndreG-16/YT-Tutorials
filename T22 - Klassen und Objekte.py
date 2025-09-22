#Im Folgenden wird ein Auto modelliert

class car:
    def __init__(self):
        self.brand = None
        self.horse_pwr = None
        self.color = None

car1 = car()

print(car1.brand)               #Hier wird der Wert 'None' ausgegeben, da kein Wert zugewiesen wurd

#1. Objekt (Auto) wird konfiguriert
car1.brand = "Mercedes"
car1.horse_pwr = 250
car1.color = "red"

print(car1.brand)
print(car1.horse_pwr)
print(car1.color)

#2. Objekt wird konfiguriert - gleiche Attribute aber andere Werte
car2 = car()
car2.brand = "BMW"
car2.horse_pwr = 210
car2.color = "black"

print(car2.brand)
print(car2.horse_pwr)
print(car2.color)