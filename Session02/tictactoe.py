game_board = []

for cell_number in range (0, 9) :

    game_board.append(str(cell_number + 1))

player_turn = True
winner = False
draw = False

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

while not winner and not draw:
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

    for column_value in range (0, 3) :        
        row_value = column_value * 3
        if (game_board[row_value] == game_board[(row_value + 1)] and game_board[row_value] == game_board[(row_value + 2)]) :
            winner = True
            print_board()
            print ("Player " + str(int(player_turn + 1)) + " wins!\n")

        if (game_board[column_value] == game_board[(column_value + 3)] and game_board[column_value] == game_board[(column_value + 6)]) :
            winner = True
            print_board()
            print ("Player " + str(int(player_turn + 1)) + " wins!\n")
        
    if game_board[0] != '1' and game_board[1] != '2' and game_board[2] != '3' and \
        game_board[3] != '4' and game_board[4] != '5' and game_board[5] != '6' and game_board[6] \
        != '7' and game_board[7] != '8' and game_board[8] != '9':
        draw = True
        print_board()
        print('GAME IS OVER AND ITS A DRAW')

    if((game_board[0] == game_board[4] and game_board[0] == game_board[8]) or (game_board[2] == game_board[4] and game_board[4] == game_board[6])) :
        winner = True
        print_board()
        print ("Player " + str(int(player_turn + 1)) + " wins!\n")