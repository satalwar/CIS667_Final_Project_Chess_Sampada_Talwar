from numpy import select
import chessboard
import moves
import MiniMax
import matplotlib.pyplot as pt

def get_user_action():
    
    current = input("Enter which piece you want to move ")
    c = tuple(map(int, current.split(',')))
    possibleMoves = moves.Rules.possible_moves_of_piece(c,game.chessboard)
    print("Possible Moves:")
    print(possibleMoves)
    humanpossibleSwape = MiniMax.Minimax.humanpossibleSwape(game.chessboard,c)
    print("Possible Swapes:")
    print(humanpossibleSwape)
    new = input("Enter target position")

    c = tuple(map(int, current.split(',')))
    n = tuple(map(int, new.split(',')))
    return c,n

def experiment(size):
    game = chessboard.Chess(size)
    black_player_scores = []
    white_player_scores = []
    node_counts = []

    for i in range(100):
        count = 0
        game = chessboard.Chess(size)
        print("Game ",i)
        while not chessboard.Chess.is_game_over(game):
            player1 = "w"
            player2 = "b"
            print("AI 1's Turn")
            game.chessboard = MiniMax.Baseline_AI.baseline_AI(game.chessboard,"b")
            game.displayChessboard()  

            if chessboard.Chess.is_game_over(game):
                black_player_score,white_player_score = chessboard.Chess.get_score(game.chessboard)
                black_player_scores.append(black_player_score)
                white_player_scores.append(white_player_score)
                print(black_player_score)
                print(white_player_score)
                break

            print("AI 2's Turn")   
            root,node_count = MiniMax.Minimax.create_tree_with_node_count(game, game.chessboard, player2)
            game.chessboard = MiniMax.Minimax.minimax(root, 0, True, -99999,99999,"white").data
            count += node_count
            game.displayChessboard() 

            if chessboard.Chess.is_game_over(game):
                black_player_score,white_player_score = chessboard.Chess.get_score(game.chessboard)
                black_player_scores.append(black_player_score)
                white_player_scores.append(white_player_score)
                print(black_player_score)
                print(white_player_score)

        node_counts.append(count)        

    
    print(white_player_scores)
    print(black_player_scores)
    pt.hist(white_player_scores,bins=3,rwidth=0.95)
    pt.show()
    pt.hist(black_player_scores,bins=3,rwidth=0.95)
    pt.show()
    
    print(node_counts)
    pt.hist(node_counts,bins=3,rwidth=0.95)
    pt.show()

if __name__ == '__main__':

    print("Select from the following board sizes")
    print("1. 4x4")
    print("2. 5x5")
    print("3. 6x6")
    print("4. 7x7")
    print("5. 8x8")

    choice = int(input("Enter your choice"))
    size = 0
    if(choice == 1):
        size = 4
    elif(choice == 2):
        size = 5
    elif(choice == 3):
        size = 6    
    elif(choice == 4):
        size = 7    
    elif(choice == 5):
        size = 8           

    game = chessboard.Chess(size)


    print("Select mode of each player:")
    print("1. Player 1 - Human Controlled   Player 2 - Human Controlled")
    print("2. Player 1 - AI Controlled   Player 2 - Human Controlled")
    print("3. Player 1 - AI Controlled   Player 2 - AI Controlled")

    mode = int(input("Enter your choice "))

    player = "w"
    AI_player = "b"
    #print(MiniMax.Minimax.possibleStates(game.chessboard, player))
    state = game.chessboard,player
    
    print("Starting game. Here is the board")
    game.displayChessboard() 

    if(mode == 1):
        player1 = "black"
        player2 = "white"
        while not chessboard.Chess.is_game_over(game):
            print("Player 1's Turn")
            current,new = get_user_action()

            if new in moves.Rules.possible_moves_of_player(current,game.chessboard,player1):
                game.chessboard = moves.Rules.makeMove(game.chessboard, current, new)
                game.displayChessboard()
            else:
            
                while new not in moves.Rules.possible_moves_of_player(current,game.chessboard,player1):
                    print("invalid move") 
                    current,new = get_user_action()

                game.chessboard = moves.Rules.makeMove(game.chessboard, current, new)
                game.displayChessboard()


            print("Player 2's Turn")
            current,new = get_user_action()

            if new in moves.Rules.possible_moves_of_player(current,game.chessboard,player2):
                game.chessboard = moves.Rules.makeMove(game.chessboard, current, new)
                game.displayChessboard()
            
            else:
                while new not in moves.Rules.possible_moves_of_player(current,game.chessboard,player2):
                    print("invalid move") 
                    current,new = get_user_action()

                game.chessboard = moves.Rules.makeMove(game.chessboard, current, new)
                game.displayChessboard()                    


    elif(mode == 2):
        while not chessboard.Chess.is_game_over(game):
 
            print("AI's Turn")
            root = MiniMax.Minimax.create_tree(game, game.chessboard, player)
            game.chessboard = MiniMax.Minimax.minimax(root, 0, True, -99999,99999,"black").data
            game.displayChessboard()  

            if chessboard.Chess.is_game_over(game):
                break 
 
            print("Player's Turn")
            current,new = get_user_action()

            if new in moves.Rules.possible_moves_of_piece(current,game.chessboard):
                game.chessboard = moves.Rules.makeMove(game.chessboard, current, new)
                game.displayChessboard()
            else:

                while new not in moves.Rules.possible_moves_of_piece(current,game.chessboard):
                    print("invalid move") 
                    current,new = get_user_action()

                game.chessboard = moves.Rules.makeMove(game.chessboard, current, new)
                game.displayChessboard()    


    elif(mode == 3):
        while not chessboard.Chess.is_game_over(game):
            player1 = "w"
            player2 = "b"
            print("AI 1's Turn")
            #root = MiniMax.Minimax.create_tree(game, game.chessboard, player1)
            game.chessboard = MiniMax.Baseline_AI.baseline_AI(game.chessboard,"b")
            game.displayChessboard()  

            if chessboard.Chess.is_game_over(game):
                black_player_score,white_player_score = chessboard.Chess.get_score(game.chessboard)
                break
            
            print("AI 2's Turn")   
            root = MiniMax.Minimax.create_tree(game, game.chessboard, player2)
            game.chessboard = MiniMax.Minimax.minimax(root, 0, True, -99999,99999,"white").data
            game.displayChessboard() 

            if chessboard.Chess.is_game_over(game):
                black_player_score,white_player_score = chessboard.Chess.get_score(game.chessboard)

    if(black_player_score and white_player_score):
        print("Score of Player 1 - ",black_player_score)
        print("Score of Player 2 - ",white_player_score)
    if game.winner != "none":
        print("Winner of the game is ",game.winner)    
