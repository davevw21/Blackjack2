import requests
from pprint import pprint
import json

#ask for name and deck deck_count
name = input("Please enter your name:")
dc = input("How many decks would you like?")

#shuffle the decks

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6"

payload={}
headers = {
'Accept': 'application/json'
}
response = requests.request("GET", url, headers=headers, data=payload)
deckJson = response.json()
id = deckJson['deck_id']

player = []
dealer = []

#values
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'JACK': 10, 'QUEEN': 10, 'KING': 10}

#function to draw cards
def draw():
    url = "https://deckofcardsapi.com/api/deck/" + id + "/draw/?count=2"

    payload={}
    headers = {
        'accept': 'application/json'
    }

    drawresponse = requests.request("GET", url, headers=headers, data=payload)
    handJson = drawresponse.json()
    cards = handJson['cards']

    for c in range(len(cards)):
        return(cards[c]["value"])


player.append(draw())
dealer.append(draw())
player.append(draw())
dealer.append(draw())

print("The cards have been dealt, here is your hand " + str(player) + " .")
print("The dealers hand is showing a " + str(dealer[1]) + " .")

#Gets the sum of the cards in the players hand.
def values(hand):
    total = 0
    for card in hand:
        if card == "JACK" or card == "QUEEN" or card == "KING" or card == "10":
            total+= 10
        elif card == "2":
            total+= 2
        elif card == "3":
            total+= 3
        elif card == "4":
            total+= 4
        elif card == "5":
            total+= 5
        elif card == "6":
            total+= 6
        elif card == "7":
            total+= 7
        elif card == "8":
            total+= 8
        elif card == "9":
            total+= 9
        elif card == "ACE":
            if total >= 11: total+= 1
            else: total+= 11
        else:
            total+= card
    return total

psum = values(player)
dsum = values(dealer)

#Rules to handle a Blackjack for dealer, player, or both.
if int(psum) == 21 and int(dsum) == 21:
    print("Player Hand " + str(values(player)) + ".")
    print("Dealer Hand " + str(values(dealer)) + ".")
    print("Its a push")
elif psum == 21:
    print("Player Hand " + str(values(player)) + ".")
    print("Dealer Hand " + str(values(dealer)) + ".")
    print("Congratulations, You got a blackjack, You win!!")
    quit()
elif dsum == 21:
    print("Player Hand " + str(values(player)) + ".")
    print("Dealer Hand " + str(values(dealer)) + ".")
    print("Sorry, you lose.  The dealer Got a blackjack.")
    quit()

#What to do if the player hand does not equal 21
while psum != 21:
    values(player)
    if int(values(player)) > 21:
        print("Player Hand " + str(values(player)) + ".")
        print("Dealer Hand " + str(values(dealer)) + ".")
        print("Sorry, you lose, you busted")
        quit()
    elif psum < 21:
        print("The sum of your cards is " + str(values(player)) + " would you like to hit or stay?")
        choice = input("Please press h for hit or s for stay then press enter.")
        if choice == "h":
            h = player.append(draw())
            print("Player Hand " + str(player) + ".")
        elif choice == "s":
            break
    else:
        break


#Rules for the dealer hand
while values(dealer) != 21:
    if values(dealer) < 17:
        break
    elif values(dealer) < 21:
        print("Sorry, You lose, You busted")
        break
    else:
        dealer.append(draw())
        if values(dealer) > 17:
            break

#Scoring of the hand after all other requirements are met. 
if values(player) == 21:
    print("Player hand " + str(player) + ".")
    print("Dealer hand " + str(dealer) + ".")
    print("Congratulations, You Got Blackjack!!  You Win!!")
elif values(player) == 21:
    print("Player hand " + str(player) + ".")
    print("Dealer hand " + str(dealer) + ".")
    print("Sorry you lose, the dealer got a Blackjack")
elif values(player) > 21:
    print("Player hand " + str(player) + ".")
    print("Dealer hand " + str(dealer) + ".")
    print("sorry, You busted.  You Lose.")
elif values(dealer) > 21:
    print("Player hand " + str(player) + ".")
    print("Dealer hand " + str(dealer) + ".")
    print("You win.  Dealer Busted")
elif values(player) < values(dealer):
    print("Player hand " + str(player) + ".")
    print("Dealer hand " + str(dealer) + ".")
    print("sorry, Dealer wins.")
elif values(player) > values(dealer):
    print("Player hand " + str(player) + ".")
    print("Dealer hand " + str(dealer) + ".")
    print("You win!!!.")
else:
    Print("Fix the code")
