import random

# It just picks a random card in hand
# What a chad

def select (myHand, myScore, currentRound, myHistory, opHistory):
        card = random.choice(myHand)
        return card