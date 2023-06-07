class Player:
    def __init__(self, xPos = 0, yPos = 0, tokenColor = "white", moneyAvailable = 1500):
        self.xPos = xPos
        self.yPos = yPos
        self.color = tokenColor
        self.moneyAvailable = moneyAvailable
        self.hasRolled = False