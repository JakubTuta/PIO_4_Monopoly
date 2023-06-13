from random import shuffle, randint
from Player import Player
from Tile import Tile, Property, Special, WINDOW_SIZE, TILE_SIZE
import pygame                                                   # pip install pygame / pip install pygame --pre
import os

PLAYER_IMAGES = {
    "red": pygame.image.load(os.path.join("assets", "Type=red.png")),
    "green": pygame.image.load(os.path.join("assets", "Type=green.png")),
    "blue": pygame.image.load(os.path.join("assets", "Type=blue.png")),
    "yellow": pygame.image.load(os.path.join("assets", "Type=yellow.png"))
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
    "GRAY": (60, 60, 60),
    "DARK_GRAY": (45, 45, 45),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 214, 0)
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

EVENTS = {
    "PLAYER_ON_TILE": {
        "State": False,
        "Text": ("Would you like to buy this tile?", "Yes", "No")
    },
    "PLAYER_BROKE": {
        "State": False,
        "Text": ("You don't have enough money.", "Sell", "Bankrupt"),
        "Position": (EVENT_WINDOW_X + 15, EVENT_WINDOW_Y + EVENT_WINDOW_HEIGHT - BUTTON_WIDTH - 15, BUTTON_WIDTH, BUTTON_HEIGHT)
    },
    "PLAYER_WON": {
        "State": False,
        "Text": ("Congratulations, you have won!", "Exit", "Exit"),
        "Position": (EVENT_WINDOW_X + 15, EVENT_WINDOW_Y + EVENT_WINDOW_HEIGHT - BUTTON_WIDTH - 15, BUTTON_WIDTH, BUTTON_HEIGHT)
    }
}


def createPlayersArray(amountOfPlayers):
    if amountOfPlayers < 2 or amountOfPlayers > 4:
        return
    
    colors = ["red", "green", "blue", "yellow"]
    shuffle(colors)
    players = {}
    for color in colors:
        players[color] = Player(7, 7, color)
        players[color].setCurrentTile(0)
    
    return players, colors


def createBoard(WIN):
    boardArr = []
    
    # bottom wall
    boardArr.append(Special(WIN, 7, 7, "Start" ,"Type=Start.png", 0, 0, 0))
    boardArr.append(Property(WIN, 6, 7, "Lodz", "bottom", "State=Empty, Type=Lodz.png", "State=Bought, Type=Lodz.png", 1, 40, 10))
    boardArr.append(Property(WIN, 5, 7, "Cracow", "bottom", "State=Empty, Type=Cracow.png", "State=Bought, Type=Cracow.png", 2, 50, 10))
    boardArr.append(Property(WIN, 4, 7, "Warsaw", "bottom", "State=Empty, Type=Warsaw.png", "State=Bought, Type=Warsaw.png", 3, 70, 10))
    boardArr.append(Property(WIN, 3, 7, "Berlin", "bottom", "State=Empty, Type=Berlin.png", "State=Bought, Type=Berlin.png", 4, 120, 20))
    boardArr.append(Property(WIN, 2, 7, "Munich", "bottom", "State=Empty, Type=Munich.png", "State=Bought, Type=Munich.png", 5, 150, 20))
    boardArr.append(Property(WIN, 1, 7, "Dortmund", "bottom", "State=Empty, Type=Dortmund.png", "State=Bought, Type=Dortmund.png", 6, 150, 20))
    
    # left wall
    boardArr.append(Special(WIN, 0, 7, "Jail" ,"Type=Jail.png", 7, 0, 0))
    boardArr.append(Property(WIN, 0, 6, "Lyon", "left", "State=Empty, Type=Lyon.png", "State=Bought, Type=Lyon.png", 8, 170, 20))
    boardArr.append(Property(WIN, 0, 5, "Marseille", "left", "State=Empty, Type=Marseille.png", "State=Bought, Type=Marseille.png", 9, 220, 30))
    boardArr.append(Property(WIN, 0, 4, "Paris", "left", "State=Empty, Type=Paris.png", "State=Bought, Type=Paris.png", 10, 200, 30))
    boardArr.append(Property(WIN, 0, 3, "Liverpool", "left", "State=Empty, Type=Liverpool.png", "State=Bought, Type=Liverpool.png", 11, 250, 30))
    boardArr.append(Property(WIN, 0, 2, "Manchester", "left", "State=Empty, Type=Manchester.png", "State=Bought, Type=Manchester.png", 12, 250, 30))
    boardArr.append(Property(WIN, 0, 1, "London", "left", "State=Empty, Type=London.png", "State=Bought, Type=London.png", 13, 300, 40))
    
    # top wall
    boardArr.append(Special(WIN, 0, 0, "Parking" ,"Type=Parking.png", 14, 0, 0))
    boardArr.append(Property(WIN, 1, 0, "Mediolan", "top", "State=Empty, Type=Mediolan.png", "State=Bought, Type=Mediolan.png", 15, 320, 40))
    boardArr.append(Property(WIN, 2, 0, "Venice", "top", "State=Empty, Type=Venice.png", "State=Bought, Type=Venice.png", 16, 350, 40))
    boardArr.append(Property(WIN, 3, 0, "Rome", "top", "State=Empty, Type=Rome.png", "State=Bought, Type=Rome.png", 17, 350, 40))
    boardArr.append(Property(WIN, 4, 0, "Lisbon", "top", "State=Empty, Type=Lisbon.png", "State=Bought, Type=Lisbon.png", 18, 390, 40))
    boardArr.append(Property(WIN, 5, 0, "Porto", "top", "State=Empty, Type=Porto.png", "State=Bought, Type=Porto.png", 19, 400, 50))
    boardArr.append(Property(WIN, 6, 0, "Braga", "top", "State=Empty, Type=Braga.png", "State=Bought, Type=Braga.png", 20, 430, 50))

    # right wall
    boardArr.append(Special(WIN, 7, 0, "GoToJail" ,"Type=Gotojail.png", 21, 0, 0))
    boardArr.append(Property(WIN, 7, 1, "Helsinki", "right", "State=Empty, Type=Helsinki.png", "State=Bought, Type=Helsinki.png", 22, 480, 50))
    boardArr.append(Property(WIN, 7, 2, "Stockholm", "right", "State=Empty, Type=Stockholm.png", "State=Bought, Type=Stockholm.png", 23, 520, 60))
    boardArr.append(Property(WIN, 7, 3, "Oslo", "right", "State=Empty, Type=Oslo.png", "State=Bought, Type=Oslo.png", 24, 550, 60))
    boardArr.append(Property(WIN, 7, 4, "Sevilla", "right", "State=Empty, Type=Sevilla.png", "State=Bought, Type=Sevilla.png", 25, 580, 60))
    boardArr.append(Property(WIN, 7, 5, "Madrid", "right", "State=Empty, Type=Madrid.png", "State=Bought, Type=Madrid.png", 26, 630, 70))
    boardArr.append(Property(WIN, 7, 6, "Barcelona", "right", "State=Empty, Type=Barcelona.png", "State=Bought, Type=Barcelona.png", 27, 670, 70))
    
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


def drawPlayerTextMoney(WIN, font, titleFont, players, turn):
    if turn in players:
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
        
        if color == "red":
            xPos = (WINDOW_SIZE / 2) - (textWidth / 2)
            yPos = WINDOW_SIZE - TILE_SIZE - 60
        elif color == "green":
            xPos = TILE_SIZE + 20
            yPos = (WINDOW_SIZE / 2) - textHeight
        elif color == "blue":
            xPos = (WINDOW_SIZE / 2) - (textWidth / 2)
            yPos = TILE_SIZE + 20
        else:
            xPos = WINDOW_SIZE - TILE_SIZE - 20 - textWidth
            yPos = yPos = (WINDOW_SIZE / 2) - textHeight
        
        WIN.blit(labelPlayerText, (xPos, yPos))
        WIN.blit(labelPlayerMoney, (xPos, yPos + textHeight + 10))

def drawPlayers(WIN, players, board):
    occupied_positions = {}
    players_to_remove = []
    for player in players.values():
        if player.getMoneyAvailable() == 0:
            players_to_remove.append(player)
            continue
        
        tileId = player.getCurrentTile()
        tile = next((tile for tile in board if tile.id == tileId), None)
        if tile:
            xPos, yPos = int(tile.xPos * TILE_SIZE), int(tile.yPos * TILE_SIZE)
            color = player.getTokenColor()
            player_image = PLAYER_IMAGES[color]
            player_rect = player_image.get_rect()

            if tile.xPos == 0:
                player_rect.topright = (xPos + TILE_SIZE, yPos)
            else:
                player_rect.topleft = (xPos, yPos)

            if (xPos, yPos) in occupied_positions:
                offset = occupied_positions[(xPos, yPos)] * TILE_SIZE / 4
                if tile.xPos != 0 and tile.xPos != 7:
                    player_rect.move_ip(offset, 0)
                else:
                    player_rect.move_ip(0, offset)
                occupied_positions[(xPos, yPos)] += 1
            else:
                occupied_positions[(xPos, yPos)] = 1

            WIN.blit(player_image, player_rect)

    for player in players_to_remove:
        del players[player.getTokenColor()]


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
    
    diceGraphs = {}
    for i in range(1, 7):
        diceGraphs[i] = pygame.Surface.convert_alpha(pygame.transform.scale(pygame.image.load(os.path.join(f"assets/State=Dice_{i}.png")), (DICE_SIZE, DICE_SIZE)))
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
                for event in EVENTS.values():
                    if event==EVENTS["PLAYER_ON_TILE"] and event["State"]:
                        if action == 3:                                         # "YES" button hit
                            currentPlayer = players[currentTurn]
                            currentTile = currentPlayer.getCurrentTile()
                            board[currentTile].isBought = True
                            board[currentTile].owner = currentPlayer
                            currentPlayer.subMoney(board[currentTile].price)
                            amount = board[currentTile].price
                            currentPlayer.addToSumOfBought(amount)
                            event["State"]=False
                        elif action == 4:                                       # "NO" button hit
                            event["State"]=False

                    if event==EVENTS["PLAYER_BROKE"] and event["State"]:
                        if action == 3:                                         # "YES" button hit
                            currentPlayer = players[currentTurn]
                            currentTile = currentPlayer.getCurrentTile()
                            SumOfBought = currentPlayer.getSumOfBought()
                            currentPlayer.addMoney(SumOfBought/2)
                            if currentPlayer.getMoneyAvailable() < board[currentTile].fees:
                                board[currentTile].owner.addMoney(currentPlayer.getMoneyAvailable())
                                currentPlayer.setMoneyAvailable(0)
                                del players[currentPlayer.getTokenColor()]
                            for x in board:
                                if isinstance(x,Property):
                                    if x.owner == currentPlayer:
                                        x.owner = None
                                        x.isBought = False
                            event["State"]=False
                            if len(players) == 1:
                                EVENTS["PLAYER_WON"]["State"] = True
                        elif action == 4:                                       # "NO" button hit
                            currentPlayer = players[currentTurn]
                            currentTile = currentPlayer.getCurrentTile()
                            board[currentTile].owner.addMoney(currentPlayer.getMoneyAvailable())
                            currentPlayer.setMoneyAvailable(0)
                            del players[currentPlayer.getTokenColor()]
                            for x in board:
                                if isinstance(x,Property):
                                    if x.owner == currentPlayer:
                                        x.owner = None
                                        x.isBought = False
                            event["State"]=False
                            if len(players) == 1:
                                EVENTS["PLAYER_WON"]["State"] = True
                    if event==EVENTS["PLAYER_ON_TILE"] and event["State"]:
                        if action == 3:                                         # "YES" button hit
                            event["State"]=False
                        elif action == 4:                                       # "NO" button hit
                            event["State"]=False
                            
                    if action == 1 and not players[currentTurn].hasRolled:      # roll the dice button clicked
                        players[currentTurn].hasRolled = True
                        moves = tossDice()
                        currentPlayer = players[currentTurn]
                        currentTile = currentPlayer.getCurrentTile()
                        newTile = (currentTile + moves) % len(board)

                        if currentTile + moves > 27:
                            currentPlayer.addMoney(200)
        
                        movePlayerToTile(currentPlayer, newTile)

                        if board[newTile].id != 7 and board[newTile].id != 14 and board[newTile].id != 21 and board[newTile].id != 0:

                            if board[newTile].owner == None and board[newTile].isBought == False and currentPlayer.getMoneyAvailable()>board[newTile].price:
                                EVENTS["PLAYER_ON_TILE"]["State"] = True
                            if board[newTile].owner != currentPlayer and board[newTile].isBought == True and currentPlayer.getMoneyAvailable() >= board[newTile].fees:
                                currentPlayer.subMoney(board[newTile].fees)
                                board[newTile].owner.addMoney(board[newTile].fees)
                            if board[newTile].owner != currentPlayer and board[newTile].isBought == True and currentPlayer.getMoneyAvailable() < board[newTile].fees:
                                    EVENTS["PLAYER_BROKE"]["State"] = True
                        if newTile == 21: # Przeniesienie gracza na pole jail gdy wejdzie na pole gotojail
                            movePlayerToTile(currentPlayer, 7)
                    elif action == 2: # next turn button clicked
                        if currentTurn in players:
                            players[currentTurn].hasRolled = False
                        currentTurn = turns.pop(0)
                        turns.append(currentTurn)

            
            pygame.display.update()

if __name__ == "__main__":
    main()