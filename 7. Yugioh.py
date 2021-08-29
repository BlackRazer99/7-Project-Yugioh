#Yu-Gi-Oh!
#A simple version where I only have 5 cards in the deck and draw 1 at the start of the turn

#to shuffle the deck import random
import random

#to use the cards that are added, import own module where all monster cards are 
import Yugioh_Monstercards

#all cards in the deck (could have been another module, but wanted it here for visualization)
deck = [Yugioh_Monstercards.Killer_Bee[0],
        Yugioh_Monstercards.Iron_Wall[0],
        Yugioh_Monstercards.Commodo[0],
        Yugioh_Monstercards.Dark_Grapher[0],
        Yugioh_Monstercards.Mystic_Tomato[0]]

#randomize the Deck to not stack the cards
def deckShuffle():
    random.shuffle(deck)

deckShuffle()

#starting the game with 0 Cards in Hand
cardsHand = 0
#the number of cards in the deck is equal to its length
cardsDeck = len(deck)
#status to see both
status = cardsHand, cardsDeck
#which card is in the hand(at the start nothing)
hand = []

#standard draw Phase but some effects like pot of greed change it
def drawCards(x = 1):
    #change number of cards in hand
    global cardsHand
    cardsHand = cardsHand + x
    #change number of cards in deck
    global cardsDeck
    cardsDeck = cardsDeck - x
    #if there are less than 0 cards in the deck you lose the game (i.e overdraw)
    if cardsDeck < 0:
        print("You have no Cards left in the Deck, you lose!")
        exit()
    else:
        pass
    
    #update the status
    global status
    status = cardsHand, cardsDeck

    #changing the status of the cards in hand and deck(draw the card means removing it from deck) and showing you what you drew
    hand.append(deck[cardsDeck - cardsDeck])
    newCardDrawn = deck[cardsDeck - cardsDeck]
    deck.remove(deck[cardsDeck - cardsDeck])
    print("You drew ",newCardDrawn)

#turn begins
startTurn = True
while startTurn:
    drawCards()
    if cardsHand > 0 :
        print("Do you want to check the card in your Hand")
        check = input("Press yes \n")
        if check == "yes":
            for cardsChecking in hand:
                print(cardsChecking)
                if cardsChecking == "Killer Bee":
                    print(Yugioh_Monstercards.Killer_Bee)
                elif cardsChecking == "Iron Wall":
                    print(Yugioh_Monstercards.Iron_Wall)
                elif cardsChecking == "Commodo":
                    print(Yugioh_Monstercards.Commodo)
                elif cardsChecking == "Dark Grapher":
                    print(Yugioh_Monstercards.Dark_Grapher)
                elif cardsChecking == "Mystic Tomato":
                    print(Yugioh_Monstercards.Mystic_Tomato)
                else:
                    print("Failure there")               
        else:
            print("You don't want to check the cards")
    else:
        pass
    endTurn = input("go to End-Phase?\n")
    if endTurn == "yes":
        startTurn = False
        print("It's your opponents turn")

print("You have", cardsDeck, "cards left in the Deck")
print("You have", cardsHand, "cards in your Hand")
