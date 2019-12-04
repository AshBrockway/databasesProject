#thankfully the server that this data is from
#already comes assuming correct chess logic.
#this means we dont need to look for checks in a position, or other nastiness
#we just need to know how pieces move..


#the following class defines a board, which contains a 2d array of squares
#that contain pieces.  Each piece is given by a string (e.g. a white knight is
# 'WN')  Some of the logic here is from the other codebase, and irrelevant except
#for saving me time removing redundant code in this project
class Board:

    def __init__(self, boardState = None):

        if boardState == None:
            #initializing empty board
            self.board = [[0 for i in range(8)] for j in range(8)]
            
            #initializing pawns
            for i in range(8):
                self.board[i][1] = 'BP'
                self.board[i][6] = 'WP'
            #initializing rooks
            self.board[0][0] = 'BR'
            self.board[7][0] = 'BR'
            self.board[0][7] = 'WR'
            self.board[7][7] = 'WR'
            #initializing bishops
            self.board[2][0] = 'BB'
            self.board[5][0] = 'BB'
            self.board[2][7] = 'WB'
            self.board[5][7] = 'WB'
            #initializing knights
            self.board[1][0] = 'BN'
            self.board[6][0] = 'BN'
            self.board[1][7] = 'WN'
            self.board[6][7] = 'WN'
            #initializing kings and queens
            self.board[3][7] = 'WQ'
            self.board[4][7] = 'WK'
            self.board[4][0] = 'BK'
            self.board[3][0] = 'BQ'

            self.prevBoard = self.board
            #previous board states for
            #Castling helper variables, with coordinates

            #black king
            self.castlingRights = {
                'BK': True,
                'WK': True,
                'R00': True,
                'R70': True,
                'R07': True,
                'R77': True
            }

            self.kingPos = {
                'WK': (4,7),
                'BK': (4,0)
            }
            
        else:
            self.board = boardState[0]
            self.castlingRights = boardState[1]
            self.kingPos = boardState[2]
            
        self.statesStack = []

        #allows us to easily reset the board at a later point
        def setBoard(self, inBoard, inPrev):
            self.board = inBoard
            self.prevBoard = inPrev

    #SETTING UP PIECE DYNAMICS
    #the syntax is a bit messy, but basically the functions take in a piece at a 
    #given position (x,y), a target amount of squares to move (dx, dy),
    #the current color of the piece to move (myColor) and the opponent (otherColor).
    #targetValue and tester are not nessecary for this project, but I dont want to
    #screw up code somewhere else
    #the function either returns that the move is valid (true), or that it is not (false)
    def pawnMove(self, x, y, dx, dy, myColor, otherColor, targetValue, tester):
        forward = {'W':1, 'B':-1}[myColor]
        try:
            #checking en passant condition
            try:
                if int(targetValue) == 0:
                    if self.board[dx][y] == otherColor + 'P':
                        if self.prevBoard[dx][dy - forward] == otherColor + 'P':
                            if self.board[dx][dy - forward] == 0:
                                if self.prevBoard[dx][dy] == 0:
                                    return (True, 'P')
            except:
                dummy = None
                    
            #capture condition
            if targetValue[0] == otherColor:
                if forward*(y-dy) == 1 and abs(x-dx) == 1:
                    return True
                else:
                    return False
            #normal pawn move
            elif forward*(y-dy) == 1 and (x - dx) == 0:
                return True
            #double pawn advance from start squares
            elif forward*(y-dy) == 2 and (x - dx == 0) and self.board[x][y + -forward] == 0 and (y == 1 or y == 6):
                return True
        except Exception as e:
            print(e)
            return False

    def knightMove(self, x, y, dx, dy, myColor, otherColor, targetValue, tester):
        try:
            #we have eight conditions to deal with
            if (((x - dx) == 1 and abs(y - dy) == 2) or ((x - dx) == 2 and abs(y - dy) == 1)) or (((x - dx) == -1 and abs(y - dy) == 2) or ((x - dx) == -2 and abs(y - dy) == 1)):
                return True
            else:
                return False
        except:
            return False

    def rookMove(self, x, y, dx, dy, myColor, otherColor, targetValue, tester):
        if (x - dx) != 0 and (y-dy) != 0:
            return False
        
        if (x-dx) == 0:
            #no x movement
            yDir = int((dy - y)/abs(dy-y))
            xDir = 0
            posi = [x,y]
            for i in range(abs(y-dy)-1):
                test = self.board[posi[0]][posi[1]+yDir]
                if test != 0:
                    return False
                posi[1] += yDir
            if tester == False:
                self.castlingRights['R' + str(x) + str(y)] = False
            return True
                
        elif (y-dy) == 0:
            #no y movement
            xDir = int((dx-x)/abs(dx-x))
            yDir = 0
            posi = [x,y]
            for i in range(abs(x-dx)-1):
                test = self.board[posi[0] + xDir][posi[1]]
                if test != 0:
                    return False
                posi[0] += xDir
            if tester == False:
                self.castlingRights['R' + str(x) + str(y)] = False
            return True      

    def bishopMove(self, x, y, dx, dy, myColor, otherColor, targetValue, tester):
        if abs(x-dx) != abs(y-dy):
            return False
        
        xDir = int((dx - x)/abs(dx - x))
        yDir = int((dy - y)/abs(dy - y))
        posi = [x, y]
        if abs(x-dx) == 1:
            return True
        for i in range(abs(x-dx)-1):
            test = self.board[posi[0]+xDir][posi[1]+yDir]
            if test != 0:
                return False
            posi[0] += xDir
            posi[1] += yDir
        return True

    #kingMove has alot of redundant code from the other project.  We test for alot
    #of edge cases that we dont need to check for here.
    def kingMove(self, x, y, dx, dy, myColor, otherColor, targetValue, tester):
        if (x == dx) and (y == dy):
            return False
        
        if targetValue != myColor + 'R':
            if targetValue[0] == myColor:
                return False
            
            if math.sqrt((x-dx)**2 + (y-dy)**2) < 2:
                if (self.bishopMove(x, y, dx, dy, myColor, otherColor, targetValue, tester) == True) or (self.rookMove(x, y, dx, dy, myColor, otherColor, targetValue, tester) == True):
                    #if self.squareControlCheck(otherColor, myColor, (dx,dy)) == False:
                        if tester == False:
                            self.castlingRights[myColor + 'K'] = False
                            self.kingPos[myColor + 'K'] = (dx, dy)
                        return True
                return False
            return False
        
        #checking for castling rights for king and rook
        elif targetValue == myColor + 'R' and self.castlingRights[myColor + 'K']:
            if (dx == 0 or dx == 7) and (dy == 0 or dy == 7) and self.castlingRights['R' + str(dx) + str(dy)]:
                #opponentControlledSquares = self.squareControlCheck(myColor, otherColor)
                direction = int((dx - x)/abs(dx - x))
                posi = [x,y]
                for i in range(abs(x-dx) - 1):
                    test = self.board[posi[0]+direction][posi[1]]
                    #self.squareControlCheck(player, otherPlayer, squareToCheck, pieceSquares = None)
                    controlTest = self.squareControlCheck(otherColor, myColor, (posi[0] + direction, posi[1]))[0]
                    if test != 0 or controlTest:
                        return False
                    posi[0] += direction 
                return (True, 'K')
            
            return False
        return False     