# It starts strong with Knights in the first two round
# Then it checks if the opponent didn't play Knight and tries to capitalize with the Emperor
# Otherwise, it tosses Clerics
# Truly a maniac.

def select (myHand, myScore, currentRound, myStack, opponentStack):
    if (currentRound < 3):
        card = "Knight"
    elif (currentRound >= 3 and "Knight" not in opponentStack and "Emperor" in myHand):
        card = "Emperor"
    else:
        card = "Cleric"
    return card