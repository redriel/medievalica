from lib import player
from prettytable import PrettyTable
import os

# function to assign points after each player plays a card
def battle(cardP1, cardP2, playerOne, playerTwo, currentRound):
    if (cardP1 == cardP2 == "Cleric"):
        playerOne.scoreUpdate(1)
        playerTwo.scoreUpdate(1)
    elif (cardP1 == "Emperor" and cardP2 == "Knight"):
        playerOne.scoreUpdate(4)
    elif (cardP1 == "Knight" and cardP2 == "Emperor"):
        playerTwo.scoreUpdate(4)
    elif (cardP1 == "Knight" and cardP2 =="Cleric"):
        playerOne.scoreUpdate(2)
    elif (cardP1 == "Cleric" and cardP2 == "Knight"):
        playerTwo.scoreUpdate(2)
    # handling the edge cases when a player plays an invalid card
    elif (cardP1 == "Penalty" and cardP2 != "Penalty"):
        playerOne.scoreUpdate(-4*(5 - currentRound))
        currentRound = 5
    elif (cardP1 != "Penalty" and cardP2 == "Penalty"):
        playerTwo.scoreUpdate(-4*(5 - currentRound))
        currentRound = 5
    elif (cardP1 == "Penalty" and cardP2 == "Penalty"):
        playerOne.scoreUpdate(-4*(5 - currentRound))
        playerTwo.scoreUpdate(-4*(5 - currentRound))
        currentRound = 5
    # catch all that does nothing
    else:
        return

currentRound = 1
pointList = []
strategyList = []

# fetching all strategies in folder
for (root, dirs, file) in os.walk("./lib/strategies"):
    for f in file:
        if '.py' in f and 'yourStrategy' not in f:
            strategyList.append(f.replace(".py", ""))
    break

# running each strategy against itself and others strategies multiple times (100)
for i, strategy in enumerate(strategyList):
    playerOne = player.Player(strategyList[i])
    for j, strategy in enumerate(strategyList):
        playerTwo = player.Player(strategyList[j])
        for x in range (1, 101):
            for x in range(1, 6):
                cardP1 = playerOne.play()
                cardP2 = playerTwo.play()
                battle(cardP1, cardP2, playerOne, playerTwo, currentRound)
                currentRound = currentRound + 1
                playerOne.update(playerTwo.myStack, currentRound)
                playerTwo.update(playerOne.myStack, currentRound)
            currentRound = 1
            playerOne.refresh()
            playerTwo.refresh()
    pointList.append((playerOne.name, playerOne.scoreUpdate()))

# plotting in a table every strategy, its points and efficiency
n = len(strategyList)
pointList.sort(key=lambda a: a[1], reverse = True)
t = PrettyTable(['Strategy', 'Points', 'Efficiency'])
for strategy in pointList:
   t.add_row((strategy[0], strategy[1], "{:.2f}".format((strategy[1] * 100) / (1000 * n))+"%"))
t.align = "r"
print(t)