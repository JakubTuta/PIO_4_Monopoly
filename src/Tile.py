from mainGame import TILE_SIZE


class Tile:
    id = 0
    def __init__(self, xPos = 0, yPos = 0, wall = "bottom"):
        self.__xPos = xPos
        self.__yPos = yPos
        self.__tileWidth = 0
        self.__tileHeight = 0
        self.wall = wall
        
        if wall == "corner":
            self.__tileWidth = 2 * TILE_SIZE
            self.__tileHeight = 2 * TILE_SIZE
        if wall == "bottom" or wall == "top":
            self.__tileWidth = TILE_SIZE
            self.__tileHeight = 2 * TILE_SIZE
        elif wall == "left" or wall == "right":
            self.__tileWidth = 2 * TILE_SIZE
            self.__tileHeight = TILE_SIZE
        
        self.id = Tile.id
        Tile.id += 1
    
    def getPos(self):
        return (self.__x, self.__y)