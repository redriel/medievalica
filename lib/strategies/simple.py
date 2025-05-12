# The simplest strategy.
# If the opponent played an Emperor, it goes all out with Knights
# Otherwise, it just chills with Clerics

def select (myHand, myScore, currentRound, myStack, opponentStack):
    if ("Emperor" in opponentStack and "Knight" in myHand):
        card = "Knight"
    else:
        card = "Cleric"
    return card