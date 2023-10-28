import random

finished = False
board_data = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]


#  __functions__
def print_start_menu():
    print("Hello! \nIn this game you are playing a tic-tac-toe game with computer.\
    \nRules are simple: \n- game board is 3x3; \n- you can draw X or O in an empty field;\
    \n- Whoever gets three X or O in the row (vertical, horizontal or diagonally) wins\
    \nGood Luck!")
    player_symbol = int(input("Choose 0 if you want to play with O or choose 1 if you want to play with X: "))
    print("________________________________________________________________________________________")
    if player_symbol == 0:
        computer_symbol = 1
    else:
        computer_symbol = 0
    return player_symbol, computer_symbol


def clean_board(board):
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    return board


def draw_board(board):
    row_counter = 0             # TODO Check if row_counter can be replaced by some nicer way of counting items in a list
    for row in board:
        row_to_print = ""

        for i in range(3):
            if i < 2:
                row_to_print = row_to_print + row[i] + " | "
            else:
                row_to_print = row_to_print + row[i]

        if row_counter < 2:
            print(row_to_print)
            print("---------")
        else:
            print(row_to_print)

        row_counter += 1


def check_if_empty(row, column, board):
    if board[row - 1][column - 1] == ".":
        is_empty = True
    else:
        is_empty = False

    return is_empty


def check_field_left(board):
    counter = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == ".":
                counter += 1

    if counter == 0:
        board = print_finish_menu(board, '999', computer_symbol, player_symbol, finished)
        is_full = True
    else:
        is_full = False
    return board, is_full


def pick_computer_move(board):
    is_busy = True

    while is_busy:
        choosen_row = random.randint(1, 3)
        choosen_field = random.randint(1, 3)

        if check_if_empty(choosen_row, choosen_field, board):
            is_busy = False
        else:
            continue

    return choosen_row, choosen_field


def make_move(symbol, board, row, field):
    if symbol == 0:
        board[row - 1][field - 1] = "O"
    else:
        board[row - 1][field - 1] = "X"


def print_move_menu(board):
    is_empty = False

    while not is_empty:
        player_field = input("Input two digits - first for the row (1-3) and second for column (1-3): ")
        print("________________________________________________________________________________________")

        try:
            player_row = int(player_field[0:1])
            player_column = int(player_field[1:2])

            try:
                if check_if_empty(player_row, player_column, board):
                    is_empty = True
                else:
                    print("Chosen field is not empty, chose another one")
                    print("________________________________________________________________________________________")

            except IndexError:
                print("Given numbers are out of range")

        except ValueError:
            print("Given value is not a number in required range")

    return player_row, player_column


def print_finish_menu(board, result, comp_symbol, player_symbol, finished):
    print("________________________________________________________________________________________")
    draw_board(board)

    if result == "XXX":
        if player_symbol == 0:
            print("Computer won!")
        else:
            print("You won, congratulations!")
    elif result == "OOO":
        if player_symbol == 0:
            print("You won, congratulations!")
        else:
            print("Computer won!")
    elif result == "999":
        print("Board full, draw")

    finished = True

    return board, finished


def check_if_finished(board, computer_symbol, player_symbol, finished):
    result_horizontal = ""
    result_vertical = ""
    result_diag_left = ""           # Diagonally from top left to bottom right
    result_diag_right = ""          # Diagonally from top right to bottom left
    for i in range(3):
        for j in range(3):
            result_horizontal = result_horizontal + board[i][j]
            result_vertical = result_vertical + board[j][i]
            result_diag_left = result_diag_left + board[j][j]
            result_diag_right = result_diag_right + board[2-j][j]

        if result_horizontal == "XXX" or result_horizontal == "OOO":
            result = result_horizontal
            board, finished = print_finish_menu(board, result, computer_symbol, player_symbol, finished)
        elif result_vertical == "XXX" or result_vertical == "OOO":
            result = result_vertical
            board, finished = print_finish_menu(board, result, computer_symbol, player_symbol, finished)
        elif result_diag_left == "XXX" or result_diag_left == "OOO":
            result = result_diag_left
            board, finished = print_finish_menu(board, result, computer_symbol, player_symbol, finished)
        elif result_diag_right == "XXX" or result_diag_right == "OOO":
            result = result_diag_right
            board, finished = print_finish_menu(board, result, computer_symbol, player_symbol, finished)
        
    return board, finished


def move(side, board, player_symbol, computer_symbol, finished):
    if side == "computer":
        board, is_board_full = check_field_left(board)
        if is_board_full:
            finished = True
        else:
            computer_row, computer_field = pick_computer_move(board)
            make_move(computer_symbol, board, computer_row, computer_field)
            board, finished = check_if_finished(board, computer_symbol, player_symbol, finished)

    elif side == "player":
        board, is_board_full = check_field_left(board)
        if is_board_full:
            finished = True
        else:
            draw_board(board_data)
            player_row, player_column = print_move_menu(board)
            make_move(player_symbol, board, player_row, player_column)
            board, finished = check_if_finished(board, computer_symbol, player_symbol, finished)
    return board, finished


#  __main__
while True:
    restart = False
    
    player_symbol, computer_symbol = print_start_menu()
    starting_player = random.randint(0, 1)
    board_data = clean_board(board_data)

    while not restart:
        finished = False

        while not finished:
            
            if starting_player == 0:
                board_data, finished = move("computer", board_data, player_symbol, computer_symbol, finished)
                board_data, finished = move("player", board_data, player_symbol, computer_symbol, finished)
            else:
                board_data, finished = move("player", board_data, player_symbol, computer_symbol, finished)
                board_data, finished = move("computer", board_data, player_symbol, computer_symbol, finished)

        if_again = int(input("If you want to play again enter 1, otherwise enter 0: "))
        if if_again == 1:
            restart = True
        else:
            exit()
