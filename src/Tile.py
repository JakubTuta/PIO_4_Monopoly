import pygame
import os
ASSETS_DIR = "assets"
BOARD_SIZE = 8
WINDOW_SIZE = 800
TILE_SIZE = WINDOW_SIZE / BOARD_SIZE

class Tile:
    id = 0

    def __init__(self, xPos, yPos, name,image_path):
        self.xPos = xPos
        self.yPos = yPos
        self.name = name
        
        self.id = Tile.id
        Tile.id += 1
        self.image = pygame.image.load(os.path.join(ASSETS_DIR,image_path))
    
    def draw(self, surface):
        tile_rect = pygame.Rect(self.xPos * TILE_SIZE, self.yPos * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        surface.blit(self.image, tile_rect)



class Property(Tile):
    def __init__(self, WIN, xPos, yPos, name, wall, notBoughtGraphic, boughtGraphic):
        super().__init__(WIN, xPos, yPos, name)
        self.__tileWidth = 0
        self.__tileHeight = 0
        self.__notBoughtGraphic = None
        self.__boughtGraphic = None
        self.isBought = True

        if wall == "bottom" or wall == "top":
            self.__tileWidth = TILE_SIZE
            self.__tileHeight = 2 * TILE_SIZE
            self.__notBoughtGraphic = pygame.Surface.convert(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/{notBoughtGraphic}")), (self.__tileWidth, self.__tileHeight)))
            self.__boughtGraphic = pygame.Surface.convert(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/{boughtGraphic}")), (self.__tileWidth, self.__tileHeight)))
        elif wall == "left":
            self.__tileWidth = 2 * TILE_SIZE
            self.__tileHeight = TILE_SIZE
            self.__notBoughtGraphic = pygame.Surface.convert(pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/{notBoughtGraphic}")), (self.__tileHeight, self.__tileWidth)), 90))
            self.__boughtGraphic = pygame.Surface.convert(pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/{boughtGraphic}")), (self.__tileHeight, self.__tileWidth)), 90))
        elif wall == "right":
            self.__tileWidth = 2 * TILE_SIZE
            self.__tileHeight = TILE_SIZE
            self.__notBoughtGraphic = pygame.Surface.convert(pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/{notBoughtGraphic}")), (self.__tileHeight, self.__tileWidth)), 270))
            self.__boughtGraphic = pygame.Surface.convert(pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/{boughtGraphic}")), (self.__tileHeight, self.__tileWidth)), 270))

    def draw(self):
        if not self.isBought:
            self.WIN.blit(self.__notBoughtGraphic, (self.xPos * self.__tileWidth, self.yPos * self.__tileHeight))
        else:
            self.WIN.blit(self.__boughtGraphic, (self.xPos * self.__tileWidth, self.yPos * self.__tileHeight))


class Special(Tile):
    def __init__(self, WIN, xPos, yPos, name, graphic):
        super().__init__(WIN, xPos, yPos, name)
        self.__tileWidth = 2 * TILE_SIZE
        self.__tileHeight = 2 * TILE_SIZE
        self.__graphic = pygame.Surface.convert(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/{graphic}")), (self.__tileWidth, self.__tileHeight)))

    def draw(self):
        self.WIN.blit(self.__graphic, (self.xPos * self.__tileWidth, self.yPos * self.__tileHeight))