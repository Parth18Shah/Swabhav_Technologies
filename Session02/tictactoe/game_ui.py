import game as g

game_board = []

for cell_number in range (0, 9) :

    game_board.append(str(cell_number + 1))

def print_board() :
    print("\n\n\tTic Tac Toe\n\n")
    print("Player 1 (X)  -  Player 2 (O)\n\n\n")
    print("     |     |     \n")
    print("  {}  |  {}  |  {} \n".format( game_board[0], game_board[1], game_board[2]))
    print("_____|_____|_____\n")
    print("     |     |     \n")
    print("  {}  |  {}  |  {} \n".format( game_board[3], game_board[4], game_board[5]))
    print("_____|_____|_____\n")
    print("     |     |     \n")
    print("  {}  |  {}  |  {} \n".format( game_board[6], game_board[7], game_board[8]))
    print("     |     |     \n\n")

player_turn = True

while True:
    print_board()
    if player_turn :
        print( "Player 1:")

    else :
        print( "Player 2:")
    choice = int(input(">> "))

    if(game_board[choice - 1] == 'X' or game_board [choice-1] == 'O'):
        print("\nIllegal move, please try again\n")
        continue

    if (player_turn):
        game_board[choice - 1] = 'X'

    else :
        game_board[choice - 1] = 'O'

    player_turn = not player_turn

    turn_result = g.game_logic(game_board)

    if(turn_result==1):
        print_board()
        print ("Player " + str(int(player_turn + 1)) + " wins!\n")
        break

    if(turn_result==2):
        print_board()
        print('GAME IS OVER AND ITS A DRAW')
        break