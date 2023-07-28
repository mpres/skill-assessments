#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Mprelsey 7/24/23
import os
import sys
import random
import time
import re


# In[3]:


def printGrid(grid,round):
    print('###############')
    print('')
    print('### Round',round, '###' )
    print('')
    print('###############')
    print('')
    print('Current Board')
    print('')
    print('~~~~~~~~~~~~~~')
    print('     ','0','1','2')
    i = 0
    for g in grid:
        print("   ",i,g[0],g[1],g[2])
        i += 1
    print('~~~~~~~~~~~~~~')
    print('')


# In[4]:


#Mpresley 7/24/23 create lookForWin, (this will be ran after each move), 


# In[6]:


def lookForWin(grid):
    #look for three in a row up top

    if (grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2] and grid[0][0] != '.'):
        return("Congratulations",grid[0][0]," you got three in a row!") 
    elif (grid[1][0] == grid[1][1] and grid[1][0] == grid[1][2] and grid[1][0] != '.'):
        return("Congratulations",grid[1][0]," you got three in a row!") 
    elif (grid[2][0] == grid[2][1] and grid[2][0] == grid[2][2] and grid[2][0] != '.'):
        return("Congratulations",grid[2][0]," you got three in a row!") 

    elif (grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0] and grid[0][0] != '.'):
        return("Congratulations",grid[0][0]," you got three in the left column!") 
    elif (grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1] and grid[0][1] != '.'):
        return("Congratulations",grid[0][1]," you got three in the middle column!")
    elif (grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2] and grid[0][2] != '.'):
        return("Congratulations",grid[0][2]," you got three in the right column!") 
    
    elif (grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] != '.'):
        return("Congratulations",grid[0][0]," you got three in the top left diagonal!") 
    elif (grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0] and grid[0][2] != '.'):
        return("Congratulations",grid[0][2]," you got three in the bottom left diagonal!") 

    return "No Victor"


# In[7]:


#Mpresley 7/24/23 look for complete Grid


# In[19]:


def isGridComplete(grid):
    assert(len(grid) == 3 and len(grid[0]) == 3 and len(grid[1]) == 3 and len(grid[2]) == 3 )
    if (not '.' in grid[0] and not '.' in grid[1] and not '.' in grid[2]):
        return True
    else:
        return False


# In[9]:


#Mpresley 7/27/23 add function computer move. This computer will look for a win, defend an urgent loss or choose a random spot depending on the status of the board


# In[10]:


def ComputerMove(grid,comp_symbol):
    assert(comp_symbol == 'X' or comp_symbol == 'O')
    assert(len(grid) == 3 and len(grid[0]) == 3 and len(grid[1]) == 3 and len(grid[2]) == 3 )

    if (comp_symbol == 'X'):
        user_symbol = 'O'
    else:
        user_symbol = 'X'
    #Look for a row, column or diagnol that is only one letter away from computer victory
    if (grid[0].count('.') == 1 and grid[0].count(comp_symbol) == 2):
        grid[0] = [comp_symbol for g in grid[0]]
        print(lookForWin(grid))
        print("row hit 1 ")
        return
    elif(grid[1].count('.') == 1 and grid[1].count(comp_symbol) == 2):
        grid[1] = [comp_symbol for g in grid[1]]
        print(lookForWin(grid))
        print("row hit 2 ")
        return
    elif(grid[2].count('.') == 1 and grid[2].count(comp_symbol) == 2):
        grid[2] = [comp_symbol for g in grid[2]]
        print(lookForWin(grid))
        print("row hit 3 ")
        return
    
    #Look for victory in the columns 
    #First set columns
    col1 = [grid[0][0],grid[1][0],grid[2][0]]
    col2 = [grid[0][1],grid[1][1],grid[2][1]]
    col3 = [grid[0][2],Grid[1][2],grid[2][2]]
    
    #Go through all three columns to look for single gap
    if (col1.count('.') == 1 and col1.count(comp_symbol) == 2):
        grid[0][0] = comp_symbol ; grid[1][0] = comp_symbol ; grid[2][0] = comp_symbol 
        print(lookForWin(grid))
        print("col hit 1 ")
        return
    
    elif(col2.count('.') == 1 and col2.count(comp_symbol) == 2):
        grid[0][1] = comp_symbol ; grid[1][1] = comp_symbol ; grid[2][1] = comp_symbol 
        print(lookForWin(grid))
        print("col hit 2 ")
        return
    
    elif(col3.count('.') == 1 and col3.count(comp_symbol) == 2):
        grid[0][2] = comp_symbol ; grid[1][2] = comp_symbol ; grid[2][2] = comp_symbol 
        print(lookForWin(grid))
        print("col hit 3 ")
        return


    diag1 = [grid[0][0],grid[1][1],grid[2][2]]
    diag2 = [grid[0][2],grid[1][1],grid[2][0]]
    
    if(diag1.count('.') == 1 and diag1.count(comp_symbol) == 2):
        grid[0][0] = comp_symbol ; grid[1][1] = comp_symbol ; grid[2][2] = comp_symbol 
        print(lookForWin(grid))
        print("diag hit 1 ")
        return
    elif(diag2.count('.') == 1 and diag2.count(comp_symbol) == 2):
        grid[0][2] = comp_symbol ; grid[1][1] = comp_symbol ; grid[2][0] = comp_symbol 
        print(lookForWin(grid))
        print("diag hit 2 ")
        return
    
    
    
    
    #No Victory was not found in a single move, next the computer will go on defense to avoid obvious defeat
    if (grid[0].count('.') == 1 and grid[0].count(user_symbol) == 2):
        grid[0][grid[0].index('.')] = comp_symbol
        print("row def hit 1 ")
        return
    elif(grid[1].count('.') == 1 and grid[1].count(user_symbol) == 2):
        grid[1][grid[1].index('.')] = comp_symbol 
        print("row def hit 2 ")
        return
    elif(grid[2].count('.') == 1 and grid[2].count(user_symbol) == 2):
        grid[2][grid[2].index('.')] = comp_symbol  
        print("row def hit 3 ")
        return
        
    #look for columns
    elif (col1.count('.') == 1 and col1.count(user_symbol) == 2):
        grid[col1.index('.')][0] = comp_symbol
        print("col def hit 1 ")
        return
    elif (col2.count('.') == 1 and col2.count(user_symbol) == 2):
        grid[col2.index('.')][1] = comp_symbol
        print("col def hit 2 ")
        return
    elif (col3.count('.') == 1 and col3.count(user_symbol) == 2):
        grid[col3.index('.')][2] = comp_symbol
        print("col def hit 3 ")
        return
        
    #look for diagnos
    if(diag1.count('.') == 1 and diag1.count(user_symbol) == 2):
        idx = diag1.index('.')
        if(idx==0):
            grid[0][0] = comp_symbol
            print("diag def hit 1 ")
            return
        elif(idx==1):
            grid[1][1] = comp_symbol
            print("diag def hit 2 ")
            return
        elif(idx==2):
            grid[2][2] = comp_symbol
            print("diag def hit 3 ")
            return
    elif(diag2.count('.') == 1 and diag2.count(user_symbol) == 2):
        idx = diag2.index('.')
        if(idx==0):
            grid[0][2] = comp_symbol
            print("diag2 def hit 1 ")
            return
        elif(idx==1):
            grid[1][1] = comp_symbol
            print("diag2 def hit 2 ")
            return
        elif(idx==2):
            grid[2][0] = comp_symbol
            print("diag2 def hit 3 ")
            return
            
    
    #No obvious defense needed, now we'll place a random tick for the computer
    else:
        print("Set Random")
        setRandomTic(grid,comp_symbol)
    
#    else:
#        return 'No victory in first row or second row'


# In[12]:


def setRandomTic(grid,comp_symbol):
    i = 1
    dotCount = (Grid[0].count('.') + Grid[1].count('.') + Grid[2].count('.'))
    stopCount = random.randint(1,dotCount)


    row_idx = 0
    for g in grid[0]:
        if(i == stopCount and g == '.'):            
            grid[0][row_idx] = comp_symbol
            return
        elif(g == '.'):
            i += 1
        row_idx += 1
    
    row_idx = 0
    for g in Grid[1]:
        if(i == stopCount) and g == '.':
            grid[1][row_idx] = comp_symbol
            return
        elif(g == '.'):
            i += 1
        row_idx += 1

    row_idx = 0
    for g in Grid[2]:
        if(i == stopCount and g == '.'):
            grid[2][row_idx] = comp_symbol
            return
        elif(g == '.'):
            i += 1
        row_idx += 1


# In[15]:


def promptUserMove(grid,user_symbol,round):
    printGrid(grid,round)
    print("")
    print("Player's ",user_symbol," move")
    row_valid = False
    while row_valid == False:
        row = input('Please enter the Row number (Enter 0, 1 or 2):')
        if( row != '0' and row != '1' and row != '2'):
            print(row,"Error, you must enter 0, 1 and 2")
        else:
            row_valid = True
    
    col_valid = False
    while col_valid == False:
        col = input('Please enter the col number (Enter 0, 1 or 2):')
        if( col != '0' and col != '1' and col != '2'):
            print(col,"Error, you must enter 0, 1 and 2")
        else:
            col_valid = True
    print('row',row,'col',col)
    if(grid[int(row)][int(col)] == 'X' or grid[int(row)][int(col)] == 'O' ):
        print('Error, this position has already been filled',grid[int(row)][int(col)])
        print('')
        time.sleep(2)
        promptUserMove(Grid,user_symbol,1)
    else:
        grid[int(row)][int(col)] = user_symbol


# In[17]:


def chooseXorO():
    symbol = input('Please choose X or O:')
    symbol_valid = False
    while symbol_valid == False:
        if(symbol != 'X' and symbol != 'O'):
            print('Error, you must choose X or O')
            time.sleep(2)
            symbol = chooseXorO()
        else:
            symbold_valid = True
            return symbol


# In[20]:



user_symbol = chooseXorO()
# Set computer symbol (either X or O)
if user_symbol == "O":
    comp_user = "X"
elif user_symbol == "X":
    comp_user = "O"

# Initiate the round, grid and gridComplete
GridComplete = False
round = 1
col_list1 = [".", ".", "."]
col_list2 = [".", ".", "."]
col_list3 = [".", ".", "."]
Grid = [col_list1, col_list2, col_list3]

# Print first round
# printGrid(Grid,round)

# determine who moves first and initiate game
if comp_user == "X":
    print("")
    print("Since user choose O, computer will move first")
    time.sleep(1)
    ComputerMove(Grid, comp_user)
    round += 1
    print("Computer has made it's move, it's now your turn")
    promptUserMove(Grid, user_symbol, round)
    printGrid(Grid, round)
elif comp_user == "O":
    print("")
    print("Since user choose X, User will move first")
    time.sleep(1)
    promptUserMove(Grid, user_symbol, round)
    round += 1
    printGrid(Grid, round)

# Set while loop
while GridComplete == False:
    print("")
    time.sleep(1)
    print("Computer has registerd move")
    time.sleep(1)
    ComputerMove(Grid, comp_user)
    round += 1
    #    printGrid(Grid,round)
    time.sleep(1)
    lookForWin(Grid)
    result = lookForWin(Grid)
    if "Congratulations" in result:
        GridComplete = True
        printGrid(Grid, round)
        break
    elif isGridComplete(Grid) == True:
        print("Tie Game! :-/ ")
        GridComplete = True
        printGrid(Grid, round)
        break
    print("")
    time.sleep(1)
    promptUserMove(Grid, user_symbol, round)
    round += 1
    time.sleep(1)
    lookForWin(Grid)
    result = lookForWin(Grid)
    print("result", result)
    if "Congratulations" in result:
        GridComplete = True
        printGrid(Grid, round)
        break
    elif isGridComplete(Grid) == True:
        print("Tie Game! :-/ ")
        GridComplete = True
        printGrid(Grid, round)
        break

