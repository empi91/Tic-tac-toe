import random

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

def move():
    pass



##  __main__
draw_board()


