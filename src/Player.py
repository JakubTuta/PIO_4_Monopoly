class Player:
    def __init__(self, xPos = 0, yPos = 0, tokenColor = "white", moneyAvailable = 1500):
        self._currentTile = 0
        self.__xPos = xPos
        self.__yPos = yPos
        self.__tokenColor = tokenColor
        self.__moneyAvailable = moneyAvailable
        self.hasRolled = False
    
    def getPos(self):
        return (self.__xPos, self.__yPos)
    
    def getTokenColor(self):
        return self.__tokenColor
    
    def getMoneyAvailable(self):
        return self.__moneyAvailable
    
    def getCurrentTile(self):
        return self._currentTile

    def setCurrentTile(self, newTile):
        self._currentTile = newTile