#grid[x][2] is public one, grid[x][3] is the hidden one.
import os
import random
import time
import save
actions = ["sweep","flag","unflag"]
a = 0
b = 0
c = 0
health = 1
while True:
    play = "yes"
    times = 0
    mines = "none"
    while True:
        action = input("Do you want start a new game or load a save?\n")
        action = action.lower()
        if "load" in action:
            f = open("save.py","r")
            contents = f.read()
            f.close()
            if contents != "":
                grid = save.savegrid
                health = save.health
                boardSize = save.boardSize
                times = save.times
                print ("Board has been loaded.")
                break
            else:
                print ("The save file is empty, save cannot be loaded!")
        elif "new" in action:
            while True:
                boardSize = input("Select size of the grid: '9x9', '20x20'.\n")
                if "9" in boardSize:
                    boardSize = 9
                    break
                elif "20" in boardSize:
                    boardSize = 20
                    break
                else:
                    print ("That is not a valid size!")
            while True:
                health = input("What difficulty do you want to play with? 'Hard', 'Medium' or 'Easy'?\n")
                health = health.lower()
                if "hard" in health:
                    health = 1
                    break
                elif "medium" in health:
                    health = 3
                    break
                elif "easy" in health:
                    health = 5
                    break
                else:
                    print ("That's not a valid difficulty!\n")
            break
        else:
            print ("Please include 'new' or 'load'!\n")
    print ("\nEnter /save at any time to save the game.\n")
    if boardSize == 9:
        yaxis = ["a","b","c","d","e","f","g","h","i"]
        xaxis = [0,1,2,3,4,5,6,7,8,9,"1","2","3","4","5","6","7","8","9"]
    elif boardSize == 20:
        yaxis = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t"]
        xaxis = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
    if "load" not in action:
        print ("Starting Minesweeper...")
        print ("? on a square means it has not been sweeped yet, ! means a squared has been flagged, and the numbers tell you how many mines are adjacent to that square.")
        print ("When you have flagged all the mines, you have to sweep all the remaining squares to complete the game.\n")
        time.sleep(c+a)
        print ("Generating board...")
        time.sleep(a)
        if boardSize == 9:
            c, r = 6, 81
            grid = [[0 for x in range(c)] for y in range(r)]
        elif boardSize == 20:
            c, r = 6, 400
            grid = [[0 for x in range(c)] for y in range(r)]
        for x in range(len(grid)):
            grid[x][0] = yaxis[x//boardSize]#Vilken rad det är.
            grid[x][1] = x-boardSize*(x//boardSize)+1#Vilken kolumn det är.
        for x in range(len(grid)):
            grid[x][2] = "?"
            grid[x][3] = "N/A"
            grid[x][4] = "no"
            grid[x][5] = x
    time.sleep(b)
    os.system('cls')
    while play != "no" and health != 0:
        if times == 0:
            print ("     [Mines: ?] [Flags placed: 0]")
        if boardSize == 9:
            print ("      1  2  3  4  5  6  7  8  9 ")
            for x in range(0,9):
                print ("{}    [{}][{}][{}][{}][{}][{}][{}][{}][{}]".format(yaxis[x].upper(),grid[9*x][2],grid[9*x+1][2],grid[9*x+2][2],grid[9*x+3][2],grid[9*x+4][2],grid[9*x+5][2],grid[9*x+6][2],grid[9*x+7][2],grid[9*x+8][2]))
        elif boardSize == 20:
            print ("      1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20")
            for x in range(0,20):
                print ("{}    [{}][{}][{}][{}][{}][{}][{}][{}][{}][{}][{}][{}][{}][{}][{}][{}][{}][{}][{}][{}]".format(yaxis[x].upper(),grid[20*x][2],grid[20*x+1][2],grid[20*x+2][2],grid[20*x+3][2],grid[20*x+4][2],grid[20*x+5][2],grid[20*x+6][2],grid[20*x+7][2],grid[20*x+8][2],grid[20*x+9][2],grid[20*x+10][2],grid[20*x+11][2],grid[20*x+12][2],grid[20*x+13][2],grid[20*x+14][2],grid[20*x+15][2],grid[20*x+16][2],grid[20*x+17][2],grid[20*x+18][2],grid[20*x+19][2]))
        print ("[Health: %d]"%(health))
        while True:
            if times == 0:
                print ("Enter the coordinates of the square and then what you want to do with it ('flag', 'unflag' or 'sweep').\n")
            square = input("Enter the coordinates.\n")
            action = input("Enter the action.\n")
            action = action.lower()
            square = square.lower()
            if "save" in square or "save" in action:
                print ("Alright, saving the board.")
                string = "boardSize = "+str(boardSize)+"\nhealth = "+str(health)+"\ntimes = "+str(times)+"\nsavegrid = "+str(grid)
                f = open("save.py","w")
                f.write(string)
                f.close()
                print ("Done.\n")
                time.sleep(b)
                break
            elif times == 0 and action != "sweep":
                print ("The first action should be a sweep.")
            elif action in actions:
                square = square.replace(" ","")
                square = list(square)
                if len(square) > 1:
                    if square[0] in yaxis:
                        if square[-1] in yaxis:
                            print ("Write the coordinates properly!\n")
                        else:
                            square0 = square[0]#Saves the letter of the square
                            square.pop(0)#Removes the letter from square
                            square = [int("".join(square))]#Joins the numbers of the square together.
                            square.insert(0,square0)#Adds the letter back.
                            if square[0] in yaxis and square[1] in xaxis:
                                break
                            else:
                                print ("Write the coordinates of the square properly.")
                    elif square[0] in xaxis:
                        if square[-1] in xaxis:
                            print ("Write the coordinates of the square properly.")
                        else:
                            square1 = square[1]#Saves the letter of the square
                            square.pop(1)#Removes the letter from square
                            square = [int("".join(square))]#Joins the numbers of the square together.
                            square.insert(0,square1)#Adds the letter back.
                            if square[0] in yaxis and square[1] in xaxis:
                                break
                            else:
                                print ("Write the coordinates of the square properly.")
                    elif square[2] in yaxis:
                        square2 = square[2]#Saves the letter of the square
                        square.pop(2)#Removes the letter from square
                        square = [int("".join(square))]#Joins the numbers of the square together.
                        square.insert(0,square2)#Adds the letter back.
                        if square[0] in yaxis and square[1] in xaxis:
                            break
                        else:
                            print ("Write the coordinates of the square properly.")
                    else:
                        print ("Write the coordinates of the square properly.")
                else:
                    print ("Write properly.")
            else:
                print ("You have to include the action!")
        for x in range (len(grid)):
            if grid[x][0] == square[0] and grid[x][1] == square[1]:
                if grid[x][4] == "yes":
                    if action == "sweep":
                        print ("You have already sweeped that square.")
                        time.sleep(a)
                    elif action == "flag":
                        print ("You cannot flag a sweeped square.")
                        time.sleep(a)
                    break
                if action == "unflag":
                  print ("Marking the selected square as '?'")
                  grid[x][2] = "?"
                  time.sleep(a)
                elif action == "sweep":
                    if times == 0:
                        grid[x][2] = "number"
                        grid[x][3] = "number"
                        grid[x][4] = "yes"
                        y = x
                        toRemove = []
                        adj = []
                        if boardSize == 9:#This seems to work.
                            additions = [-1,-8, -9, -10, 1, 8, 9, 10]
                        elif boardSize == 20:
                            additions = [-1, -19, -20, -21, 1, 19, 20, 21]
                        if grid[y][1] == 1:
                            toRemove.append(additions[0])
                            toRemove.append(additions[3])
                            toRemove.append(additions[5])
                        if grid[y][1] == 9:
                            toRemove.append(additions[1])
                            toRemove.append(additions[4])
                            toRemove.append(additions[7])
                        if grid[y][0] == "a":
                            toRemove.append(additions[1])
                            toRemove.append(additions[2])
                            toRemove.append(additions[3])
                        if grid[y][0] == "i":
                            toRemove.append(additions[5])
                            toRemove.append(additions[6])
                            toRemove.append(additions[7])
                        additions = [x for x in additions if x not in toRemove]
                        for x in additions:
                            if y+x < boardSize ** 2 - 1:
                                adj.append(grid[y+x])
                        break
                    else:
                        if grid[x][2] == "!":
                          print ("That square has been flagged. Remove the flag to sweep the square.")
                          time.sleep(a)
                          break
                        elif grid[x][3] == "x":
                            if health == 1:
                                os.system('cls')
                                time.sleep(a)
                                print ("You sweeped a square, but there was a mine there. You have exploded.")
                                health = 0
                            else:
                                print ("You sweeped a square, but there was a mine there. You lost 1 health.\n")
                                health -= 1
                            time.sleep(b)
                            break
                        elif grid[x][3] in xaxis:
                            grid[x][2] = grid[x][3]
                            grid[x][4] = "yes"
                elif action == "flag":
                    grid[x][2] = "!"
                    break
                else:
                    print ("Error, action is not either flag or sweep...")
        if times == 0 and "save" not in square:
            for x in range (len(grid)):
                if x != y:
                    hidden = random.randint(1,100)
                    if hidden < 30:
                        grid[x][3] = "x"
                    else:
                        grid[x][3] = "number"
        bombas = 0
        for p in range(len(grid)):
            if grid[p][3] == "x":#They will be either "x" or "number" here.
                bombas += 1
        if times == 0:
            for x in range (len(grid)):#The code below does not work as perfectly. Some squares show  instead of 0.
                if grid[x][3] != "x" and grid[x][3] != "N/A":
                    tempAdj = []
                    bombCount = 0
                    toRemove = []
                    if boardSize == 9:
                        additions = [-1, -8, -9, -10, 1, 8, 9, 10]
                    elif boardSize == 20:
                        additions = [-1, -19, -20, -21, 1, 19, 20, 21]
                    if grid[x][1] == 1:
                        toRemove.append(additions[0])
                        toRemove.append(additions[3])
                        toRemove.append(additions[5])
                    if grid[x][1] == boardSize:
                        toRemove.append(additions[1])
                        toRemove.append(additions[4])
                        toRemove.append(additions[7])
                    if grid[x][0] == "a":
                        toRemove.append(additions[1])
                        toRemove.append(additions[2])
                        toRemove.append(additions[3])
                    if grid[x][0] == yaxis[-1]:
                        toRemove.append(additions[5])
                        toRemove.append(additions[6])
                        toRemove.append(additions[7])
                    additions = [temp for temp in additions if temp not in toRemove]
                    for number in additions:
                        if x+number < boardSize ** 2:#Removed the -1, might work now.
                            tempAdj.append(grid[x+number])
                    for temp in range(len(tempAdj)):
                        if tempAdj[temp][3] == "x":
                            bombCount += 1
                    grid[x][3] = bombCount
                    if x == y:
                        grid[x][2] = bombCount
        if times == 0 and "save" not in square: #Shows the squares adjacent to the first selected one.
            for x in adj:
                if x[3] != "x":
                    x[2] = x[3] #adj[x][5] = index of the adjacent one.
                    x[4] = "yes"
        correct = 0
        flags = 0
        sweeped = 0
        mines = 0
        for x in range (len(grid)):
            if grid[x][3] != "x":
                if grid[x][2] == grid[x][3]:
                    sweeped += 1
            if grid[x][3] == "x":
                mines += 1
            if grid[x][2] == "!":
                flags += 1
        for x in range (len(grid)):
            if grid[x][2] == "!" and grid[x][3] == "x":
                correct += 1
            if correct == mines and sweeped == len(grid) - mines:
                print ("You have succesfully marked all the mines.")
                play = "no"
                time.sleep(c)
                break
        os.system('cls')
        if "save" not in square:
            times += 1
        if times > 0:
            if health != 0 and play != "no":
                print ("     [Mines: {}] [Flags placed: {}]".format(mines, flags))
    while True:
        action = input("Do you want to go again? Y/N \n")
        action = action.lower()
        if "n" in action:
            print ("Alright, exiting.")
            timme.sleep(c)
            import sys
            sys.exit()
        elif "y" in action:
            print ("Alright, restarting...")
            time.sleep(c)
            break
        else:
            print ("%d is not an option." %(action))
