from random import shuffle, randint
from Player import Player
from Tile import Tile, Property, Special, WINDOW_SIZE, TILE_SIZE
import pygame                                                   # pip install pygame / pip install pygame --pre
import os


DICE_SIZE = 60
DICE_POS = WINDOW_SIZE / 2 - DICE_SIZE / 2

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 45

ROLL_DICE_BUTTON_POSX = WINDOW_SIZE / 2 - BUTTON_WIDTH / 2
ROLL_DICE_BUTTON_POSY = WINDOW_SIZE / 2 - DICE_SIZE / 2 + DICE_SIZE + 10

NEXT_TURN_BUTTON_POSX = WINDOW_SIZE / 2 - BUTTON_WIDTH / 2
NEXT_TURN_BUTTON_POSY = TILE_SIZE + 20


def createPlayersArray(amountOfPlayers):
    if amountOfPlayers < 2 or amountOfPlayers > 4:
        return
    
    colors = ["red", "green", "blue", "purple"]
    shuffle(colors)
    players = {}
    for color in colors:
        players[color] = Player(0, 0, color)
    
    return players, colors


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
    
    if ROLL_DICE_BUTTON_POSX <= mouseX <= ROLL_DICE_BUTTON_POSX + BUTTON_WIDTH and ROLL_DICE_BUTTON_POSY <= mouseY <= ROLL_DICE_BUTTON_POSY + BUTTON_HEIGHT:
        return 1
    elif NEXT_TURN_BUTTON_POSX <= mouseX <= NEXT_TURN_BUTTON_POSX + BUTTON_WIDTH and NEXT_TURN_BUTTON_POSY <= mouseY <= NEXT_TURN_BUTTON_POSY + BUTTON_HEIGHT:
        return 2
    return 0


def draw(WIN, board, diceGraphs, RollDiceButtonGraphic, NextTurnButtonGraphic, moves):
    WIN.fill((0, 0, 0))

    for tile in board:
        tile.draw()
    
    WIN.blit(diceGraphs[moves], (DICE_POS, DICE_POS))
    WIN.blit(RollDiceButtonGraphic, (ROLL_DICE_BUTTON_POSX, ROLL_DICE_BUTTON_POSY))
    WIN.blit(NextTurnButtonGraphic, (NEXT_TURN_BUTTON_POSX, NEXT_TURN_BUTTON_POSY))


def main(): 
    pygame.init()
    WIN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Monopoly")
    
    diceGraphs = {}
    for i in range(1, 7):
        diceGraphs[i] = pygame.Surface.convert_alpha(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/State=Dice_{i}.png")), (DICE_SIZE, DICE_SIZE)))
    RollDiceButtonGraphic = pygame.Surface.convert_alpha(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/State=Dice_button.png")), (BUTTON_WIDTH, BUTTON_HEIGHT)))
    NextTurnButtonGraphic = pygame.Surface.convert_alpha(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/Next_turn_button.png")), (BUTTON_WIDTH, BUTTON_HEIGHT)))
    
    board = createBoard(WIN)
    players, turns = createPlayersArray(4)
    currentTurn = turns.pop(0)
    turns.append(currentTurn)
    
    clock = pygame.time.Clock()

    moves = 1
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break

        draw(WIN, board, diceGraphs, RollDiceButtonGraphic, NextTurnButtonGraphic, moves)
        if event.type == pygame.MOUSEBUTTONDOWN:
            action = handleMouseClick(pygame.mouse.get_pos())
            if action == 1 and not players[currentTurn].hasRolled: # roll the dice button clicked
                players[currentTurn].hasRolled = True
                moves = tossDice()
            elif action == 2: # next turn button clicked
                players[currentTurn].hasRolled = False
                currentTurn = turns.pop(0)
                turns.append(currentTurn)
        
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()