from Processing import *
from random import *
window(700,700)
grid=[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
def draw():
    rowNumber=0
    for row in grid:
        colNumber=0
        for col in row:
            if col==0:
                fill(255,255,0)
                rect(rowNumber*140,colNumber*140,140,140)
            else:
                fill(255,255,255)
                rect(rowNumber*140,colNumber*140,140,140)
            colNumber+=1
        rowNumber+=1
draw()
idx1 = randrange(0,len(grid[0]))
idx2 = randrange(0,len(grid[0]))
grid[idx1][idx2] = 0
turns=0
guessX=int(input("Enter the row number:"))
guessY=int(input("Enter the column number:"))
guess=grid[guessX][guessY]
while guess!=grid[idx1][idx2] or turns>=5:    
    guessX=int(input("Enter the row number:"))
    guessY=int(input("Enter the column number:"))
    guess=grid[guessX][guessY]       
    if guess== 0:
        print("You win!!!")
        delay (1000)
        break
    elif guess==1 :       
        grid[guessX][guessY]= 2
        def draw():
            rowNumber=0
            for row in grid:
                colNumber=0
                for col in row:
                    if col==2:
                        fill(255,0,0)
                        rect(rowNumber*140,colNumber*140,140,140)
                    elif col==1:
                        pass
                    else:
                        fill(255,255,255)
                        rect(rowNumber*140,colNumber*140,140,140)
                    colNumber+=1
                rowNumber+=1
        draw()
        turns+=1
        print("Try again")
    elif turns>=5:
        print("You have failed!")
        delay(1000)
        break
