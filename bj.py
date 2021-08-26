import random

deck = []
suite = ["2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10", "J ", "Q ", "K ", "A "]
valueForNumsAceAs1 = {"2 ": 2, "3 ": 3, "4 ": 4, "5 ": 5, "6 ": 6, "7 ": 7, "8 ": 8, "9 ": 9, "10": 10, "J ": 10,
                      "Q ": 10, "K ": 10, "A ": 1}
valueForNumsAceAs11 = {"2 ": 2, "3 ": 3, "4 ": 4, "5 ": 5, "6 ": 6, "7 ": 7, "8 ": 8, "9 ": 9, "10": 10, "J ": 10,
                       "Q ": 10, "K ": 10, "A ": 11}

# this creates a whole deck of playing cards

for i in range(len(suite)):
    deck.append(("♦", suite[i]))

for i in range(len(suite)):
    deck.append(("♠", suite[i]))

for i in range(len(suite)):
    deck.append(("♥", suite[i]))

for i in range(len(suite)):
    deck.append(("♣", suite[i]))


# this function prints out the card pairs (player/dealer)
# the hiddenDL variable is able to display a "hidden card" which only shows a "?"

def printCard(suitePL, numberPL, suiteDL, numberDL, hiddenDL):
    if hiddenDL == 1:
        numberDL = "  "
        suiteDL = "?"

    print(" ---------                 ---------")
    print("|%s       |               |%s       |" % (numberPL, numberDL))
    print("|         |               |         |")
    print("|    %s    |               |    %s    |" % (suitePL, suiteDL))
    print("|         |               |         |")
    print("|       %s|               |       %s|" % (numberPL, numberDL))
    print(" ---------                 ---------")


# this checks whether counting aces as 1 or 11 gives the player a higher score and returns the better option

def whichAceBetterFunc(a1, a11):
    if a1 > 21 and a11 > 21:
        return "bust"
    else:
        if a1 == 21 or a11 == 21:
            return "Blackjack"
        elif a1 < 21 and a11 < 21:
            if 21 - a1 < 21 - a11:
                return a1
            else:
                return a11
        elif a1 < 21:
            return a1
        else:
            return a11


# this checks for every possible game outcome and tells the player whether they`ve won or not

def gameOutcome(pS, dS):
    if pS == "bust":
        print("You lost. Too bad :(")
        return
    elif pS == "Blackjack" and dS != "Blackjack":
        print("Congratulations! You won!")
        return
    elif dS == "Blackjack" and pS != "Blackjack":
        print("You lost. Too bad :(")
        return
    elif (pS == "Blackjack" and dS == "Blackjack"):
        print("Wow a tie. Want a remacht?")
        return
    elif pS == dS:
        print("Wow a tie. Want a remacht?")
        return
    elif 21 - pS < 21 - dS:
        print("Congratulations! You won!")
        return
    else:
        print("You lost. Too bad :(")
        return


def blackjackGame():
    print("Hello! Welcome to the Blackjacktable! If you wish to be a dealt another card, type: \"Card\" \n"
          "If you want to call, type \"Call\"")
    playerCards = []
    dealerCards = []

    # dealing first and showing first cards
    for x in range(2):
        playerCards.append(random.choice(deck))
        dealerCards.append(random.choice(deck))

    printCard(*playerCards[0], *dealerCards[0], 0)
    printCard(*playerCards[1], *dealerCards[1], 1)

    round = 1

    # gameloop

    while True:

        # this block gives the player and dealer another card

        if input() == "Card":
            playerCards.append(random.choice(deck))
            dealerCards.append(random.choice(deck))
            printCard(*playerCards[round + 1], *dealerCards[round + 1], 1)

            round = round + 1

        # this block ends the game and returns the result

        elif input() == "Call":
            scorePL = []
            scorePLN1 = []
            scorePLN11 = []
            scoreDL = []
            scoreDLN1 = []
            scoreDLN11 = []

            # getting scores from cardnumbers and creating list for either ace=11 or ace=1

            for i in playerCards:
                scorePL.append(i[1])

            for x in dealerCards:
                scoreDL.append(x[1])

            for i in scorePL:
                scorePLN1.append(valueForNumsAceAs1[i])
            for i in scorePL:
                scorePLN11.append(valueForNumsAceAs11[i])

            scorePLN1 = sum(scorePLN1)
            scorePLN11 = sum(scorePLN11)

            for i in scoreDL:
                scoreDLN1.append(valueForNumsAceAs1[i])
            for i in scoreDL:
                scoreDLN11.append(valueForNumsAceAs11[i])

            scoreDLN1 = sum(scoreDLN1)
            scoreDLN11 = sum(scoreDLN11)

            playerScore = whichAceBetterFunc(scorePLN1, scorePLN11)

            dealerScore = whichAceBetterFunc(scoreDLN1, scoreDLN11)

            # checking the game outcome
            print("The game ended in round:", round)
            print("Here you can see all the cards")
            for i in range(len(playerCards)):
                printCard(*playerCards[i], *dealerCards[i], 0)

            gameOutcome(playerScore, dealerScore)
            exit()

        # catching typos

        else:
            print("Either type \"Card\" to be dealt a new card or \"Call\" to call the game")



