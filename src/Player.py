import pygame
import os

class Player:
    def __init__(self, WIN, id, xPos=0, yPos=0, tokenColor="white", moneyAvailable=1500):
        self.__xPos = xPos
        self.__yPos = yPos
        self.__tileWidth = 20
        self.__tileHeight = 32
        self.__tokenColor = tokenColor
        self.__moneyAvailable = moneyAvailable
        self.__WIN = WIN
        self.__id = id
        self.__icon = pygame.image.load(os.path.join("assets", f"Type={self.__tokenColor}.png")).convert_alpha()

    def getPos(self):
        return (self.__xPos, self.__yPos)

    def getTokenColor(self):
        return self.__tokenColor

    def getMoneyAvailable(self):
        return self.__moneyAvailable

    def draw(self):
        if self.__id == 0:
            self.__WIN.blit(self.__icon, (self.__xPos * self.__tileWidth + 15, self.__yPos * self.__tileHeight + 15))
        elif self.__id == 1:
            self.__WIN.blit(self.__icon,
                            (self.__xPos * self.__tileWidth + 15 + 40, self.__yPos * self.__tileHeight + 15))
        elif self.__id == 2:
            self.__WIN.blit(self.__icon,
                            (self.__xPos * self.__tileWidth + 15, self.__yPos * self.__tileHeight + 40 + 15))
        else:
            self.__WIN.blit(self.__icon,
                            (self.__xPos * self.__tileWidth + 15 + 40, self.__yPos * self.__tileHeight + 40 + 15))