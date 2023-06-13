class Player:
    def __init__(self, xPos = 0, yPos = 0, tokenColor = "white", moneyAvailable = 200, sumOfBought = 0):
        self._currentTile = 0
        self.__xPos = xPos
        self.__yPos = yPos
        self.__tokenColor = tokenColor
        self.__moneyAvailable = moneyAvailable
        self.hasRolled = False
        self.__sumOfBought = sumOfBought

    def getPos(self):
        return (self.__xPos, self.__yPos)
    
    def getTokenColor(self):
        return self.__tokenColor
    
    def getMoneyAvailable(self):
        return self.__moneyAvailable
    
    def addMoney(self, amount):
        self.__moneyAvailable += amount

    def subMoney(self, amount):
        self.__moneyAvailable -= amount

    def getCurrentTile(self):
        return self._currentTile

    def setCurrentTile(self, newTile):
        self._currentTile = newTile

    def addToSumOfBought(self, amount):
        self.__sumOfBought +=amount
    def getSumOfBought(self):
         return self.__sumOfBought