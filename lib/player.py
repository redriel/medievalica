import importlib

#player class
class Player:
    def __init__(self, strategy):
        self.strategy = importlib.import_module("lib.strategies." + strategy)
        self.name = strategy
        self.score = 0
        self.hand = 5 * ["Cleric"] + 2 * ["Knight"] + ["Emperor"]
        self.myStack = []
        self.opponentStack = []
        self.currentRound = 1

    #play a card in your hand
    def play(self):
        select = getattr(self.strategy, "select")
        opponentStack = self.opponentStack[:]
        if(len(self.opponentStack) > len(self.myStack)):
            opponentStack.pop()
        card = select(self.hand, self.score, self.currentRound, self.myStack, opponentStack)
        if(card in self.hand):
            self.hand.remove(card)
            self.myStack.append(card)
        else:
            card = "Penalty"
        return card

    #look and update your score
    def scoreUpdate(self, points = 0):
        self.score = self.score + points
        return self.score

    #update
    def update(self, opponentStack, currentRound):
        self.opponentStack = opponentStack
        self.currentRound = currentRound

    def refresh(self):
        self.hand = 5 * ["Cleric"] + 2 * ["Knight"] + ["Emperor"]
        self.myStack = []
        self.opponentStack = []
        self.currentRound = 1