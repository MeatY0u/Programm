import random

def generate_password(tastatur):
    counter = 0
    password_lenght = random.randint(8,32)
    password = ""
    while counter != password_lenght:
        password = random.choice(tastatur) + password
        counter = counter + 1
    return password

with open("Grossbuchstaben.txt") as f:
    grossbuchstaben = f.read().lstrip()
with open("Kleinbuchstaben.txt") as f:
     kleinbuchstaben = f.read().lstrip()
with open("Sonderzeichen.txt") as f:
    sonderzeichen = f.read().lstrip()
with open("Zahlen.txt") as f:
    zahlen = f.read().lstrip()

zeichen = list(zahlen) + list(sonderzeichen) + list(kleinbuchstaben) + list(grossbuchstaben)





richtig = True

while richtig == True:
    schlüssel = generate_password(zeichen)
    anzahl_sonderzeichen = len(set(list(schlüssel)) & set(sonderzeichen))
    anzahl_grossbuchstaben = len(set(list(schlüssel)) & set(grossbuchstaben))
    anzahl_kleinbuchstaben = len(set(list(schlüssel)) & set(kleinbuchstaben))
    anzahl_zahlen = len(set(list(schlüssel)) & set(zahlen))
    if anzahl_sonderzeichen == 0 or anzahl_grossbuchstaben == 0 or anzahl_kleinbuchstaben == 0 or anzahl_zahlen == 0:
        schlüssel = generate_password(zeichen)
    else:
        print("Hier ist dein Password: " + schlüssel)
        richitg = False
        break







print("Zahlen im Passwort: ", anzahl_zahlen)
print("Sonderzeichen im Passwort: ", anzahl_sonderzeichen)
print("Grossbuchstaben im Passwort: ", anzahl_grossbuchstaben)
print("Kleinbuchstaben im Passwort: ", anzahl_kleinbuchstaben)
