from random import shuffle, randint
from Player import Player
from Tile import Tile, Property, Special, WINDOW_SIZE, TILE_SIZE
import pygame                                                   # pip install pygame / pip install pygame --pre
import os
import math

PLAYER_IMAGES = {
    "Red": pygame.image.load(os.path.join("assets", "Type=red.png")),
    "Green": pygame.image.load(os.path.join("assets", "Type=green.png")),
    "Blue": pygame.image.load(os.path.join("assets", "Type=blue.png")),
    "Yellow": pygame.image.load(os.path.join("assets", "Type=yellow.png"))
}

DICE_SIZE = 60
DICE_POS = WINDOW_SIZE / 2 - DICE_SIZE / 2

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 45

EVENT_WINDOW_WIDTH = 350
EVENT_WINDOW_HEIGHT = 130
EVENT_WINDOW_X = WINDOW_SIZE / 2 - EVENT_WINDOW_WIDTH / 2
EVENT_WINDOW_Y = TILE_SIZE + 80

COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),

    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 214, 0)
}

BUTTONS = {
    "RollDice": (WINDOW_SIZE / 2 - BUTTON_WIDTH / 2, WINDOW_SIZE / 2 - DICE_SIZE / 2 + DICE_SIZE + 10, BUTTON_WIDTH, BUTTON_HEIGHT),
    "NextTurn": (WINDOW_SIZE / 2 - BUTTON_WIDTH / 2, WINDOW_SIZE / 2 - DICE_SIZE / 2 + DICE_SIZE + BUTTON_HEIGHT + 10, BUTTON_WIDTH, BUTTON_HEIGHT),
    "Event": {
        "Window": (EVENT_WINDOW_X, EVENT_WINDOW_Y, EVENT_WINDOW_WIDTH, EVENT_WINDOW_HEIGHT),
        "Yes": (EVENT_WINDOW_X + 15, EVENT_WINDOW_Y + EVENT_WINDOW_HEIGHT - BUTTON_HEIGHT - 15, BUTTON_WIDTH, BUTTON_HEIGHT),
        "No": (EVENT_WINDOW_X + EVENT_WINDOW_WIDTH - BUTTON_WIDTH - 15, EVENT_WINDOW_Y + EVENT_WINDOW_HEIGHT - BUTTON_HEIGHT - 15, BUTTON_WIDTH, BUTTON_HEIGHT)
    }
}

def createPlayersArray(amountOfPlayers):
    if amountOfPlayers < 2 or amountOfPlayers > 4:
        return
    
    colors = ["Red", "Green", "Blue", "Yellow"]
    shuffle(colors)
    players = {}
    for color in colors:
        players[color] = Player(7, 7, color)
        players[color].setCurrentTile(0)
    
    return players, colors


def createBoard(WIN):
    boardArr = []
    
    # bottom wall
    boardArr.append(Special(WIN, 7, 7, "Start" ,"Type=Start.png", 0, 0))
    boardArr.append(Property(WIN, 6, 7, "Lodz", "bottom", "State=Empty, Type=Lodz.png", "State=Bought, Type=Lodz.png", 1, 40))
    boardArr.append(Property(WIN, 5, 7, "Cracow", "bottom", "State=Empty, Type=Cracow.png", "State=Bought, Type=Cracow.png", 2, 50))
    boardArr.append(Property(WIN, 4, 7, "Warsaw", "bottom", "State=Empty, Type=Warsaw.png", "State=Bought, Type=Warsaw.png", 3, 70))
    boardArr.append(Property(WIN, 3, 7, "Berlin", "bottom", "State=Empty, Type=Berlin.png", "State=Bought, Type=Berlin.png", 4, 120))
    boardArr.append(Property(WIN, 2, 7, "Munich", "bottom", "State=Empty, Type=Munich.png", "State=Bought, Type=Munich.png", 5, 150))
    boardArr.append(Property(WIN, 1, 7, "Dortmund", "bottom", "State=Empty, Type=Dortmund.png", "State=Bought, Type=Dortmund.png", 6, 150))
    
    # left wall
    boardArr.append(Special(WIN, 0, 7, "Jail" ,"Type=Jail.png", 7, 0))
    boardArr.append(Property(WIN, 0, 6, "Lyon", "left", "State=Empty, Type=Lyon.png", "State=Bought, Type=Lyon.png", 8, 170))
    boardArr.append(Property(WIN, 0, 5, "Marseille", "left", "State=Empty, Type=Marseille.png", "State=Bought, Type=Marseille.png", 9, 220))
    boardArr.append(Property(WIN, 0, 4, "Paris", "left", "State=Empty, Type=Paris.png", "State=Bought, Type=Paris.png", 10, 200))
    boardArr.append(Property(WIN, 0, 3, "Liverpool", "left", "State=Empty, Type=Liverpool.png", "State=Bought, Type=Liverpool.png", 11, 250))
    boardArr.append(Property(WIN, 0, 2, "Manchester", "left", "State=Empty, Type=Manchester.png", "State=Bought, Type=Manchester.png", 12, 250))
    boardArr.append(Property(WIN, 0, 1, "London", "left", "State=Empty, Type=London.png", "State=Bought, Type=London.png", 13, 300))
    
    # top wall
    boardArr.append(Special(WIN, 0, 0, "Parking" ,"Type=Parking.png", 14, 0))
    boardArr.append(Property(WIN, 1, 0, "Mediolan", "top", "State=Empty, Type=Mediolan.png", "State=Bought, Type=Mediolan.png", 15, 320))
    boardArr.append(Property(WIN, 2, 0, "Venice", "top", "State=Empty, Type=Venice.png", "State=Bought, Type=Venice.png", 16, 350))
    boardArr.append(Property(WIN, 3, 0, "Rome", "top", "State=Empty, Type=Rome.png", "State=Bought, Type=Rome.png", 17, 350))
    boardArr.append(Property(WIN, 4, 0, "Lisbon", "top", "State=Empty, Type=Lisbon.png", "State=Bought, Type=Lisbon.png", 18, 390))
    boardArr.append(Property(WIN, 5, 0, "Porto", "top", "State=Empty, Type=Porto.png", "State=Bought, Type=Porto.png", 19, 400))
    boardArr.append(Property(WIN, 6, 0, "Braga", "top", "State=Empty, Type=Braga.png", "State=Bought, Type=Braga.png", 20, 430))

    # right wall
    boardArr.append(Special(WIN, 7, 0, "GoToJail" ,"Type=Gotojail.png", 21, 0))
    boardArr.append(Property(WIN, 7, 1, "Helsinki", "right", "State=Empty, Type=Helsinki.png", "State=Bought, Type=Helsinki.png", 22, 480))
    boardArr.append(Property(WIN, 7, 2, "Stockholm", "right", "State=Empty, Type=Stockholm.png", "State=Bought, Type=Stockholm.png", 23, 520))
    boardArr.append(Property(WIN, 7, 3, "Oslo", "right", "State=Empty, Type=Oslo.png", "State=Bought, Type=Oslo.png", 24, 550))
    boardArr.append(Property(WIN, 7, 4, "Sevilla", "right", "State=Empty, Type=Sevilla.png", "State=Bought, Type=Sevilla.png", 25, 580))
    boardArr.append(Property(WIN, 7, 5, "Madrid", "right", "State=Empty, Type=Madrid.png", "State=Bought, Type=Madrid.png", 26, 630))
    boardArr.append(Property(WIN, 7, 6, "Barcelona", "right", "State=Empty, Type=Barcelona.png", "State=Bought, Type=Barcelona.png", 27, 670))
    
    return boardArr


def tossDice():
    moves = randint(1, 6)
    
    return moves

def movePlayerToTile(player, tileId):
    player.setCurrentTile(tileId)
    
def handleMouseClick(mousePos):
    mouseX, mouseY = mousePos
    if BUTTONS["RollDice"][0] <= mouseX <= BUTTONS["RollDice"][0] + BUTTONS["RollDice"][2] and BUTTONS["RollDice"][1] <= mouseY <= BUTTONS["RollDice"][1] + BUTTONS["RollDice"][3]:
        return 1
    elif BUTTONS["NextTurn"][0] <= mouseX <= BUTTONS["NextTurn"][0] + BUTTONS["NextTurn"][2] and BUTTONS["NextTurn"][1] <= mouseY <= BUTTONS["NextTurn"][1] + BUTTONS["NextTurn"][3]:
        return 2
    elif BUTTONS["Event"]["Yes"][0] <= mouseX <= BUTTONS["Event"]["Yes"][0] + BUTTONS["Event"]["Yes"][2] and BUTTONS["Event"]["Yes"][1] <= mouseY <= BUTTONS["Event"]["Yes"][1] + BUTTONS["Event"]["Yes"][3]:
        return 3
    elif BUTTONS["Event"]["No"][0] <= mouseX <= BUTTONS["Event"]["No"][0] + BUTTONS["Event"]["No"][2] and BUTTONS["Event"]["No"][1] <= mouseY <= BUTTONS["Event"]["No"][1] + BUTTONS["Event"]["No"][3]:
        return 4
    return 0
  
def askToBuyProperty(player, tile, WIN):
    if isinstance(tile, Property):
        if tile.isBought == False:
            # Render the text
            font = pygame.font.SysFont(None, 30)
            text = font.render(f"Czy chcesz kupić posiadłość {tile.name}? t-tak, n-nie", True, COLORS["WHITE"])
            # Get the rectangle for the text surface
            text_rect = text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2 - TILE_SIZE))

            answer = None
            while answer is None:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_t:
                            answer = "tak"
                        elif event.key == pygame.K_n:
                            answer = "nie"

                # Draw the text on the screen
                WIN.blit(text, text_rect)
                pygame.display.flip()

            if answer.lower() == "tak":
                tile.isBought = True
                tile.owner = player
                player.subMoney(tile.price)
        if player != tile.owner and tile.owner != None:
            tile.owner.addMoney(math.ceil(tile.price/100)*10) #=ROUNDUP((D5*0,1)/100+0,01;1)*100
            player.subMoney(math.ceil(tile.price/100)*10)

#def drawPlayerTextMoney(WIN, players, turn):
#    font = pygame.font.SysFont(None, 30)
#    turnFont = pygame.font.SysFont(None, 40, bold=True)

def drawPlayerTextMoney(WIN, font, titleFont, players, turn):
    turnText = f"{turn}'s turn"
    labelTurnText = titleFont.render(turnText, True, COLORS[turn])
    textWidth, textHeight = titleFont.size(turnText)
    WIN.blit(labelTurnText, ((WINDOW_SIZE / 2 - textWidth / 2), (DICE_POS - textHeight - 10)))
    
    for player in players.values():
        color = player.getTokenColor()
        money = player.getMoneyAvailable()
        
        playerText = f"Player {color}"
        playerMoney = f"Money: {money}"
        
        labelPlayerText = font.render(playerText, True, COLORS[color])
        labelPlayerMoney = font.render(playerMoney, True, COLORS["WHITE"])
        
        textWidth, textHeight = font.size(playerText)
        
        if color == "Red":
            xPos = (WINDOW_SIZE / 2) - (textWidth / 2)
            yPos = WINDOW_SIZE - TILE_SIZE - 60
        elif color == "Green":
            xPos = TILE_SIZE + 20
            yPos = (WINDOW_SIZE / 2) - textHeight
        elif color == "Blue":
            xPos = (WINDOW_SIZE / 2) - (textWidth / 2)
            yPos = TILE_SIZE + 20
        else:
            xPos = WINDOW_SIZE - TILE_SIZE - 20 - textWidth
            yPos = yPos = (WINDOW_SIZE / 2) - textHeight
        
        WIN.blit(labelPlayerText, (xPos, yPos))
        WIN.blit(labelPlayerMoney, (xPos, yPos + textHeight + 10))

def drawPlayers(WIN, players, board):
    occupied_positions = {}  # Słownik do przechowywania pozycji, na których znajdują się pionki

    for player in players.values():
        tileId = player.getCurrentTile()
        tile = next((tile for tile in board if tile.id == tileId), None)
        if tile:
            xPos, yPos = int(tile.xPos * TILE_SIZE), int(tile.yPos * TILE_SIZE)
            color = player.getTokenColor()
            player_image = PLAYER_IMAGES[color]
            player_rect = player_image.get_rect()

            if tile.xPos == 0:
                # Jeśli pionek znajduje się na polu ściany lewej, ustaw pozycję pionka względem prawego górnego narożnika pola
                player_rect.topright = (xPos + TILE_SIZE, yPos)
            else:
                player_rect.topleft = (xPos, yPos)

            if (xPos, yPos) in occupied_positions:
                # Jeśli na danej pozycji jest już pionek, przesuń nowy pionek na odpowiednią odległość
                offset = occupied_positions[(xPos, yPos)] * TILE_SIZE / 4
                if tile.xPos != 0 and tile.xPos != 7:
                    player_rect.move_ip(offset, 0)
                else:
                    player_rect.move_ip(0, offset)
                occupied_positions[(xPos, yPos)] += 1
            else:
                occupied_positions[(xPos, yPos)] = 1

            WIN.blit(player_image, player_rect)




def drawEvent(WIN, font, responseFont, eventText, eventYes, eventNo):
    pygame.draw.rect(WIN, COLORS["GRAY"], BUTTONS["Event"]["Window"])
    pygame.draw.rect(WIN, COLORS["DARK_GRAY"], BUTTONS["Event"]["Yes"])
    pygame.draw.rect(WIN, COLORS["DARK_GRAY"], BUTTONS["Event"]["No"])
    
    labelEventText = font.render(eventText, True, COLORS["WHITE"])
    labelEventYes = responseFont.render(eventYes, True, COLORS["WHITE"])
    labelEventNo = responseFont.render(eventNo, True, COLORS["WHITE"])
    
    width = font.size(f"{eventText}")[0]
    WIN.blit(labelEventText, (WINDOW_SIZE / 2 - width / 2, EVENT_WINDOW_Y + 15))
    
    width, height = responseFont.size(f"{eventYes}")
    WIN.blit(labelEventYes, (EVENT_WINDOW_X + 15 + BUTTON_WIDTH / 2 - width / 2, EVENT_WINDOW_Y + EVENT_WINDOW_HEIGHT - 15 - BUTTON_HEIGHT / 2 - height / 2))
    
    width, height = responseFont.size(f"{eventNo}")
    WIN.blit(labelEventNo, (EVENT_WINDOW_X + EVENT_WINDOW_WIDTH - 15 - BUTTON_WIDTH / 2 - width / 2, EVENT_WINDOW_Y + EVENT_WINDOW_HEIGHT - 15 - BUTTON_HEIGHT / 2 - height / 2))


def draw(WIN, board, players, diceGraphs, RollDiceButtonGraphic, NextTurnButtonGraphic, moves, turn):
    font = pygame.font.SysFont(None, 30)
    titleFont = pygame.font.SysFont(None, 40, bold=True)
    responseFont = pygame.font.SysFont(None, 25, italic=True)
    WIN.fill(COLORS["BLACK"])
    
    for tile in board:
        tile.draw()

    drawPlayers(WIN, players, board)  # Dodanie pionków graczy
    
    WIN.blit(diceGraphs[moves], (DICE_POS, DICE_POS))
    WIN.blit(RollDiceButtonGraphic, (BUTTONS["RollDice"][0], BUTTONS["RollDice"][1]))
    WIN.blit(NextTurnButtonGraphic, (BUTTONS["NextTurn"][0], BUTTONS["NextTurn"][1]))
    
    drawPlayerTextMoney(WIN, font, titleFont, players, turn)
    
    for event in EVENTS.values():
        if event["State"]:
            drawEvent(WIN, font, responseFont, *event["Text"])
            break


def nextTurn(turns):
    currentTurn = turns.pop(0)
    turns.append(currentTurn)
    return currentTurn


def main(): 
    pygame.init()
    WIN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Monopoly")
    
    diceGraphics = {}
    for i in range(1, 7):
        diceGraphics[i] = pygame.Surface.convert_alpha(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/State=Dice_{i}.png")), (DICE_SIZE, DICE_SIZE)))
    RollDiceButtonGraphic = pygame.Surface.convert_alpha(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/State=Dice_button.png")), (BUTTON_WIDTH, BUTTON_HEIGHT)))
    NextTurnButtonGraphic = pygame.Surface.convert_alpha(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/Next_turn_button.png")), (BUTTON_WIDTH, BUTTON_HEIGHT)))
    
    board = createBoard(WIN)
    players, turns = createPlayersArray(4)
    currentTurn = nextTurn(turns)
    
    moves = 1
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break
        draw(WIN, board, players, diceGraphs, RollDiceButtonGraphic, NextTurnButtonGraphic, moves, currentTurn)
        if event.type == pygame.MOUSEBUTTONDOWN:
            action = handleMouseClick(pygame.mouse.get_pos())
            if action == 1 and not players[currentTurn].hasRolled: # roll the dice button clicked
                players[currentTurn].hasRolled = True
                moves = tossDice()
                currentPlayer = players[currentTurn]
                currentTile = currentPlayer.getCurrentTile()
                newTile = (currentTile + moves) % len(board)
                if currentTile + moves > 27:
                    currentPlayer.addMoney(200)
                movePlayerToTile(currentPlayer, newTile)
                askToBuyProperty(currentPlayer, board[newTile], WIN)  # dodane wywołanie funkcji askToBuyProperty
                # Sprawdzanie, czy gracz jest na polu o ID równym 21
                if newTile == 21:
                    movePlayerToTile(currentPlayer, 7)
            elif action == 2: # next turn button clicked
                players[currentTurn].hasRolled = False
                currentTurn = turns.pop(0)
                turns.append(currentTurn)
        pygame.display.update()

if __name__ == "__main__":
    main()