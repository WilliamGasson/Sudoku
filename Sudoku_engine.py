""" 
stores state data for the game, calcuates valid moves and move log
"""

from select import select


class GameState():


    def __init__(self, board = None):
        #board is an 9x9 2d list for each box, - is empty
        DefaultBoard=[
            [4,0,0,  0,0,0,  0,0,2],
            [1,6,2,  7,0,4,  5,0,8],
            [0,0,8,  0,1,9,  7,6,0],
            
            [2,5,0,  0,0,7,  6,0,0],
            [0,0,7,  3,0,0,  9,1,0],
            [9,1,0,  5,0,0,  4,2,0],
            
            [0,0,5,  0,0,0,  0,0,0],
            [7,0,6,  0,5,1,  0,0,0],
            [8,9,0,  0,0,3,  2,0,6]]
        
        self.board = board if board is not None else DefaultBoard
        self.moveLog = []

    '''
    Executes normal moves
    '''
    def insertNumber(self, square, number):
        if square == ():
            pass
        else:
            print(square)
            self.board[square[0]][square[1]] = number
            self.moveLog.append(square) # log move
            print(self.moveLog)

    '''
    Undoes moves
    '''
    def undoNumber(self):
        if len(self.moveLog)!=0: # not the first move
            square = self.moveLog.pop()
            self.board[square[0]][square[1]] = 0 # set box back to empty

    """
    Which box each square is in
    """

    def findBox(self, r, c):
        box = [0,0]
        if r <=2:
            box[0] = 0
        if r >= 3 and r <= 5:
            box[0] = 1
        if r >= 6:
            box[0] = 2
        if c <= 2:
            box[1] = 0
        if c >= 3 and c <= 5:
            box[1] = 1
        if c >= 6:
            box[1] = 2
        return box
    
    """
    Checking move is legal
    """

    def getValidNumber(self, r, c):
        # generate possible numbers
        numbers = [1,2,3,4,5,6,7,8,9]
        # make the moves
        for number in range(len(numbers),0,-1): # loop from end of list to start
            for i in range(9):
                # numbers checks
                if number == self.board[r][i]:
                    if number in numbers:
                        numbers.remove(number)  
                if number == self.board[i][c]:
                    if number in numbers:
                        numbers.remove(number)  

                boxId = self.findBox(r,c)
                box = [3*boxId[0]+int(i/3), 3*boxId[1]+int(i%3)]
                if number == self.board[box[0]][box[1]]:
                    if number in numbers:                   
                        numbers.remove(number)  

        return numbers

    
    """
    Finding a solution
    """
    def solve(self):

        completedSq = 0

        for r in range(9):
            for c in range(9):
                if self.board[r][c] != 0:
                    completedSq += 1

        while completedSq <81:
            for r in range(9):
                for c in range(9):
                    print(r,c)
                    if self.board[r][c] == 0:
                        validNumbers = self.getValidNumber(r,c)
                        print(r,c,validNumbers)

                        if len(validNumbers) == 1:
                            print(r,c,validNumbers[0])

                            self.insertNumber([r,c],validNumbers[0])
                            completedSq += 1
        
        print("solved")








