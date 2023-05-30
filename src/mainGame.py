from random import shuffle
from Player import Player
from Tile import Tile
from Tile import Property
from Tile import Special
import pygame
import os


BOARD_SIZE = 8
WINDOW_SIZE = 800
TILE_SIZE = WINDOW_SIZE / BOARD_SIZE

def createPlayersArray(amountOfPlayers):
    if amountOfPlayers < 2 or amountOfPlayers > 4:
        return
    
    colors = ["red", "green", "blue", "purple"]
    shuffle(colors)
    return [Player(0, 0, colors[i]) for i in range(amountOfPlayers)]


def createBoard():
    WIN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    boardArr = [[None for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
    
   
    # top wall
    boardArr[0][0] = Special(WIN, 0, 0, "Parking" ,"Type=Parking.png")
    boardArr[0][1] = Property(WIN, 1, 0, "Mediolan", "top", "State=Empty, Type=Mediolan.png", "State=Bought, Type=Mediolan.png")
    boardArr[0][2] = Property(WIN, 2, 0, "Venice", "top", "State=Empty, Type=Venice.png", "State=Bought, Type=Venice.png")
    boardArr[0][3] = Property(WIN, 3, 0, "Rome", "top", "State=Empty, Type=Rome.png", "State=Bought, Type=Rome.png")
    boardArr[0][4] = Property(WIN, 4, 0, "Lisbon", "top", "State=Empty, Type=Lisbon.png", "State=Bought, Type=Lisbon.png")
    boardArr[0][5] = Property(WIN, 5, 0, "Porto", "top", "State=Empty, Type=Porto.png", "State=Bought, Type=Porto.png")
    boardArr[0][6] = Property(WIN, 6, 0, "Braga", "top", "State=Empty, Type=Braga.png", "State=Bought, Type=Braga.png")
    
    # left wall
    boardArr[1][0] = Property(WIN, 0, 1, "London", "left", "State=Empty, Type=London.png", "State=Bought, Type=London.png")
    boardArr[2][0] = Property(WIN, 0, 2, "Manchester", "left", "State=Empty, Type=Manchester.png", "State=Bought, Type=Manchester.png")
    boardArr[3][0] = Property(WIN, 0, 3, "Liverpool", "left", "State=Empty, Type=Liverpool.png", "State=Bought, Type=Liverpool.png")
    boardArr[4][0] = Property(WIN, 0, 4, "Paris", "left", "State=Empty, Type=Paris.png", "State=Bought, Type=Paris.png")
    boardArr[5][0] = Property(WIN, 0, 5, "Marseille", "left", "State=Empty, Type=Marseille.png", "State=Bought, Type=Marseille.png")
    boardArr[6][0] = Property(WIN, 0, 6, "Lyon", "left", "State=Empty, Type=Lyon.png", "State=Bought, Type=Lyon.png")
    boardArr[7][0] = Special(WIN, 0, 7, "Jail" ,"Type=Jail.png")

    # right wall
    boardArr[0][7] = Special(WIN, 7, 0, "GoToJail" ,"Type=Gotojail.png")
    boardArr[1][7] = Property(WIN, 7, 1, "Helsinki", "right", "State=Empty, Type=Helsinki.png", "State=Bought, Type=Helsinki.png")
    boardArr[2][7] = Property(WIN, 7, 2, "Stockholm", "right", "State=Empty, Type=Stockholm.png", "State=Bought, Type=Stockholm.png")
    boardArr[3][7] = Property(WIN, 7, 3, "Oslo", "right", "State=Empty, Type=Oslo.png", "State=Bought, Type=Oslo.png")
    boardArr[4][7] = Property(WIN, 7, 4, "Sevilla", "right", "State=Empty, Type=Sevilla.png", "State=Bought, Type=Sevilla.png")
    boardArr[5][7] = Property(WIN, 7, 5, "Madrid", "right", "State=Empty, Type=Madrid.png", "State=Bought, Type=Madrid.png")
    boardArr[6][7] = Property(WIN, 7, 6, "Barcelona", "right", "State=Empty, Type=Barcelona.png", "State=Bought, Type=Barcelona.png")
    boardArr[7][7] = Special(WIN, 7, 7, "Start" ,"Type=Start.png")

    # bottom wall
    boardArr[7][1] = Property(WIN, 1, 7, "Dortmund", "bottom", "State=Empty, Type=Dortmund.png", "State=Bought, Type=Dortmund.png")
    boardArr[7][2] = Property(WIN, 2, 7, "Munich", "bottom", "State=Empty, Type=Munich.png", "State=Bought, Type=Munich.png")
    boardArr[7][3] = Property(WIN, 3, 7, "Berlin", "bottom", "State=Empty, Type=Berlin.png", "State=Bought, Type=Berlin.png")
    boardArr[7][4] = Property(WIN, 4, 7, "Warsaw", "bottom", "State=Empty, Type=Warsaw.png", "State=Bought, Type=Warsaw.png")
    boardArr[7][5] = Property(WIN, 5, 7, "Cracow", "bottom", "State=Empty, Type=Cracow.png", "State=Bought, Type=Cracow.png")
    boardArr[7][6] = Property(WIN, 6, 7, "Lodz", "bottom", "State=Empty, Type=Lodz.png", "State=Bought, Type=Lodz.png")

    

    
    
        
    return boardArr


def main(): 
    pygame.init()
    playersArr = createPlayersArray(4)
    
    WIN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Monopoly")
    
    clock = pygame.time.Clock()

    board = createBoard()
    gameRunning = True
    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        clock.tick(60)

        WIN.fill((0, 0, 0))

        # Rysowanie kafelków z grafikami
        for row in board:
            for tile in row:
                if tile is not None:
                    tile.draw()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()