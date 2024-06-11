import random

def quiz_game():
    print("Welkom bij de quiz!")
    playing = input("Wil je spelen? (ja of nee) ").lower()

    if playing != "ja":
        print("Ik wou toch niet met je spelen!") 
        return "stop"

    print("Oke! Laten we beginnen, er zijn 8 vragen en je mag geen spelfouten maken :). Als je wilt stoppen mag je het woord 'stop' invullen.")
    score = 0

    questions = [
        ("Wie is de beste docent van TCR Schiedamseweg?", "jason"),
        ("Wie is Jason zijn favoriete leerling?", "melodi"),
        ("Wat is Jason zijn favoriete scripttaal?", "javascript"),
        ("Welke docent geeft PHP? Alleen de achternaam graag!", "berkhout"),
        ("Waar staat PHP voor?", "hypertext preprocessor"),
        ("Waar staat HTML voor?", "hypertext markup language"),
        ("Waar staat SQL voor?", "structured query language"),
        ("Met welke scripttaal is deze quiz gemaakt?", "python")
    ]

    for question, correct_answer in questions:  # Loop door de lijst van vragen en juiste antwoorden
        answer = input(question + " ").lower()  # Vraag de vraag en zet de invoer om naar kleine letters
        if answer == "stop":  # Controleer of de invoer 'stop' is
            return "stop"  # Spel stoppen
        if answer == correct_answer:  # Controleer of het antwoord juist is
            print('Correct!')  # Juist bericht
            score += 1  # Score verhogen
        else:
            print(f"Incorrect! Het juiste antwoord is: {correct_answer.capitalize()}")  # Incorrect bericht

    print("Je hebt " + str(score) + " vragen correct!")  # Eindscore tonen
    print("Je hebt " + str((score / 8) * 100) + "%.")  # Percentage correcte antwoorden tonen
    doorgaan = input("Wil je een ander spel spelen? (ja of nee) ").lower()  # Vragen of de speler verder wil spelen
    if doorgaan == "ja":
        return "continue"  # Verder spelen
    else:
        return "stop"  # Spel stoppen

def number_guessing_game():
    print("Welkom bij het Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        user_guess = input("Raad het getal (tussen 1 en 100) of typ 'stop' om te stoppen: ").lower()
        
        if user_guess == "stop":  # Controleer of de invoer 'stop' is
            return "stop"  # Spel stoppen
        
        if not user_guess.isdigit():  # Controleer of de invoer een getal is
            print("Voer alstublieft een geldig getal in.")  # Ongeldig getal bericht
            continue
        
        user_guess = int(user_guess)  # Zet de invoer om naar een geheel getal
        attempts += 1  # Pogingen verhogen
        
        if user_guess < number_to_guess:  # Controleren of het getal te laag is
            print("Te laag! Probeer opnieuw.")  # Bericht als het getal te laag is
        elif user_guess > number_to_guess:  # Controleren of het getal te hoog is
            print("Te hoog! Probeer opnieuw.")  # Bericht als het getal te hoog is
        else:
            print(f"Gefeliciteerd! Je hebt het juiste getal {number_to_guess} geraden in {attempts} pogingen.")  # Juist bericht
            break  # Verlaat de loop

    doorgaan = input("Wil je een ander spel spelen? (ja of nee) ").lower()  # Vragen of de speler verder wil spelen
    if doorgaan == "ja":
        return "continue"  # Verder spelen
    else:
        return "stop"  # Spel stoppen

def main_menu():
    while True:
        print("\nKies een spel om te spelen:")  # Hoofdmenu tonen
        print("1. Quiz Game")  # Optie 1: Quiz Game
        print("2. Number Guessing Game")  # Optie 2: Number Guessing Game
        print("3. Quit")  # Optie 3: Stoppen

        choice = input("Voer je keuze in (1, 2, of 3): ").lower()  # Vraag om een keuze

        if choice == "1":
            result = quiz_game()  # Start Quiz Game
        elif choice == "2":
            result = number_guessing_game()  # Start Number Guessing Game
        elif choice == "3" or choice == "stop":
            result = "stop"  # Spel stoppen
        else:
            print("Ongeldige keuze. Probeer het opnieuw.")  # Ongeldige keuze bericht
            continue
        
        if result == "stop":
            print("Bedankt voor het spelen! Tot ziens!")  # Bedankt bericht
            break  # Verlaat de loop

# Start het programma met het hoofdmenu
main_menu()  # Hoofdmenu functie aanroepen