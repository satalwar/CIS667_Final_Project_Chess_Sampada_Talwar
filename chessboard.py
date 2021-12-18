#from chessPieces import Rook
import numpy as np
import re

class Chess():

    def __init__(self,size):

        #chessboard
        self.chessboard = [["    __    "] * size for i in range (size)]

        if(size == 4):
            self.chessboard[0][0] = 'black_rook'
            self.chessboard[0][1] = 'black-king'
            self.chessboard[0][2] = 'blackqueen'
            self.chessboard[0][3] = 'black_rook'

            self.chessboard[3][0] = 'white_rook'
            self.chessboard[3][1] = 'white-king'
            self.chessboard[3][2] = 'whitequeen'
            self.chessboard[3][3] = 'white_rook'

        elif(size == 5):
            
            for i in range(5):
                self.chessboard[1][i] = 'black_pawn'
                self.chessboard[3][i] = 'white_pawn'
                self.chessboard[0][i] = 'black_rook'
                self.chessboard[4][i] = 'white_rook'

            self.chessboard[0][2] =  'black-king'
            self.chessboard[4][2] =  'white-king'


        
        elif(size == 6):
            #pawns
            for i in range(6):
                self.chessboard[1][i] = 'black_pawn'
                self.chessboard[4][i] = 'white_pawn'
            #self.chessboard[1][2] = "    __    "
            #rooks
            self.chessboard[0][0] = 'black_rook'
            self.chessboard[0][1] = 'black_rook'
            self.chessboard[0][4] = 'black_rook'
            self.chessboard[0][5] = 'black_rook'

            self.chessboard[5][0] = 'white_rook'
            self.chessboard[5][1] = 'white_rook'
            self.chessboard[5][4] = 'white_rook'
            self.chessboard[5][5] = 'white_rook'

            #king
            self.chessboard[0][2] = 'black-king'
            self.chessboard[5][2] = 'white-king'

            #queen
            self.chessboard[0][3] = 'blackqueen'
            self.chessboard[5][3] = 'whitequeen'


        elif(size == 7):
            
            for i in range(7):
                self.chessboard[1][i] = 'black_pawn'
                self.chessboard[5][i] = 'white_pawn'
                self.chessboard[0][i] = 'black_rook'
                self.chessboard[6][i] = 'white_rook'

            self.chessboard[0][3] =  'black-king'
            self.chessboard[6][3] =  'white-king'

        
        elif(size == 8):

            for i in range(8):
                self.chessboard[1][i] = 'black_pawn'
                self.chessboard[6][i] = 'white_pawn'

            self.chessboard[0][0] = 'black_rook'
            self.chessboard[0][1] = 'black_rook'
            self.chessboard[0][2] = 'black_rook'
            self.chessboard[0][5] = 'black_rook'
            self.chessboard[0][6] = 'black_rook'   
            self.chessboard[0][7] = 'black_rook'   

            self.chessboard[7][0] = 'white_rook'
            self.chessboard[7][1] = 'white_rook'
            self.chessboard[7][2] = 'white_rook'
            self.chessboard[7][5] = 'white_rook'
            self.chessboard[7][6] = 'white_rook'   
            self.chessboard[7][7] = 'white_rook' 

            #king
            self.chessboard[0][3] = 'black-king'
            self.chessboard[7][3] = 'white-king'

            #queen
            self.chessboard[0][4] = 'blackqueen'
            self.chessboard[7][4] = 'whitequeen'


        
        #self.current_player = "b"
        self.winner = "none"

    def is_game_over(game):

        size = len(game.chessboard)
        is_game_over = False
        count = 0
        kings = []
        for i in range (size):
            for j in range(size):
                if "king" in game.chessboard[i][j]:
                    count += 1
                    kings.append(game.chessboard[i][j])

        if count == 1:
            is_game_over = True
            if "white" in  kings[0]:
                game.winner = "White"

            else:
                game.winner = "Black"


        return is_game_over  

    def get_score(board):

        black_player_score = 0
        white_player_score = 0

        boardSize = np.shape(board)
        score = 0
        pawn = re.compile("pawn")
        rook = re.compile("rook")
        queen = re.compile("queen")
        king = re.compile("king")

        color1 = "black+"
        color2 = "white+"

        for x in range(0,boardSize[0]):
            for y in range(0,boardSize[1]):
                if(re.match(color1,board[x][y])):
                    if(pawn.search(board[x][y])):
                        black_player_score += 30
                    if(rook.search(board[x][y])):
                        black_player_score += 60
                    if(queen.search(board[x][y])):
                        black_player_score += 80
                    if(king.search(board[x][y])):
                        black_player_score += 1000
                if(re.match(color2,board[x][y])):
                    if(pawn.search(board[x][y])):
                        white_player_score += 30
                    if(rook.search(board[x][y])):
                        white_player_score += 60
                    if(queen.search(board[x][y])):
                        white_player_score += 80
                    if(king.search(board[x][y])):
                        white_player_score += 1000

        return black_player_score,white_player_score
    

    def is_tied(chessboard):
        return False

    def winner(chessboard):
        winner = ""

        return winner


    def displayChessboard(self):
        #print(self.chessboard)
        size = len(self.chessboard)

        if(size == 4):
            print("|_________________________________________________|")
            print("|                                                 |")
            for i in range(size):
                for j in range(size):
                    print("|"+self.chessboard[i][j]+"|", end=' ')
                print(end='\n')
                print("|_________________________________________________|")
            print("|                                                 |")

        elif(size == 5):
            print("|______________________________________________________________|")
            print("|                                                              |")
            for i in range(size):
                for j in range(size):
                    print("|"+self.chessboard[i][j]+"|", end=' ')
                print(end='\n')
                print("|______________________________________________________________|")
            print("|                                                              |")

        elif(size == 6):
            print("|___________________________________________________________________________|")
            print("|                                                                           |")
            for i in range(size):
                for j in range(size):
                    print("|"+self.chessboard[i][j]+"|", end=' ')
                print(end='\n')
                print("|___________________________________________________________________________|")
            print("|                                                                           |")

        elif(size == 7):
            print("|________________________________________________________________________________________|")
            print("|                                                                                        |")
            for i in range(size):
                for j in range(size):
                    print("|"+self.chessboard[i][j]+"|", end=' ')
                print(end='\n')
                print("|________________________________________________________________________________________|")
            print("|                                                                                        |")

        elif(size == 8):
            print("|_____________________________________________________________________________________________________|")
            print("|                                                                                                     |")
            for i in range(size):
                for j in range(size):
                    print("|"+self.chessboard[i][j]+"|", end=' ')
                print(end='\n')
                print("|_____________________________________________________________________________________________________|")
            print("|                                                                                                     |")

