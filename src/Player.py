import pygame
import os

from Tile import BOARD_SIZE, TILE_SIZE, WINDOW_SIZE

class Player:
    def __init__(self, xPos = 0, yPos = 0, tokenColor = "white", moneyAvailable = 1500):
        self.__xPos = xPos
        self.__yPos = yPos
        self.__tokenColor = tokenColor
        self.__moneyAvailable = moneyAvailable
        self.image = pygame.image.load(os.path.join("assets", f"Type={self.__tokenColor}.png"))  # Ścieżka do pliku graficznego gracza
        
        # Ograniczenia ruchu na obrzeżach planszy
        self.minX = 0
        self.maxX = BOARD_SIZE - 1
        self.minY = 0
        self.maxY = BOARD_SIZE - 1

    def getPos(self):
        return (self.__xPos, self.__yPos)
    
    def getTokenColor(self):
        return self.__tokenColor
    
    def getMoneyAvailable(self):
        return self.__moneyAvailable

    def move(self, direction, board):
        if direction == "up":
            if self.__yPos > self.minY and (self.__xPos == self.maxX or self.__xPos == self.minX ):
                self.__yPos -= 1
        elif direction == "down":
            if self.__yPos < self.maxY and (self.__xPos == self.maxX or self.__xPos == self.minX ):
                self.__yPos += 1
        elif direction == "left":
            if self.__xPos > self.minX and (self.__yPos == self.maxY or self.__yPos == self.minY ):
                self.__xPos -= 1
        elif direction == "right":
            if self.__xPos < self.maxX and (self.__yPos == self.maxY or self.__yPos == self.minY ):
                self.__xPos += 1
    
    def draw(self, WIN):
        player_width, player_height = self.image.get_size()
        player_pos = (
            int(self.__xPos * TILE_SIZE + (TILE_SIZE - player_width) / 2),
            int(self.__yPos * TILE_SIZE + (TILE_SIZE - player_height) / 2),
        )
        WIN.blit(self.image, player_pos)