#Funktionen ermöglichen bessere Strukturierungen - Funktion = Unterprogramm
#Beispiel print

def say_hello():                    #Anweisung definieren
    print("Hallo Lisa")
    print("Willkommen zurück")

say_hello()                         #Funktion wird aufgerufen
print("Test")
say_hello()                         #Funktion wird erneut aufgerufen

#Für Funktionen Parameter definieren -> damit einzelne Teile einer Funktion flexibel angepasst werden können

def say_hello(name):       
    print("Hallo " + name)          #Parameter 'name' kann angepasst werden
    print("Willkommen zurück")

say_hello("Fabian")                 #Parameter name wird der Wert 'Fabian' zugewiesen

#2 Parameter:

def say_hello(name, last_name):                     #Reihenfolge ist wichtig
    print("Hallo " + name + " " + last_name)          
    print("Willkommen zurück")

say_hello("Erik", "Svenson")