import re
import chessboard
import moves
import numpy as np
import copy
import random
import torch as tr

class Node():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.score =  -10000
        self.count = 0

    def add_child(self, obj):
        self.children.append(obj)

class Minimax():
    count = 0
    def evaluation (board, playerColor):
        boardSize = np.shape(board)
        score = 0
        pawn = re.compile("pawn")
        rook = re.compile("rook")
        queen = re.compile("queen")
        king = re.compile("king")
        if(playerColor == "black"):
            pattern = "white+"
            color = "black+"
        else:
             pattern = "black+"
             color= "white+"
        for x in range(0,boardSize[0]):
            for y in range(0,boardSize[1]):
                if(re.match(color,board[x][y])):
                    if(pawn.search(board[x][y])):
                        score += 30
                    if(rook.search(board[x][y])):
                        score += 60
                    if(queen.search(board[x][y])):
                        score += 80
                    if(king.search(board[x][y])):
                        score += 1000
                if(re.match(pattern,board[x][y])):
                    if(pawn.search(board[x][y])):
                        score -= 30
                    if(rook.search(board[x][y])):
                        score -= 60
                    if(queen.search(board[x][y])):
                        score -= 80
                    if(king.search(board[x][y])):
                        score -= 1000
        return score/100
    
    #call minimax(root, 0, True, -99999,99999,"black"). Credit:geekforgeeeks pseudocode
    def minimax(node, depth,isMaxPlayer, alpha, beta, AIColor):
        if(len(node.children) == 0): 
            node.score = Minimax.evaluation(node.data, AIColor)
            return node
        if(isMaxPlayer):
            bestValue = -99999
            for i in node.children:
                value = Minimax.minimax(i, depth+1,False, alpha, beta ,AIColor).score
                bestValue = max(value, bestValue)
                alpha = max(alpha, bestValue)
                i.score = bestValue
                if(bestValue == value):
                   chosenNode = i
                if(beta < alpha):
                    break
            return chosenNode
        else:
            bestValue = 99999
            for i in node.children:
                value = Minimax.minimax(i, depth+1,True, alpha, beta ,AIColor).score
                bestValue = min(value, bestValue)
                beta = min(beta, bestValue)
                i.score = bestValue
                if(bestValue == value):
                    chosenNode = i
                if(beta < alpha):
                    break
            return chosenNode
    
    def humanpossibleSwape(board,current):
        possible_states = []
        boardCopy = copy.deepcopy(board)
        pattern = "white+"
        if(re.search(pattern,boardCopy[current[0]][current[1]]) ):
            color= "white+"
        else:
            color = "black+"
 
        boardSize = np.shape(boardCopy)
        #print("board size",boardSize)
        pieceA = boardCopy[current[0]][current[1]]
        for i in range(boardSize[0]):
            for j in range(boardSize[1]):
                if((i != current[0] or j != current[1]) and re.match(color,boardCopy[i][j]) and (boardCopy[i][j] != boardCopy[current[0]][current[1]]) and (boardCopy[i][j] != "black-king" and boardCopy[current[0]][current[1]] != "black-king") and (boardCopy[i][j] != "white-king" and boardCopy[current[1]][current[1]] != "white-king")):
                    possible_states.append((i,j))
        return possible_states

    def possibleSwape(board, player):
        possible_states = []
        boardCopy = copy.deepcopy(board)
        if(player == "b"):
            pattern = "white+"
            color = "black+"
        else:
             pattern = "black+"
             color= "white+"
 
        boardSize = np.shape(boardCopy)
        #print("board size",boardSize)
        for x in range(boardSize[0]):
            for y in range(boardSize[1]):
                pieceA = boardCopy[x][y]
                if(not re.match(color,pieceA)):
                    break
                for i in range(x,boardSize[0]):
                    for j in range(boardSize[1]):
                        if(not (i <= x and j <= y)):
                            if(re.match(color,boardCopy[i][j]) and (boardCopy[i][j] != boardCopy[x][y]) and (boardCopy[i][j] != "black-king" and boardCopy[x][y] != "black-king") and (boardCopy[i][j] != "white-king" and boardCopy[x][y] != "white-king")):
                                boardCopy2 = copy.deepcopy(board)
                                boardCopy2[i][j], boardCopy2[x][y] = boardCopy2[x][y], boardCopy2[i][j]
                                if(board != boardCopy2):
                                    possible_states.append(boardCopy2)
        return possible_states

    def possibleStates(board, player): 
        possible_states = []
        
        possible_moves = moves.Rules.moves(board, player)

        for current_position in possible_moves:
            new_positions = possible_moves[current_position]

            for new_position in new_positions:
                possible_states.append(moves.Rules.makeMove(board,current_position,new_position))

        return possible_states    

    def create_tree(self,board, player, depth = 3):

        if(player == 'b'):
            AIplayer = 'w'
        else:
            AIplayer = 'b'
        root = Node(board)
        states1 = Minimax.possibleSwape(board, AIplayer)
        states1 += Minimax.possibleStates(board, AIplayer)
        AIplayer,player  = player,AIplayer
        for j in states1:
            child = Node(j)
            root.add_child(child)
            if((depth-1) != 0):
                node = Minimax.create_tree(self,j, player, depth-1)
                for k in node.children:
                    child.add_child(k)

        return root

    def create_tree_with_node_count(self,board, player, depth = 3):

        node_count = 0
        if(player == 'b'):
            AIplayer = 'w'
        else:
            AIplayer = 'b'
        root = Node(board)
        states1 = Minimax.possibleSwape(board, AIplayer)
        states1 += Minimax.possibleStates(board, AIplayer)
        AIplayer,player  = player,AIplayer
        for j in states1:
            child = Node(j)
            root.add_child(child)
            node_count += 1
            if((depth-1) != 0):
                node = Minimax.create_tree(self,j, player, depth-1)
                for k in node.children:
                    child.add_child(k)
                    node_count += 1

        return root,node_count


    def displayChessboard(chessboard):
        print("|___________________________________________________________________________|")
        print("|                                                                           |")
        for i in range(np.shape(chessboard)[0]):
            for j in range(np.shape(chessboard)[1]):
                print("|"+chessboard[i][j]+"|", end=' ')
            print(end='\n')
            print("|___________________________________________________________________________|")
        print("|                                                                           |")
    
class Baseline_AI():
    def baseline_AI(board,AIplayer):
        states = Minimax.possibleStates(board, AIplayer)
        states += Minimax.possibleSwape(board, AIplayer)
        updated_board = random.choice(states)

        return updated_board

