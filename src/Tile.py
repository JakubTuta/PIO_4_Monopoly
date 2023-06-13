import pygame
import os
import math
ASSETS_DIR = "assets"
BOARD_SIZE = 8
WINDOW_SIZE = 800
TILE_SIZE = WINDOW_SIZE / BOARD_SIZE

class Tile:
    def __init__(self, WIN, xPos, yPos, name, id, price, fees):
        self.xPos = xPos
        self.yPos = yPos
        self.name = name
        self.WIN = WIN
        self.id = id
        self.price = price
        self.fees = fees


class Property(Tile):
    def __init__(self, WIN, xPos, yPos, name, wall, notBoughtGraphic, boughtGraphic, id, price, fees):
        super().__init__(WIN, xPos, yPos, name, id, price, fees)
        self.__tileWidth = 0
        self.__tileHeight = 0
        self.__notBoughtGraphic = None
        self.__boughtGraphic = None
        self.isBought = False
        self.owner = None
        self.id = id
        self.price = price
        self.fees = math.ceil(price/100)*10

        if wall == "bottom" or wall == "top":
            self.__tileWidth = TILE_SIZE
            self.__tileHeight = TILE_SIZE
            self.__notBoughtGraphic = pygame.Surface.convert(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/{notBoughtGraphic}")), (self.__tileWidth, self.__tileHeight)))
            self.__boughtGraphic = pygame.Surface.convert(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/{boughtGraphic}")), (self.__tileWidth, self.__tileHeight)))
        elif wall == "left":
            self.__tileWidth = TILE_SIZE
            self.__tileHeight = TILE_SIZE
            self.__notBoughtGraphic = pygame.Surface.convert(pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/{notBoughtGraphic}")), (self.__tileHeight, self.__tileWidth)), 270))
            self.__boughtGraphic = pygame.Surface.convert(pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/{boughtGraphic}")), (self.__tileHeight, self.__tileWidth)), 270))
        elif wall == "right":
            self.__tileWidth = TILE_SIZE
            self.__tileHeight = TILE_SIZE
            self.__notBoughtGraphic = pygame.Surface.convert(pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/{notBoughtGraphic}")), (self.__tileHeight, self.__tileWidth)), 90))
            self.__boughtGraphic = pygame.Surface.convert(pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/{boughtGraphic}")), (self.__tileHeight, self.__tileWidth)), 90))

    def draw(self):
        if not self.isBought:
            self.WIN.blit(self.__notBoughtGraphic, (self.xPos * self.__tileWidth, self.yPos * self.__tileHeight))
        else:
            self.WIN.blit(self.__boughtGraphic, (self.xPos * self.__tileWidth, self.yPos * self.__tileHeight))


class Special(Tile):
    def __init__(self, WIN, xPos, yPos, name, graphic, id, price, fees):
        super().__init__(WIN, xPos, yPos, name, id, price, fees)
        self.__tileWidth = TILE_SIZE
        self.__tileHeight = TILE_SIZE
        self.__graphic = pygame.Surface.convert(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/{graphic}")), (self.__tileWidth, self.__tileHeight)))
        self.id = id
        self.price = price

    def draw(self):
        self.WIN.blit(self.__graphic, (self.xPos * self.__tileWidth, self.yPos * self.__tileHeight))