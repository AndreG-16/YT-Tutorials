#2 Anwendungsfälle
#1. Iterierbare Objekte einer Liste werden nacheinander durchlaufen

for element in [1, 3, 5, 7, "Hans"]:
    print(element)

for element in "Der Hund":
    print(element)

#2. Als Zählerschleife
for element in range(5):               #Zahlen von 0 bis 9 werden wiedergegeben
    print(element)

for element in range(2, 5):            #Zahlen von 5 bis 9 werden wiedergegeben
    print(element)

for element in range (2, 8, 2):        #Zahlen von 2 bis 8 werden in Schritten von 2 wiedergegeben
    print(element)


