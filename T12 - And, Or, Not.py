#Logische Operatoren and, or, not

#In der umständliche Variante ohne logische Operatoren:
print("Willkommen in der Lotterie!")

number1 = int(input("Bitte wähle eine Zahl zwischen 1 und 49: "))
number2 = int(input("Bitte wähle eine weitere Zahl zwischen 1 und 49: "))
number3 = int(input("Bitte wähle eine letzte Zahl zwischen 1 und 49: "))

#Gewinnerzahlen: 3, 14, 22

if number1 == 3:
    if number2 == 14:
        if number3 == 22:
            print("Herzlichen Glückwunsch, du hast die Lotterie gewonnen!")
        else:
            print("Du hast leider verloren.")
    else:
        print("Du hast leider verloren.")
else:
    print("Du hast leider verloren.")

#mit logischen Operatoren
if number1 == 3 and number2 == 14 and number3 == 22:
    print("Herzlichen Glückwunsch, du hast die Hauptzahlen richtig!")

    #Für den Jackpot
    superzahl = int(input("Bitte wähle eine Superzahl zwischen 0 und 9: "))
    #Superzahl = 7

    if not superzahl == 7:
        print("Das ist leider falsch, aber du hast den Hauptgewinn gewonnen!")
    else:
        print("Herzlichen Glückwunsch, du hast auch die Superzahl getroffen und den Jackpot gewonnen!")
else:
    print("Du hast leider verloren...")

age = int(input("Du kannst deinen Gewinn nur abholen, wenn du volljährig bist. Bitte dein Alter eingeben: "))
if age == 18 or age >18:
    print("Du darfst das Geld behalten.")
else:
    print("Du bist leider zu jung um Lotte zu spielen")
