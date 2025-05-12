# Your name:
# Your strategy name:
#
# You and your opponent start with 8 cards in hand
# 5 Clerics, 2 Knights and 1 Emperor
# You play one card per round, for 5 rounds.
# Each time, the players get points according to the rules:
#
# i. Cleric v Cleric ......... 1 point to each player
# ii. Knight v Cleric ........ 2 points to the Knight player, 0 to the Cleric player
# iii. Emperor v Knight ...... 4 points to the Emperor player, 0 to the Knight player
# iv. Other combinations ..... 0 points to each player
#
# Your goal is to get as many points as possible.
# You have to come up with a strategy that can perform well againts all kinds of opponents.
# This will include facing your own strategy and a random strategy.
# You may devise your strategy as you like, but keep in mind:
#
# i. it cannot be fully non-deterministic nor random.
# ii. it should pick only cards currently in your hand.
# iii. it should always pick a card
#
# This is the method to implement your strategy.
# These arguments represent the game status and are useful for creating you own strategy:
#
# myHand .............. list of cards in your hand
# myScore ............. your current score
# currentRound ........ current round (starts at 1 and goes up to 5)
# myStack ............. list of cards you played (in chronological order, starts empty)
# opponentStack ....... list of cards your opponent played (in chronological order, starts empty)

def select (myHand, myScore, currentRound, myStack, opponentStack):
    
    # Your code goes here
    card = "Cleric"
    return card
