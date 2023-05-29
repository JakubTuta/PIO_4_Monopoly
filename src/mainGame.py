from random import shuffle
from Player import Player
from Tile import Tile
import pygame
import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')

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
    boardArr = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    # bottom wall
    for i in range(BOARD_SIZE - 1, 0, -1):
        if i == BOARD_SIZE - 1:
            boardArr[BOARD_SIZE - 1][i] = Tile(i, BOARD_SIZE - 1,"bot", "corner","Type=Start.png")
        else:
            boardArr[BOARD_SIZE - 1][i] = Tile(i, BOARD_SIZE - 1,"bot", "bottom","State=Empty, Type=Warsaw.png")

    # left wall
    for i in range(BOARD_SIZE - 1, 0, -1):
        if i == BOARD_SIZE - 1:
            boardArr[i][0] = Tile(0, i, "corner","left","Type=Start.png")
        else:
            boardArr[i][0] = Tile(0, i, "left","left","State=Empty, Type=Paris.png")

    # top wall
    for i in range(BOARD_SIZE - 1):
        if i == 0:
            boardArr[0][i] = Tile(i, 0, "corner","top","Type=Start.png")
        else:
            boardArr[0][i] = Tile(i, 0, "top","top","State=Empty, Type=Rome.png")

    # right wall
    for i in range(BOARD_SIZE - 1):
        if i == 0:
            boardArr[i][BOARD_SIZE - 1] = Tile(BOARD_SIZE - 1, i, "corner","right","Type=Start.png")
        else:
            boardArr[i][BOARD_SIZE - 1] = Tile(BOARD_SIZE - 1, i, "right","right","State=Empty, Type=Oslo.png")



    return boardArr



def main():
    board = createBoard()
    playersArr = createPlayersArray(4)
    
    WIN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Monopoly")
    
    clock = pygame.time.Clock()
    
    gameRunning = True
    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        WIN.fill((0, 0, 0))

        # Rysowanie kafelków z grafikami
        for row in board:
            for tile in row:
                if tile is not None:
                    tile.draw(WIN)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()