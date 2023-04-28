from random import shuffle
from Player import Player
from Tile import Tile


BOARD_SIZE = 11
WINDOW_SIZE = 900
TILE_SIZE = WINDOW_SIZE / BOARD_SIZE


def createPlayersArray(amountOfPlayers):
    if amountOfPlayers < 2 or amountOfPlayers > 4:
        return
    
    colors = ["red", "green", "blue", "purple"]
    shuffle(colors)
    return [Player(0, 0, colors[i]) for i in range(amountOfPlayers)]


def createBoard():
    boardArr = [[0 for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
    
    # bottom wall
    for i in range(BOARD_SIZE - 1, 0, -1):
        if i == BOARD_SIZE - 1:
            boardArr[BOARD_SIZE - 1][i] = Tile(i, BOARD_SIZE - 1, "corner")
        else:
            boardArr[BOARD_SIZE - 1][i] = Tile(i, BOARD_SIZE - 1, "bottom")
    
    # left wall
    for i in range(BOARD_SIZE - 1, 0, -1):
        if i == BOARD_SIZE - 1:
            boardArr[i][0] = Tile(0, i, "corner")
        else:
            boardArr[i][0] = Tile(0, i, "left")
    
    # top wall
    for i in range(BOARD_SIZE - 1):
        if i == 0:
            boardArr[0][i] = Tile(i, 0, "corner")
        else:
            boardArr[0][i] = Tile(i, 0, "top")
    
    # right wall
    for i in range(BOARD_SIZE - 1):
        if i == 0:
            boardArr[i][BOARD_SIZE - 1] = Tile(BOARD_SIZE - 1, i, "corner")
        else:
            boardArr[i][BOARD_SIZE - 1] = Tile(BOARD_SIZE - 1, i, "right")
        
    return boardArr


def main():
    board = createBoard()
    playersArr = createPlayersArray(4)
    
    for row in board:
        for col in row:
            if col == 0:
                print(0, end="\t")
            else:
                print(col.wall, end="\t")
        print()


if __name__ == "__main__":
    main()