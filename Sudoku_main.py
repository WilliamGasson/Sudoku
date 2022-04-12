"""
driver file :  handles user inputs, displays board
needs to be replaced if an online version - engine the same
"""

"""
imports
"""
import pygame as p
import Sudoku_engine
import Sudoku_img_rec

"""
constants
"""
WIDTH = HEIGHT = 729 # could go 400
DIMENSION = 9 # dimension of Sudoku board are 9 by 9
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animation
IMAGES = {}


def getBoard():
    id = Sudoku_img_rec.image_identifier()
    id.loadImg("img\Sudoku2.png")
    id.findBoxes()
    board = id.idNumbers()
    return board

'''
Draw the current state
'''
def drawGameSate(screen, gs):
    p.display.set_caption('Sudoku')

    # Set the colours of the board
    colours = [p.Color("white"), p.Color("gray")]
    font = p.font.Font('freesansbold.ttf', 72)
    white = (255, 255, 255)
    black = (0, 0, 0)

    #print(p.font.get_fonts())
    # Loop through the squares
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            # draw squares
            colour=colours[((r+c)%2)]
            p.draw.rect(screen, colour, p.Rect(c*SQ_SIZE,r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

            # draw numbers
            number = gs.board[r][c]
            if number != 0:
                text = font.render(" {}".format(number),False, black)
                screen.blit(text, p.Rect(c*SQ_SIZE,r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    for i in range(1,4):
        p.draw.line(screen,p.Color("black"),start_pos=[i*WIDTH/3,0], end_pos=[i*WIDTH/3,WIDTH])
        p.draw.line(screen,p.Color("black"),start_pos=[0,i*WIDTH/3], end_pos=[WIDTH,i*WIDTH/3])

            
'''
Main driver, user inputs and graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()

    board = getBoard()

    gs = Sudoku_engine.GameState(board)
    sqSelected = () # keep track of last click - tuple

    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running =False

            # tracking mouse
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # x,y location of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                sqSelected= (row, col)

                
            # tracking keyboard
            if e.type == p.KEYDOWN:
                # numbers that fit
                if e.key == p.K_h:
                    print("Hint")
                    if sqSelected != ():
                        validNumber = gs.getValidNumber(row,col) # get a list of possible moves
                        print(validNumber)
                # Solve
                if e.key == p.K_s:
                    print("Solve")
                    gs.solve()                   

                # Undo move
                if e.key == p.K_z:
                    print("Move undone")
                    gs.undoNumber()
                # clear the box
                elif e.key == p.K_0:
                    number = 0
                    gs.insertNumber(sqSelected, number)

                # Enter moves
                elif e.key == p.K_1:
                    number = 1
                    gs.insertNumber(sqSelected, number)
                elif e.key == p.K_2:
                    number = 2
                    gs.insertNumber(sqSelected, number)
                elif e.key == p.K_3:
                    number = 3
                    gs.insertNumber(sqSelected, number)
                elif e.key == p.K_4:
                    number = 4
                    gs.insertNumber(sqSelected, number)
                elif e.key == p.K_5:
                    number = 5
                    gs.insertNumber(sqSelected, number)
                elif e.key == p.K_6:
                    number = 6
                    gs.insertNumber(sqSelected, number)
                elif e.key == p.K_7:
                    number = 7
                    gs.insertNumber(sqSelected, number)
                elif e.key == p.K_8:
                    number = 8
                    gs.insertNumber(sqSelected, number)
                elif e.key == p.K_9:
                    number = 9
                    gs.insertNumber(sqSelected, number)
                
                #if number in validNumber:
                sqSelected = () # deselect



        drawGameSate(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


if __name__=="__main__":
    main()