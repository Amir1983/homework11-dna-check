import datetime                     #hHier werder die benötigten Pakete für Datum und Uhrzeit
import json                         #Daten werden strukturiert und für Mensch und Maschine Lesbar gemacht
import random                       #Dies wird für den Zufallsgenerator benötigt

current_time = datetime.datetime.now()   #Genaueste Zeit und Datum Angabe

print(current_time)


secret = random.randint(1, 30)              #Zufallszahl zwischen 1 und 30 generieren
attempts = 0                                #Versuche werden zunächst auf 0 gesetzt
username = input("Geben Sie bitte ihren Namen ein: ")       #Hier gibt der Spieler seinen Namen ein
name = username
wrong_guesses = []                  #Leere Liste für die falschen Versuche



with open("score_list.txt", "r") as score_file:             #Hier wird die score_list.txt Textdatei geöffnet

    score_list = json.loads(score_file.read())


    print("Top3 Highscore:")

    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]        # Mit diesem Befehl wird der Dictionary
                                                                                # sortiert und auf die ersten 3 beschränkt
for score_dict in top_score_list:                                               # Dies ist eine for schleife bei dem die ersten 3 der liste gezeigt werden
    print("Wrong: " + str(score_dict["wrong"]), "Secretnumber: " + str(score_dict["secretnumber"]), " Name: " + str(score_dict["username"]) + ", " + str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    score_data = {"wrong": wrong_guesses, "secretnumber": secret, "username": name, "attempts": attempts, "date": datetime.datetime.now()}


while True:

    guess = int(input("Guess the secret number (between 1 and 30): "))          #Eingabe der Zahl des Spielers
    attempts += 1                                                               #Hier wird nach jedem Versuch um 1 hoch gerechnet



    if guess == secret:     # wenn diese Bedingung erfüllt ist, dann füge der Liste die angegebenen Daten hinzu und beende das Programm
        score_list.append({"wrong": wrong_guesses, "secretnumber": secret, "username": name, "attempts": attempts, "date": str(datetime.datetime.now())})
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret and guess != secret:
        print("Your guess is not correct... try something smaller")
        wrong_guesses.append(guess)
    elif guess < secret and guess != secret:
        print("Your guess is not correct... try something bigger")
        wrong_guesses.append(guess)


