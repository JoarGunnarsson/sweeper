#grid[x][2] is public one, grid[x][3] is the hidden one.
#Give the player health. Hard = 1 hp, Medium = 3 hp, Easy = 5 hp.
#Square A2 (index '1') showed the number '0', while it should have been a '1'. Might be because of 'grid[x-1][3]' thingy.
#Square B2 (index '10') showed the number '1', while it should have been a '2'. Might be because of ^.
#Do so that even numbers in the adjacent can be '?'.
import os
import random
import time
import save
yaxis = ["a","b","c","d","e","f","g","h","i"]
xaxis = [0,1,2,3,4,5,6,7,8,9,"1","2","3","4","5","6","7","8","9"]
a = 1
b = 2
c = 3
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
                print ("Board has been loaded.")
                times = 1
                break
            else:
                print ("The save file is empty, cannot load save!")
        else:
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
    print ("Enter /save at any time to save the game.\n")
    if "load" not in action:
        print ("Starting Minesweeper...")
        print ("? on a square means it has not been sweeped yet, ! means a squared has been flagged, and the numbers tell you how many mines are adjacent to that square.")
        print ("When you have flagged all the mines, you have to sweep all the remaining squares to complete the game.\n")
        print ("Generating board...")
        time.sleep(c+b)
        c, r = 6, 81
        grid = [[0 for x in range(c)] for y in range(r)]
        for x in range(len(grid)):
            letter = x/9
            if letter < 1:
                grid[x][0] = "a"
                grid[x][1] = x+1
            if letter >= 1 and letter < 2:
                grid[x][0] = "b"
                grid[x][1] = x-8
            if letter >= 2 and letter < 3:
                grid[x][0] = "c"
                grid[x][1] = x-16-1
            if letter >= 3 and letter < 4:
                grid[x][0] = "d"
                grid[x][1] = x-24-2
            if letter >= 4 and letter < 5:
                grid[x][0] = "e"
                grid[x][1] = x-32-3
            if letter >= 5 and letter < 6:
                grid[x][0] = "f"
                grid[x][1] = x-40-4
            if letter >= 6 and letter < 7:
                grid[x][0] = "g"
                grid[x][1] = x-48-5
            if letter >= 7 and letter < 8:
                grid[x][0] = "h"
                grid[x][1] = x-56-6
            if letter >= 8 and letter < 9:
                grid[x][0] = "i"
                grid[x][1] = x-64-7
        for x in range(len(grid)):
            grid[x][2] = "?"
            grid[x][3] = "N/A"
            grid[x][4] = "no"
            grid[x][5] = x
    time.sleep(b)
    os.system('cls')
    while play != "no" and health != 0:
        print ("     [Health: %d]"%(health))
        print ("      1  2  3  4  5  6  7  8  9 ")
        print ("A    [{}][{}][{}][{}][{}][{}][{}][{}][{}]".format(grid[0][2], grid[1][2],grid[2][2],grid[3][2],grid[4][2],grid[5][2],grid[6][2],grid[7][2],grid[8][2]))
        print ("B    [{}][{}][{}][{}][{}][{}][{}][{}][{}]".format(grid[9][2], grid[10][2],grid[11][2],grid[12][2],grid[13][2],grid[14][2],grid[15][2],grid[16][2],grid[17][2]))
        print ("C    [{}][{}][{}][{}][{}][{}][{}][{}][{}]".format(grid[18][2], grid[19][2],grid[20][2],grid[21][2],grid[22][2],grid[23][2],grid[24][2],grid[25][2],grid[26][2]))
        print ("D    [{}][{}][{}][{}][{}][{}][{}][{}][{}]".format(grid[27][2], grid[28][2],grid[29][2],grid[30][2],grid[31][2],grid[32][2],grid[33][2],grid[34][2],grid[35][2]))
        print ("E    [{}][{}][{}][{}][{}][{}][{}][{}][{}]".format(grid[36][2], grid[37][2],grid[38][2],grid[39][2],grid[40][2],grid[41][2],grid[42][2],grid[43][2],grid[44][2]))
        print ("F    [{}][{}][{}][{}][{}][{}][{}][{}][{}]".format(grid[45][2], grid[46][2],grid[47][2],grid[48][2],grid[49][2],grid[50][2],grid[51][2],grid[52][2],grid[53][2]))
        print ("G    [{}][{}][{}][{}][{}][{}][{}][{}][{}]".format(grid[54][2], grid[55][2],grid[56][2],grid[57][2],grid[58][2],grid[59][2],grid[60][2],grid[61][2],grid[62][2]))
        print ("H    [{}][{}][{}][{}][{}][{}][{}][{}][{}]".format(grid[63][2], grid[64][2],grid[65][2],grid[66][2],grid[67][2],grid[68][2],grid[69][2],grid[70][2],grid[71][2]))
        print ("I    [{}][{}][{}][{}][{}][{}][{}][{}][{}]".format(grid[72][2], grid[73][2],grid[74][2],grid[75][2],grid[76][2],grid[77][2],grid[78][2],grid[79][2],grid[80][2]))
        while True:
            if times == 0:
                square = input("Enter the coordinates of the square you want to sweep/flag (e.g A5) and what you want to do with it ('flag', 'unflag' or 'sweep').\n")
            else:
                square = input("Enter the coordinates of the square.\n")
            square = square.lower()
            if "save" in square:
                print ("Alright, saving the board.")
                f = open("save.py","w")
                f.write("health = ")
                f.write(str(health))
                f.write("\nsavegrid = ")
                f.write(str(grid))
                f.close()
                print ("Done.\n")
                time.sleep(b)
                break
            elif times == 0 and "sweep" not in square:
                print ("The first action should be a sweep.")
            elif 'unflag' in square:
                action = 'unflag'
                square = square.replace("unflag","")
                square = square.replace(" ","")
                square = list(square)
                if len(square) != 2:
                    print ("Write the coordinates of the square properly.")
                elif square[0] not in yaxis:
                    print ("Write the coordinates of the square properly.")
                elif square[1] not in xaxis:
                    print ("Write the coordinates of the square properly.")
                else:
                    if square [1] in xaxis:
                        square[1] = int(square[1])
                    elif square [1] in yaxis:
                        square[1] = int(square[0])
                    break
            elif 'flag' in square:
                action = 'flag'
                square = square.replace("flag","")
                square = square.replace(" ","")
                square = list(square)
                if len(square) != 2:
                    print ("Write the coordinates of the square properly.")
                elif square[0] not in yaxis:
                    print ("Write the coordinates of the square properly.")
                elif square[1] not in xaxis:
                    print ("Write the coordinates of the square properly.")
                else:
                    if square [1] in xaxis:
                        square[1] = int(square[1])
                    elif square [1] in yaxis:
                        square[1] = int(square[0])
                    break
            elif 'sweep' in square:
                action = 'sweep'
                square = square.replace("sweep","")
                square = square.replace(" ","")
                square = list(square)
                if len(square) != 2:
                    print ("Write the coordinates of the square properly.")
                else:
                    if square [1] in xaxis:
                        square[1] = int(square[1])
                        break
                    elif square [1] in yaxis:
                        square1 = square[1]
                        square[1] = int(square[0])
                        square[0] = square1
                        break
                    else:
                        print ("Write the coordinates of the square properly.")
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
                        if grid[x][1] == 1:
                            if grid[x][0] == "a":
                                adj = [grid[y+1], grid[y+10], grid[y+9]]
                            elif grid[x][0] == "i":
                                adj = [grid[y+1], grid[y-9], grid[y-8]]
                            else:
                                adj = [grid[y+1], grid[y-9], grid[y-8], grid[y+10], grid[y+9]]
                        elif grid[x][1] == 9:
                            if grid[x][0] == "a":
                                adj = [grid[y-1], grid[y+9], grid[y+8]]
                            elif grid[x][0] == "i":
                                adj = [grid[y-1], grid[y-10], grid[y-9]]
                            else:
                                adj = [grid[y-1], grid[y-10], grid[y-9], grid[y+9], grid[y+8]]
                        elif grid[x][1] == 2:
                            if grid[x][0] == "a":
                                adj = [grid[y-1], grid[y+1], grid[y+10], grid[y+9], grid[y+8]]
                            elif grid[x][0] == "b":
                                adj = [grid[y-1], grid[y+1], grid[y-10], grid[y-9], grid[y-8], grid[y+10], grid[y+9], grid[y+8]]
                            elif grid[x][0] == "h":
                                adj = [grid[y-1], grid[y+1], grid[y-10], grid[y-9], grid[y-8], grid[y+10], grid[y+9], grid[y+8]]
                            elif grid[x][0] == "i":
                                adj = [grid[y-1], grid[y+1], grid[y-10], grid[y-9], grid[y-8]]
                            else:
                                adj = [grid[y-1], grid[y+1], grid[y-10], grid[y-9], grid[y-8], grid[y+10], grid[y+9], grid[y+8]]
                        elif grid[x][1] == "8":
                            if grid[x][0] == "a":
                                adj = [grid[y-1], grid[y+1], grid[y+10], grid[y+9], grid[y+8]]
                            elif grid[x][0] == "b":
                                adj = [grid[y-1], grid[y+1], grid[y-10], grid[y-9], grid[y-8], grid[y+10], grid[y+9], grid[y+8]]
                            elif grid[x][0] == "h":
                                adj = [grid[y-1], grid[y+1], grid[y-10], grid[y-9], grid[y-8], grid[y+10], grid[y+9], grid[y+8]]
                            elif grid[x][0] == "i":
                                adj = [grid[y+1], grid[y-1], grid[y-2], grid[y-10], grid[y-9], grid[y-8]]
                            else:
                                adj = [grid[y-1], grid[y+1], grid[y-10], grid[y-9], grid[y-8], grid[y+10], grid[y+9], grid[y+8]]

                        elif grid[x][0] == "a":
                            adj = [grid[y-1], grid[y+1], grid[y+10], grid[y+9], grid[y+8]]
                        elif grid[x][0] == "b":
                            adj = [grid[y-1], grid[y+1], grid[y-10], grid[y-9], grid[y-8], grid[y+10], grid[y+9], grid[y+8]]
                        elif grid[x][0] == "h":
                            adj = [grid[y-1], grid[y+1], grid[y-10], grid[y-9], grid[y-8], grid[y+10], grid[y+9], grid[y+8]]
                        elif grid[x][0] == "i":
                            adj = [grid[y-1], grid[y+1], grid[y-10], grid[y-9], grid[y-8]]
                        else:
                            adj = [grid[y-1], grid[y+1], grid[y-10], grid[y-9], grid[y-8], grid[y+10], grid[y+9], grid[y+8]]## == FULLSQUARE
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
                            #Do an ascii explosion here.
                            break
                        elif grid[x][3] in xaxis:
                            grid[x][2] = grid[x][3]
                            grid[x][4] = "yes"


                elif action == "flag":
                    grid[x][2] = "!"
                    break
                else:
                    print ("Error, action != either flag or sweep...")
        if times == 0:
            for x in range (len(grid)):
                if x != y:
                    hidden = random.randint(1,100)
                    if hidden < 30:
                        grid[x][3] = "x"
                    else:
                        grid[x][3] = "number"
        if times == 0:
            for x in range (len(grid)):
                if grid[x][3] != "x":
                    number = 0
                    if grid[x][1] != 1 and grid[x][1] != 9:
                        if x > 0:
                            if grid[x-1][3] == "x":
                                number += 1
                        if x > 7:
                            if grid[x-8][3] == "x":
                                number += 1
                        if x > 8:
                            if grid[x-9][3] == "x":
                                number += 1
                        if x > 9:
                            if grid[x-10][3] == "x":
                                number += 1
                        if x < 71:
                            if grid[x+10][3] == "x":
                                number += 1
                        if x < 72:
                            if grid[x+9][3] == "x":
                                number += 1
                        if x < 73:
                            if grid[x+8][3] == "x":
                                number += 1
                        if x < 80 and grid[x][1] != 9:
                            if grid[x+1][3] == "x":
                                number += 1

                    elif grid[x][1] == 1:#-8 och -9
                        if x > 7:#was 8
                            if grid[x-8][3] == "x":
                                number += 1
                        if x > 8:#was 9
                            if grid[x-9][3] == "x":
                                number += 1
                        if x < 71:#was 70
                            if grid[x+10][3] == "x":
                                number += 1
                        if x < 72:#was 71
                            if grid[x+9][3] == "x":
                                number += 1
                        if x < 80:#was 79 and grid[x][1] != 9
                            if grid[x+1][3] == "x":
                                number += 1

                    elif grid[x][1] == 9:
                        number = 0
                        if x > 0:#was 1
                            if grid[x-1][3] == "x":
                                number += 1
                        if x > 8:#was 9
                            if grid[x-9][3] == "x":
                                number += 1
                        if x > 9: #was 10
                            if grid[x-10][3] == "x":
                                number += 1
                        if x < 72:#was 71
                            if grid[x+9][3] == "x":
                                number += 1
                        if x < 73:#was 72
                            if grid[x+8][3] == "x":
                                number += 1
                    if x == y:
                        grid[x][2] = number
                    grid[x][3] = number
        if times == 0: #Shows the squares near the first selected one. Change this into near.
            for x in range (len(adj)):
                if adj[x][3] != "x":
                    grid[adj[x][5]][2] = grid[adj[x][5]][3] #adj[x][5] = index of the adjacent one.
                    grid[adj[x][5]][4] = "yes"
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
        if health != 0:
            print ("     [Mines: {}] [Flags placed: {}]".format(mines, flags))
        times = 1
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
    else:
        print ("%d is not an option." %(action))
