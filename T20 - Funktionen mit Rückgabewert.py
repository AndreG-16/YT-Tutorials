#Es werden immer Werte von Funktionen wiedergegeben, wenn die Funktion aufgerufen wird
def say_hello(name):       
    print(print("Hallo " + name))   #       
    print("Willkommen zurück")

print(type(say_hello("Fabian")) )   #Funktion wird aufgerufen - 


#Beispiel 2 - Funktion mit 2 Zahlen, wobei das Maximum ermittelt werden soll

def maximum(a, b):           #die zwei Variablen a und b sollen verglichen werden
    if a < b:
        return b             #b ist größer als a
    else:
        return a             #a ist größer als b
    
result = maximum(8,3)

print(result)


