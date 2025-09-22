#If-Anweisungen
age = int(input("Bitte dein Alter eingeben: "))

if age < 18:
    print("Achtung, der Nutzer ist jünger als 18")

elif age == 18:
    print("Der Nutzer ist exakt 18")

elif age == 100:
    print("Der Nutzer ist exakt 100")

else:
    print("Der Nutzer ist volljährig")

print("Programmende")

