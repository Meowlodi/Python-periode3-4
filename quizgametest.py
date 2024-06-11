print("Welkom bij de quiz!")

playing = input("Wil je spelen? (ja of nee) ").lower()

if playing != "ja":
    print("Ik wou toch niet met je spelen!") 
    quit()

print("Oke! Laten we beginnen, geen spelfouten maken :)")
score = 0

answer = input("Wie is de beste docent van TCR Schiedamseweg? ").lower()
if answer == "jason":
    print('Correct!')
    score += 1
else:
    print("Incorrect! Het juiste antwoord is: Jason ")

answer = input("Wie is Jason zijn favoriete leerling? ").lower()
if answer == "melodi":
    print('Correct!')
    score += 1
else:
    print("Incorrect! Het juiste antwoord is: Melodi ")

answer = input("Wat is Jason zijn favoriete scripttaal? ").lower()
if answer == "javascript":
    print('Correct!')
    score += 1
else:
    print("Incorrect! Het juiste antwoord is: Javascript ")

answer = input("Welke docent geeft PHP? Alleen de achternaam graag! ").lower()
if answer == "berkhout":
    print('Correct!')
    score += 1
else:
    print("Incorrect! Het juiste antwoord is: Berkhout")

    answer = input("Waar staat PHP voor? ").lower()
if answer == "hypertext preprocessor":
    print('Correct!')
    score += 1
else:
    print("Incorrect! Het juiste antwoord is: Hypertext Preprocessor")

answer = input("Waar staat HTML voor? ").lower()
if answer == "hypertext markup language":
    print('Correct!')
    score += 1
else:
    print("Incorrect! Het juiste antwoord is: HyperText Markup Language")

answer = input("Waar staat SQL voor? ").lower()
if answer == "structured query language":
    print('Correct!')
    score += 1
else:
    print("Incorrect! Het juiste antwoord is: Structured Query Language ")

answer = input("Met welke scripttaal is deze quiz gemaakt? ").lower()
if answer == "python":
    print('Correct!')
    score += 1
else:
    print("Incorrect! Het juiste antwoord is: Python ")

doorgaan = input("Wil je verder spelen? (ja of nee) ").lower()

if doorgaan != "ja":
    print("Oke, hier is je score:")
print("Je hebt " + str(score) + " vragen correct!")
print("Je hebt " + str((score / 8) * 100) + "%.")

