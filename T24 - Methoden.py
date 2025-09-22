#Neben den Eigenschaften werden den Autos Funktionen wie 'fahren' durch Methoden zugewiesen

class car:
    def __init__(self):
        self.brand = None
        self.horse_pwr = None
        self.color = None
        self.x_pos = 5                  #Eindeutige Postion in X-Position
        self.y_pos = 5                  #Eindeutige Postion in Y-Position

    def drive(self, x, y):              #Bewegung in x- bzw. y-Richtung
        self.x_pos += x
        self.y_pos += y


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

car1.drive(7, 3)
print(car1.x_pos)           #Auto1 bewegt sich von 5 um 7 auf der x-Achse
print(car1.y_pos)

print(car2.x_pos)           #Auto2 ist weiterhin auf Position 5/5
print(car2.y_pos)