# Charles Buyas cjb8qf


import random
print("Let's play Tic Tac Toe!\n")


def get_human():
    # Lets the player type which letter they want to be.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = (input("Do you want to be X or O?: ")).upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def draw_board(board):
    # "board" is a list of 10 strings representing the board
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def first_move():
    # Choose the player who goes first.
    move_letter = ''
    while not (move_letter == "P" or move_letter == "C"):
        move_letter = (str(input("Who goes first? (P or C): "))).upper()
    if move_letter == 'C':
        return "computer"
    else:
        return "player"


def empty_space(board, move):
    # Return true if the passed move is free on the board
    return board[move] == ' '


def get_human_move(board):
    # Let the player type in their move.
    move = ' '
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while move not in num_list or not empty_space(board, int(move)):
        move = int(input("What is your next move? (1-9): "))
    return move


def check_winner(board, letter):
    # this function returns true if there is a win
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or  # across the top
            (board[4] == letter and board[5] == letter and board[6] == letter) or  # across the middle
            (board[1] == letter and board[2] == letter and board[3] == letter) or  # across the bottom
            (board[7] == letter and board[4] == letter and board[1] == letter) or  # down the left side
            (board[8] == letter and board[5] == letter and board[2] == letter) or  # down the middle
            (board[9] == letter and board[6] == letter and board[3] == letter) or  # down the right side
            (board[7] == letter and board[5] == letter and board[3] == letter) or  # diagonal
            (board[9] == letter and board[5] == letter and board[1] == letter))  # diagonal


def get_board_copy(board):
    # makes a duplicate of the board list
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def move_list(board, moves):
    possible_moves = []
    for i in moves:
        if empty_space(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def existing_move(board, letter, move):
    board[move] = letter


def computer_move(board, computer_letter):
    # based on the current board, this determines the computer's move
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'
    # checks if can win in the next move
    for i in range(1, 10):
        copy = get_board_copy(board)
        if empty_space(copy, i):
            existing_move(copy, computer_letter, i)
            if check_winner(copy, computer_letter):
                return i
    # Checks if player could win on next move and blocks the player
    for i in range(1, 10):
        copy = get_board_copy(board)
        if empty_space(copy, i):
            existing_move(copy, player_letter, i)
            if check_winner(copy, player_letter):
                return i
    # Plays in the center if the player started in the corner
    player_start = move_list(board, [1, 3, 7, 9])
    if player_start == True:
        if empty_space(board, 5):
            return 5
    # Try to take one of the corners, if they are free.
    move = move_list(board, [1, 3, 7, 9])
    if move != None:
        return move
    # Try to take the center, if it is free.
    if empty_space(board, 5):
        return 5
    # Move on one of the sides.
    return move_list(board, [2, 4, 6, 8])


def full_board(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if empty_space(board, i):
            return False
    return True

game_is_playing = True

if game_is_playing:
    # Reset the board
    new_board = [' '] * 10
    player_letter, computer_letter = get_human()
    turn = first_move()
    print('The ' + turn + ' will go first.')

    while game_is_playing:
        if turn == "player":
            # player’s turn
            draw_board(new_board)
            move = get_human_move(new_board)
            existing_move(new_board, player_letter, move)

            if check_winner(new_board, player_letter):
                draw_board(new_board)
                print('Hooray! You have won the game!')
                game_is_playing = False
            else:
                if full_board(new_board):
                    draw_board(new_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            # computer’s turn
            move = computer_move(new_board, computer_letter)
            existing_move(new_board, computer_letter, move)

            if check_winner(new_board, computer_letter):
                draw_board(new_board)
                print('The computer has beaten you! You lose.')
                game_is_playing = False
            else:
                if full_board(new_board):
                    draw_board(new_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = "player"
