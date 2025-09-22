#Im Gegensatz zu Variablen, können bei Listen mehrere Werte gespeichert werden

names = ["Caro", "Lea", "Svea", "Finja", 4, 8.2]          #Variablen in eckigen Klammern und mit einem Komma getrennt
print(names)

print(names[2])                                 #Auswahl eines Wertes innerhalb einer Liste -> 2 = 3. Stelle, da 0 = Caro ist

print(names[-3])                                #Auswahl von Hinten der Liste beginnend mit -1

names[0] = "Caroline Neuser"                    #Aus der Liste wird der 1. Wert "Caro" mit "Caroline Neuser" ersetzt

print(names)