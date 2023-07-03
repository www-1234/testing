print("Try-N-Go\n---------------------------------------")
gameBoard = [
  [0],
  [0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0,0,0,],
  [0,0,0,0,0,0,0,0,0,],
  [0,0,0,0,0,0,0,0,0,0,0,]
  ]

rows = 6
x = 0
y = rows*3

def printBoard(x,y):
  for i in range(rows):
    print(" " * y, end="")
    print(gameBoard[x])
    y -=3
    x+=1

turnCounter = 0
p = 0 
def inputMove(p):
  while True:
    r = int(input("Input Row: "))-1
    c = int(input("Input Column: "))-1
    try:
      if r < 0:
        raise IndexError
      elif c < 0:
        raise IndexError
      if gameBoard[r][c] == 0:
        gameBoard[r][c] = (p+1)
      else:
        raise ValueError
    except ValueError:
      print("Error: Spot Already Taken")
    except IndexError:
      print("Error: Outside of Range")
    else:
      break
  printBoard(x,y)

assignTo = 0
pointsA = 0
pointsB = 0

def claimTriangle(p):
  while True:
      x = str(input("Claim Triangle ('y' or 'n'): "))
      if x == "y" or x == "n":
        break
  if x == "y":
    if assignTo == 1:
      global pointsA
      pointsA += p
    elif assignTo == 2:
      global pointsB
      pointsB += p
    return 1

def checkForT1A():
  a = 0
  b = 0
  try:
    while a < len(gameBoard):
      b = 0
      while b < len(gameBoard[a]):
        if (gameBoard[a][b] and gameBoard[a+1][b] and gameBoard[a+1][b+1] and gameBoard[a+1][b+2]) != 0:
            print(f"Triangle [{a+1},{b+1}] [{a+2},{b+1}] [{a+2},{b+2}] [{a+2},{b+3}] Filled")
            list = [gameBoard[a][b], gameBoard[a+1][b], gameBoard[a+1][b+1], gameBoard[a+1][b+2]]
            if list.count(1) > list.count(2):
                print("Majority 1")
                global assignTo
                assignTo = 1
                if claimTriangle(2) == 1:
                  gameBoard[a][b] = gameBoard[a+1][b] = gameBoard[a+1][b+1] = gameBoard[a+1][b+2] = 0
            elif list.count(2) > list.count(1):
                print("Majority 2")
                assignTo = 2
                if claimTriangle(2) == 1:
                  gameBoard[a][b] = gameBoard[a+1][b] = gameBoard[a+1][b+1] = gameBoard[a+1][b+2] = 0
        
        b += 2
      a += 1
  except:
    pass

def checkForT1B():
    a = 3
    b = 3
    try:
      while a < (len(gameBoard)):
        b = 3
        while b < (len(gameBoard[a])-2):
          if (gameBoard[a][b] and gameBoard[a-1][b] and gameBoard[a-1][b-1] and gameBoard[a-1][b-2]) != 0:
              print(f"Triangle [{a},{b-1}] [{a},{b}] [{a},{b+1}] [{a+1},{b+1}] Filled")
              list = [gameBoard[a][b], gameBoard[a-1][b], gameBoard[a-1][b-1], gameBoard[a-1][b-2]]
              if list.count(1) > list.count(2):
                  print("Majority 1")
                  global assignTo
                  assignTo = 1
                  if claimTriangle(2) == 1:
                    gameBoard[a][b] = gameBoard[a-1][b] = gameBoard[a-1][b-1] = gameBoard[a-1][b-2] = 0
              elif list.count(2) > list.count(1):
                  print("Majority 2")
                  assignTo = 2
                  if claimTriangle(2) == 1:
                    gameBoard[a][b] = gameBoard[a-1][b] = gameBoard[a-1][b-1] = gameBoard[a-1][b-2] = 0
          b += 2
        a += 1
    except:
      pass

def checkForT2A():
  a = 0
  b = 0
  while a < (len(gameBoard)-2):
    b = 0
    while b < len(gameBoard[a]):
      if (gameBoard[a][b] and gameBoard[a+1][b] and gameBoard[a+1][b+1] and gameBoard[a+1][b+2] and gameBoard[a+2][b] and gameBoard[a+2][b+1] and gameBoard[a+2][b+2] and gameBoard[a+2][b+3] and gameBoard[a+2][b+4]) != 0:
        print(f"Triangle [{a+1},{b+1}] [{a+2},{b+1}] [{a+2},{b+2}] [{a+2},{b+3}] [{a+3},{b+1}] [{a+3},{b+2}] [{a+3},{b+3}] [{a+3},{b+4}] [{a+3},{b+5}] Filled")
        list = [gameBoard[a][b], gameBoard[a+1][b], gameBoard[a+1][b+1], gameBoard[a+1][b+2], gameBoard[a+2][b], gameBoard[a+2][b+1], gameBoard[a+2][b+2], gameBoard[a+2][b+3], gameBoard[a+2][b+4]]
        if list.count(1) > list.count(2):
          print("Majority 1")
          global assignTo
          assignTo = 1
          if claimTriangle(5) == 1:
            gameBoard[a][b] = gameBoard[a+1][b] = gameBoard[a+1][b+1] = gameBoard[a+1][b+2] = gameBoard[a+2][b] = gameBoard[a+2][b+1] = gameBoard[a+2][b+2] = gameBoard[a+2][b+3] = gameBoard[a+2][b+4] = 0
        elif list.count(2) > list.count(1):
          print("Majority 2")
          assignTo = 2
          if claimTriangle(5) == 1:
            gameBoard[a][b] = gameBoard[a+1][b] = gameBoard[a+1][b+1] = gameBoard[a+1][b+2] = gameBoard[a+2][b] = gameBoard[a+2][b+1] = gameBoard[a+2][b+2] = gameBoard[a+2][b+3] = gameBoard[a+2][b+4] = 0
      b += 2
    a += 1


def checkForT2B():
  if (gameBoard[3][5] and gameBoard[3][4] and gameBoard[3][3] and gameBoard[3][2] and gameBoard[3][1] and gameBoard[4][4] and gameBoard[4][5] and gameBoard[4][3] and gameBoard[5][5]) != 0:
    print("Triangle [4,2] [4,3] [4,4] [4,5] [4,6] [5,4] [5,5] [5,6] [6,6] Filled")
    list = [gameBoard[3][5], gameBoard[3][4], gameBoard[3][3], gameBoard[3][2], gameBoard[3][1], gameBoard[4][4], gameBoard[4][5], gameBoard[4][3], gameBoard[5][5]]
    if list.count(1) > list.count(2):
      print("Majority 1")
      global assignTo
      assignTo = 1
      if claimTriangle(5) == 1:
        gameBoard[3][5] = gameBoard[3][4] = gameBoard[3][3] = gameBoard[3][2] = gameBoard[3][1] = gameBoard[4][4] = gameBoard[4][5] = gameBoard[4][3] = gameBoard[5][5] = 0
    elif list.count(2) > list.count(1):
      print("Majority 2")
      assignTo = 2
      if claimTriangle(5) == 1:
        gameBoard[3][5] = gameBoard[3][4] = gameBoard[3][3] = gameBoard[3][2] = gameBoard[3][1] = gameBoard[4][4] = gameBoard[4][5] = gameBoard[4][3] = gameBoard[5][5] = 0

def playGame(p, turnCounter):
  while True:
    printBoard(x,y)
    p = turnCounter%2
    print(f"Turn {turnCounter+1}")
    print(f"Player {p+1}'s Move")
    inputMove(p)
    checkForT1A()
    checkForT1B()
    checkForT2A()
    checkForT2B()
    print(f"P1 Points: {pointsA}\nP2 Points: {pointsB}")
    turnCounter+=1
    print("\n---------------------------------------")
    if turnCounter == 45:
      break
playGame(p, turnCounter)
if pointsA > pointsB:
  print("Game Over: Player 1 Wins")
if pointsB > pointsA:
  print("Game Over: Player 2 Wins")
if pointsA == pointsB:
  print("Game Over: Tie")
