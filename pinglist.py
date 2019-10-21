import os
import sys

# Standartliste der Links
linklist = ["google.de", "amazon.de", "orf.at"]
# Überprüft die Länge der eingegebenen Argumente; Dateiname ist Teil dieser Länge!
leng = len(sys.argv)

class bcolors:
    ok = '\033[92m'
    warning = '\033[91m'
    ENDC = '\033[0m'

# Conditions
# i = 1 wenn keine args vergeben
if leng == 1:
    i = 1
# Wenn ein oder mehrere args vergeben werde, wird i = die eimgegebene Zahl gesetzt
if leng >= 2:
    i = int(sys.argv[1])
# Die Argumente ab dem 2. eingegebenen Wert werden in die Liste eingefügt und überschreiben die Standartlinks
if leng >= 3:
    linklist = sys.argv[2:]

# Startwert für die Schleife
count = 0

while count < i:

    count = count + 1

    for link in linklist:

        ergebnis = os.system("ping -c 1 " + link + " > nul")

# Wenn der Server erreichbar ist, wird 0 ausgegeben
        if ergebnis == 0:
            print(bcolors.ok +"Ping zu " + link + " war erfolgreich!")
        else:
            print(bcolors.warning + "Ping zu " + link + " war nicht erfolgreich")
