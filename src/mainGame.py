from random import shuffle, randint
from Player import Player
from Tile import Tile, Property, Special, WINDOW_SIZE
import pygame                                                   # pip install pygame / pip install pygame --pre
import os


DICE_SIZE = 60
DICE_POS = WINDOW_SIZE / 2 - DICE_SIZE / 2

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
BUTTON_POSX = WINDOW_SIZE / 2 - BUTTON_WIDTH / 2
BUTTON_POSY = WINDOW_SIZE / 2 - DICE_SIZE / 2 + DICE_SIZE + 10


def createPlayersArray(amountOfPlayers):
    if amountOfPlayers < 2 or amountOfPlayers > 4:
        return
    
    colors = ["red", "green", "blue", "purple"]
    shuffle(colors)
    return [Player(0, 0, colors[i]) for i in range(amountOfPlayers)]


def createBoard(WIN):
    boardArr = []
    
    # bottom wall
    boardArr.append(Special(WIN, 7, 7, "Start" ,"Type=Start.png"))
    boardArr.append(Property(WIN, 6, 7, "Lodz", "bottom", "State=Empty, Type=Lodz.png", "State=Bought, Type=Lodz.png"))
    boardArr.append(Property(WIN, 5, 7, "Cracow", "bottom", "State=Empty, Type=Cracow.png", "State=Bought, Type=Cracow.png"))
    boardArr.append(Property(WIN, 4, 7, "Warsaw", "bottom", "State=Empty, Type=Warsaw.png", "State=Bought, Type=Warsaw.png"))
    boardArr.append(Property(WIN, 3, 7, "Berlin", "bottom", "State=Empty, Type=Berlin.png", "State=Bought, Type=Berlin.png"))
    boardArr.append(Property(WIN, 2, 7, "Munich", "bottom", "State=Empty, Type=Munich.png", "State=Bought, Type=Munich.png"))
    boardArr.append(Property(WIN, 1, 7, "Dortmund", "bottom", "State=Empty, Type=Dortmund.png", "State=Bought, Type=Dortmund.png"))
    
    # left wall
    boardArr.append(Special(WIN, 0, 7, "Jail" ,"Type=Jail.png"))
    boardArr.append(Property(WIN, 0, 6, "Lyon", "left", "State=Empty, Type=Lyon.png", "State=Bought, Type=Lyon.png"))
    boardArr.append(Property(WIN, 0, 5, "Marseille", "left", "State=Empty, Type=Marseille.png", "State=Bought, Type=Marseille.png"))
    boardArr.append(Property(WIN, 0, 4, "Paris", "left", "State=Empty, Type=Paris.png", "State=Bought, Type=Paris.png"))
    boardArr.append(Property(WIN, 0, 3, "Liverpool", "left", "State=Empty, Type=Liverpool.png", "State=Bought, Type=Liverpool.png"))
    boardArr.append(Property(WIN, 0, 2, "Manchester", "left", "State=Empty, Type=Manchester.png", "State=Bought, Type=Manchester.png"))
    boardArr.append(Property(WIN, 0, 1, "London", "left", "State=Empty, Type=London.png", "State=Bought, Type=London.png"))
    
    # top wall
    boardArr.append(Special(WIN, 0, 0, "Parking" ,"Type=Parking.png"))
    boardArr.append(Property(WIN, 1, 0, "Mediolan", "top", "State=Empty, Type=Mediolan.png", "State=Bought, Type=Mediolan.png"))
    boardArr.append(Property(WIN, 2, 0, "Venice", "top", "State=Empty, Type=Venice.png", "State=Bought, Type=Venice.png"))
    boardArr.append(Property(WIN, 3, 0, "Rome", "top", "State=Empty, Type=Rome.png", "State=Bought, Type=Rome.png"))
    boardArr.append(Property(WIN, 4, 0, "Lisbon", "top", "State=Empty, Type=Lisbon.png", "State=Bought, Type=Lisbon.png"))
    boardArr.append(Property(WIN, 5, 0, "Porto", "top", "State=Empty, Type=Porto.png", "State=Bought, Type=Porto.png"))
    boardArr.append(Property(WIN, 6, 0, "Braga", "top", "State=Empty, Type=Braga.png", "State=Bought, Type=Braga.png"))

    # right wall
    boardArr.append(Special(WIN, 7, 0, "GoToJail" ,"Type=Gotojail.png"))
    boardArr.append(Property(WIN, 7, 1, "Helsinki", "right", "State=Empty, Type=Helsinki.png", "State=Bought, Type=Helsinki.png"))
    boardArr.append(Property(WIN, 7, 2, "Stockholm", "right", "State=Empty, Type=Stockholm.png", "State=Bought, Type=Stockholm.png"))
    boardArr.append(Property(WIN, 7, 3, "Oslo", "right", "State=Empty, Type=Oslo.png", "State=Bought, Type=Oslo.png"))
    boardArr.append(Property(WIN, 7, 4, "Sevilla", "right", "State=Empty, Type=Sevilla.png", "State=Bought, Type=Sevilla.png"))
    boardArr.append(Property(WIN, 7, 5, "Madrid", "right", "State=Empty, Type=Madrid.png", "State=Bought, Type=Madrid.png"))
    boardArr.append(Property(WIN, 7, 6, "Barcelona", "right", "State=Empty, Type=Barcelona.png", "State=Bought, Type=Barcelona.png"))
    
    return boardArr


def tossDice():
    moves = randint(1, 6)
    
    return moves


def handleMouseClick(mousePos):
    mouseX, mouseY = mousePos
    
    if BUTTON_POSX <= mouseX <= BUTTON_POSX + BUTTON_WIDTH and BUTTON_POSY <= mouseY <= BUTTON_POSY + BUTTON_HEIGHT:
        return 1
    return 0


def draw(WIN, board, diceGraphs, buttonGraphic, moves):
    WIN.fill((0, 0, 0))

    for tile in board:
        tile.draw()
    
    WIN.blit(diceGraphs[moves], (DICE_POS, DICE_POS))
    WIN.blit(buttonGraphic, (BUTTON_POSX, BUTTON_POSY))


def main(): 
    pygame.init()
    WIN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Monopoly")
    
    diceGraphs = {}
    for i in range(1, 7):
        diceGraphs[i] = pygame.Surface.convert_alpha(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/State=Dice_{i}.png")), (DICE_SIZE, DICE_SIZE)))
    buttonGraphic = pygame.Surface.convert_alpha(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/State=Dice_button.png")), (BUTTON_WIDTH, BUTTON_HEIGHT)))
    
    board = createBoard(WIN)
    playersArr = createPlayersArray(4)
    
    clock = pygame.time.Clock()

    moves = 1
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break

        draw(WIN, board, diceGraphs, buttonGraphic, moves)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if handleMouseClick(pygame.mouse.get_pos()) == 1:
                moves = tossDice()
        
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()