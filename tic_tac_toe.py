import random

finished = False
board_data = [ [".", ".", "."], [".", ".", "."], [".", ".", "."]]

def draw_board():
    row_counter = 0  #TODO Check if row_counter can be replaced by some nicer way of counting items ina list
    for row in board_data:
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

def print_start_menu():
    print("Hello! \nIn this game you are playing a tic-tac-toe game with computer. \nRules are simple: \n- game board is 3x3; \n- you can draw X or O in an empty field; \n- Whoever gets three X or O in the row (vertical, horizontal or diagonally) wins \nGood Luck!")

def print_move_menu():
    pass

def print_finish_menu():
    pass

def move():
    print_menu()
    save_move_to_board()
    draw_board()
    pass


##  __main__
print_start_menu()

while not finished:
    draw_board()
    print_move_menu()



