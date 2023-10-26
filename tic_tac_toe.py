import random

finished = False
#player_symbol = 0              # 0 - 0, 1 - X
starting_player = 0             # 0 - computer starts, 1 - player starts
board_data = [ [".", ".", "."], [".", ".", "."], [".", ".", "."]]


##  __functions__
def print_start_menu():
    print("Hello! \nIn this game you are playing a tic-tac-toe game with computer. \nRules are simple: \n- game board is 3x3; \n- you can draw X or O in an empty field; \n- Whoever gets three X or O in the row (vertical, horizontal or diagonally) wins \nGood Luck!")
    player_symbol = int(input("Choose 0 if you want to play with O or choose 1 if you want to play with X: "))
    print("________________________________________________________________________________________")
    if player_symbol == 0: computer_symbol = 1
    else: computer_symbol = 0
    return player_symbol, computer_symbol

def draw_board(board):
    row_counter = 0             #TODO Check if row_counter can be replaced by some nicer way of counting items ina list
    for row in board:
        row_to_print = ""
        
        for i in range(3):
            if i < 2: row_to_print = row_to_print + row[i] + " | "
            else: row_to_print = row_to_print + row[i]

        if row_counter < 2:
            print(row_to_print)
            print("---------")
        else:
            print(row_to_print)
            
        row_counter += 1

def check_if_empty(row, column, board):
    if board[row - 1][column -1] == ".": is_empty = True
    else: is_empty = False
    return is_empty
    
def pick_computer_move(board):
    is_busy = True

    while is_busy:
        choosen_row = random.randint(1, 3)
        choosen_field = random.randint(1, 3)
        
        if check_if_empty(choosen_row, choosen_field, board): is_busy = False
        else: continue

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
        
        player_row = int(player_field[0:1])
        player_column = int(player_field[1:2])
        
        if check_if_empty(player_row, player_column, board): is_empty = True
        else:
            print("Chosen field is not empty, chose another one")
            print("________________________________________________________________________________________")
        
    return player_row, player_column

def print_finish_menu():
    # TODO Display when game finished
    pass

def move(side):
    if side == "computer":
        computer_row, computer_field = pick_computer_move(board_data)
        make_move(computer_symbol, board_data, computer_row, computer_field)
        check_if_finished(board_data)
        
    elif side == "player":
        draw_board(board_data)
        player_row, player_column = print_move_menu(board_data)
        make_move(player_symbol, board_data, player_row, player_column)
        check_if_finished(board_data)

##  __main__
player_symbol, computer_symbol = print_start_menu()
starting_player = random.randint(0, 1)

while not finished:
    if starting_player == 0:
        move("computer")
        move("player")
    else:
        move("player")
        move("computer")







