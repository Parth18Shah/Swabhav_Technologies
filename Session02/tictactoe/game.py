def game_logic(game_board):

    for column_value in range (0, 3) :        
        row_value = column_value * 3
        if (game_board[row_value] == game_board[(row_value + 1)] and game_board[row_value] == game_board[(row_value + 2)]) :
            return 1

        if (game_board[column_value] == game_board[(column_value + 3)] and game_board[column_value] == game_board[(column_value + 6)]) :
            return 1
        
    if game_board[0] != '1' and game_board[1] != '2' and game_board[2] != '3' and \
        game_board[3] != '4' and game_board[4] != '5' and game_board[5] != '6' and game_board[6] \
        != '7' and game_board[7] != '8' and game_board[8] != '9':
        return 2

    if((game_board[0] == game_board[4] and game_board[0] == game_board[8]) or (game_board[2] == game_board[4] and game_board[4] == game_board[6])) :
        return 1

    return 0