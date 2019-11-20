import random, time, csv
import tkinter as tk
''' IF YOU HAVE ANY ISSUES WITH THE SIZE OF YOUR SCREEN IN SHOWING THE GRID LAYOUTS MAKE ADJUSTMENTS IN THE LAYOUT
FUNCTION ON LINE 136 BY DECREASING THE btnWidth and btnHeight values.

The following file memoryBestTimes.csv will be created in the game directory to keep track of the scores for future use.'''

btnFont = ('Verdana', 11)
scFont = ('Verdana', 14)
randBtns = []
currBtns = []
clicked = []
score = 0
firstGuess = 0
firstIndex = 0
secondGuess = 0
secondIndex = 0
firstBtn = 0
firstBtnVal = 0
firstBtnId = 0
disBtns = 0
scoresData = []
scoresFile = 'memoryBestTimes.csv'

root = tk.Tk()

# Button StringVar's Setup for up to 10x10 layout
d0 = tk.StringVar(); d1 = tk.StringVar(); d2 = tk.StringVar(); d3 = tk.StringVar(); d4 = tk.StringVar()
d5 = tk.StringVar(); d6 = tk.StringVar(); d7 = tk.StringVar(); d8 = tk.StringVar(); d9 = tk.StringVar()
d10 = tk.StringVar(); d11 = tk.StringVar(); d12 = tk.StringVar(); d13 = tk.StringVar(); d14 = tk.StringVar()
d15 = tk.StringVar(); d16 = tk.StringVar(); d17 = tk.StringVar(); d18 = tk.StringVar(); d19 = tk.StringVar()
d20 = tk.StringVar(); d21 = tk.StringVar(); d22 = tk.StringVar(); d23 = tk.StringVar(); d24 = tk.StringVar()
d25 = tk.StringVar(); d26 = tk.StringVar(); d27 = tk.StringVar(); d28 = tk.StringVar(); d29 = tk.StringVar()
d30 = tk.StringVar(); d31 = tk.StringVar(); d32 = tk.StringVar(); d33 = tk.StringVar(); d34 = tk.StringVar()
d35 = tk.StringVar(); d36 = tk.StringVar(); d37 = tk.StringVar(); d38 = tk.StringVar(); d39 = tk.StringVar()
d40 = tk.StringVar(); d41 = tk.StringVar(); d42 = tk.StringVar(); d43 = tk.StringVar(); d44 = tk.StringVar()
d45 = tk.StringVar(); d46 = tk.StringVar(); d47 = tk.StringVar(); d48 = tk.StringVar(); d49 = tk.StringVar()
d50 = tk.StringVar(); d51 = tk.StringVar(); d52 = tk.StringVar(); d53 = tk.StringVar(); d54 = tk.StringVar()
d55 = tk.StringVar(); d56 = tk.StringVar(); d57 = tk.StringVar(); d58 = tk.StringVar(); d59 = tk.StringVar()
d60 = tk.StringVar(); d61 = tk.StringVar(); d62 = tk.StringVar(); d63 = tk.StringVar(); d64 = tk.StringVar()
d65 = tk.StringVar(); d66 = tk.StringVar(); d67 = tk.StringVar(); d68 = tk.StringVar(); d69 = tk.StringVar()
d70 = tk.StringVar(); d71 = tk.StringVar(); d72 = tk.StringVar(); d73 = tk.StringVar(); d74 = tk.StringVar()
d75 = tk.StringVar(); d76 = tk.StringVar(); d77 = tk.StringVar(); d78 = tk.StringVar(); d79 = tk.StringVar()
d80 = tk.StringVar(); d81 = tk.StringVar(); d82 = tk.StringVar(); d83 = tk.StringVar(); d84 = tk.StringVar()
d85 = tk.StringVar(); d86 = tk.StringVar(); d87 = tk.StringVar(); d88 = tk.StringVar(); d89 = tk.StringVar()
d90 = tk.StringVar(); d91 = tk.StringVar(); d92 = tk.StringVar(); d93 = tk.StringVar(); d94 = tk.StringVar()
d95 = tk.StringVar(); d96 = tk.StringVar(); d97 = tk.StringVar(); d98 = tk.StringVar(); d99 = tk.StringVar()

# Button Setup for up to 10x10 layout
mainLayout = {0 : [['A0', d0, 'b0'], ['A1', d1, 'b1'], ['A2', d2, 'b2'], ['A3', d3, 'b3'], ['A4', d4, 'b4'], ['A5', d5, 'b5'],
                   ['A6', d6, 'b6'], ['A7', d7, 'b7'], ['A8', d8, 'b8'], ['A9', d9, 'b9']],
              1 : [['B0', d10, 'b10'], ['B1', d11, 'b11'], ['B2', d12, 'b12'], ['B3', d13, 'b13'], ['B4', d14, 'b14'], ['B5', d15, 'b15'],
                   ['B6', d16, 'b16'], ['B7', d17, 'b17'], ['B8', d18, 'b18'], ['B9', d19, 'b19']],
              2 : [['C0', d20, 'b20'], ['C1', d21, 'b21'], ['C2', d22, 'b22'], ['C3', d23, 'b23'], ['C4', d24, 'b24'], ['C5', d25, 'b25'],
                   ['C6', d26, 'b26'], ['C7', d27, 'b27'], ['C8', d28, 'b28'], ['C9', d29, 'b29']],
              3 : [['D0', d30, 'b30'], ['D1', d31, 'b31'], ['D2', d32, 'b32'], ['D3', d33, 'b33'], ['D4', d34, 'b34'], ['D5', d35, 'b35'],
                   ['D6', d36, 'b36'], ['D7', d37, 'b37'], ['D8', d38, 'b38'], ['D9', d39, 'b39']],
              4 : [['E0', d40, 'b40'], ['E1', d41, 'b41'], ['E2', d42, 'b42'], ['E3', d43, 'b43'], ['E4', d44, 'b44'], ['E5', d45, 'b45'],
                   ['E6', d46, 'b46'], ['E7', d47, 'b47'], ['E8', d48, 'b48'], ['E9', d49, 'b49']],
              5 : [['F0', d50, 'b50'], ['F1', d51, 'b51'], ['F2', d52, 'b52'], ['F3', d53, 'b53'], ['F4', d54, 'b54'], ['F5', d55, 'b55'],
                   ['F6', d56, 'b56'], ['F7', d57, 'b57'], ['F8', d58, 'b58'], ['F9', d59, 'b59']],
              6 : [['G0', d60, 'b60'], ['G1', d61, 'b61'], ['G2', d62, 'b62'], ['G3', d63, 'b63'], ['G4', d64, 'b64'], ['G5', d65, 'b65'],
                   ['G6', d66, 'b66'], ['G7', d67, 'b67'], ['G8', d68, 'b68'], ['G9', d69, 'b69']],
              7 : [['H0', d70, 'b70'], ['H1', d71, 'b71'], ['H2', d72, 'b72'], ['H3', d73, 'b73'], ['H4', d74, 'b74'], ['H5', d75, 'b75'],
                   ['H6', d76, 'b76'], ['H7', d77, 'b77'], ['H8', d78, 'b78'], ['H9', d79, 'b79']],
              8 : [['I0', d80, 'b80'], ['I1', d81, 'b81'], ['I2', d82, 'b82'], ['I3', d83, 'b83'], ['I4', d84, 'b84'], ['I5', d85, 'b85'],
                   ['I6', d86, 'b86'], ['I7', d87, 'b87'], ['I8', d88, 'b88'], ['I9', d89, 'b89']],
              9 : [['J0', d90, 'b90'], ['J1', d91, 'b91'], ['J2', d92, 'b92'], ['J3', d93, 'b93'], ['J4', d94, 'b94'], ['J5', d95, 'b95'],
                   ['J6', d96, 'b96'], ['J7', d97, 'b97'], ['J8', d98, 'b98'], ['J9', d99, 'b99']]}

# Reads in previous score data if present.
def readFile():
    global grid4; global grid6; global grid8; global grid10
    global grid4Top; global grid6Top; global grid8Top; global grid10Top
    with open(scoresFile, 'r') as gameData:
        data = csv.reader(gameData)
        for line in data:
            grid4 = int(line[0])
            grid6 = int(line[1])
            grid8 = int(line[2])
            grid10 = int(line[3])
    # As the data is in seconds, now makes it into a time format for game layout.
    mins4, secs4 = divmod(grid4, 60)
    grid4Top = str(mins4).zfill(2) + ':' + str(secs4).zfill(2)
    mins6, secs6 = divmod(grid6, 60)
    grid6Top = str(mins6).zfill(2) + ':' + str(secs6).zfill(2)
    mins8, secs8 = divmod(grid8, 60)
    grid8Top = str(mins8).zfill(2) + ':' + str(secs8).zfill(2)
    mins10, secs10 = divmod(grid10, 60)
    griid10Top = str(mins10).zfill(2) + ':' + str(secs10).zfill(2)
    gameData.close()

# Writes score data in pwd for future playing creating a csv file.
def writeFile():
    global grid4; global grid6; global grid8; global grid10
    data = grid4, grid6, grid8, grid10
    with open(scoresFile, 'w+', newline='') as gameData:
        nsd = csv.writer(gameData)
        nsd.writerow(data)
    gameData.close()

# Checks data in a list for which grid game used and checks for previous and makes adjustment if required.
def topScoresCheck():
    global grid4; global grid6; global grid8; global grid10
    global grid4Top; global grid6Top; global grid8Top; global grid10Top# [useGrid, guess, score - 1, timing]
    if scoresData[-1][0] == 4:
        if scoresData[-1][2] < grid4:
            grid4 = scoresData[-1][2]
            grid4Top = scoresData[-1][3]
            writeFile()
    elif scoresData[-1][0] == 6:
        if scoresData[-1][2] < grid6:
            grid6 = scoresData[-1][2]
            grid6Top = scoresData[-1][3]
            writeFile()
    elif scoresData[-1][0] == 8:
        if scoresData[-1][2] < grid8:
            grid8 = scoresData[-1][2]
            grid8Top = scoresData[-1][3]
            writeFile()
    elif scoresData[-1][0] == 10:
        if scoresData[-1][2] < grid10:
            grid10 = scoresData[-1][2]
            grid10Top = scoresData[-1][3]
            writeFile()

# Game layout taking in which grid and best time arguments to display in game.
def layout(useGrid, currGridBest):
    def count():
        global score; global keepScoring; global timing
        if keepScoring == True:     
            score += 1
            mins, secs = divmod(score - 1, 60)
            timing = str(mins).zfill(2) + ':' + str(secs).zfill(2)
            timeArea.config(text='TIME: {}'.format(timing))
            timeArea.after(1000, count)

    ########## Adjust layout so fits on screen, if you find you need to change make adjustments here. #########
    if useGrid >= 8: ### For grids 8x8 and 10x10.
        btnWidth = 3
        btnHeight = 1
    else: ### For grids 4x4 and 6x6.
        btnWidth = 5
        btnHeight = 2
    global gameFrame
    gameFrame.destroy()       
    global score
    score = 0
    global guess
    global startScore
    startScore = True
    global keepScoring
    keepScoring = True
    guess = 0
    global validPair
    validPair = False
    randBtns.clear(); currBtns.clear()
    for i in range(1, int(((useGrid * useGrid) / 2) + 1)):
        randBtns.append(i)
        randBtns.append(i)
    random.shuffle(randBtns)
    gameFrame = tk.Frame(root, bg='grey')
    gameFrame.pack(padx=10, pady=10)
    btnNum = 0; currBtn = 0
    useRow = 0; useCol = 0; showGrid = useGrid * useGrid
    for row in range(useGrid):
        for col in range(useGrid):
            if useCol == useGrid:
                useRow += 1
                useCol = 0
            global btnText; global btnId
            btnText = mainLayout[useRow][useCol][1]
            btnId = mainLayout[useRow][useCol][2]
            button = tk.Button(gameFrame, textvariable=btnText, width=btnWidth, height=btnHeight, command=lambda myBtn=btnText,
                               myId=currBtn: revealBtn(myBtn, myId, useGrid), activebackground='lightgreen', bg='white', font=btnFont)
            button.grid(row=useRow + 1, column=useCol, padx=3, pady=3)
            btnText.set(mainLayout[useRow][useCol][0])
            currBtns.append(button)
            btnNum += 1
            useCol += 1
            currBtn += 1
    global timeArea
    timeArea = tk.Label(gameFrame, text='TIME: {}'.format(score), font=scFont, bg='grey')
    timeArea.grid(row=useRow + 2, columnspan=useCol, pady=5)
    bestTime = tk.Label(gameFrame, text='BEST TIME: {}'.format(currGridBest), font=scFont, fg='red', bg='grey')
    bestTime.grid(row=0, columnspan=useCol, pady=5)
    global total
    total = len(currBtns)
    if startScore == True:
        count()

def revealBtn(btnPressed, myId, useGrid):
    global guess; global firstGuess; global firstGuessId; global firstBtn; global firstBtnVal; global firstIndex
    global secondIndex; global score; global firstBtnId; global btnId; global disBtns; global timeArea
    global keepScoring; global secondGuess; global startScore
    guess += 1
    keepScoring = True
    startScore = True
    global total
    rowCol = str(btnPressed)
    row_col = rowCol[6:]
    if len(row_col) == 1:
        row = 0
        col = row_col
    else:
        row = row_col[0]
        col = row_col[1]
    guessIndex = 0
    for i in range(useGrid):
        for ii in range(useGrid):
            strVarBtn = mainLayout[i][ii][1]
            strVarVal = mainLayout[i][ii][0]
            if int(row) == i and int(col) == ii:
                if guess % 2 == 1: # First guess
                    strVarBtn.set(randBtns[guessIndex])
                    firstIndex = guessIndex
                    firstGuess = randBtns[guessIndex]
                    firstBtn = strVarBtn
                    firstBtnVal = strVarVal
                    firstBtnId = myId
                    currBtns[myId].config(bg='lightgreen', state='disabled')
                elif guess % 2 == 0:
                    strVarBtn.set(randBtns[guessIndex])
                    secondIndex = guessIndex
                    secondGuess = randBtns[guessIndex]
                    if secondGuess == firstGuess: # Pair found
                        currBtns[firstBtnId].config(state='disabled', bg='yellow')
                        currBtns[myId].config(state='disabled', bg='yellow')
                        disBtns += 2
                        if disBtns == total: # Check if all pairs complete, stop scoring
                            keepScoring = False
                            disBtns = 0
                            scoresData.append([useGrid, guess, score - 1, timing])
                            topScoresCheck()
                    else:
                        strVarBtn.set(secondGuess)
                        currBtns[myId].config(bg='red')
                        root.update()
                        currBtns[firstBtnId].after(1000, currBtns[firstBtnId].config(bg='white', state='normal'))
                        currBtns[myId].config(bg='white')
                        firstBtn.set(firstBtnVal)
                        strVarBtn.set(strVarVal)
            guessIndex += 1        

try:
    readFile()
except:
    grid4 = 1000
    grid4Top = '--:--'
    grid6 = 1000
    grid6Top = '--:--'
    grid8 = 1000
    grid8Top = '--:--'
    grid10 = 1000
    grid10Top = '--:--'

global gameFrame
gameFrame = tk.Frame(root, bg='grey', width=265, height=290)
gameFrame.pack()
root.title('Memory')
menu = tk.Menu(root)
root.config(menu=menu)
subMenu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label='Game', menu=subMenu)
subMenu.add_command(label='4x4', command=lambda: layout(4, grid4Top))
subMenu.add_command(label='6x6', command=lambda: layout(6, grid6Top))
subMenu.add_command(label='8x8', command=lambda: layout(8, grid8Top))
subMenu.add_command(label='10x10', command=lambda: layout(10, grid10Top))

root.mainloop()
