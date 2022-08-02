import random

board = [[0] * 9] * 9
visible = [[0] * 9] * 9
    
def generate_board():
    for i in len(board):
        for j in len(board[j]):
            condition = True
            number = 0
            while condition:
                number = random.randint(1, 10)
                if check(0, i, number) and check(1, j, number) and check(2, i, number): # Section
                    condition = False
            board[i][j] = number
            
    print(board)
# 0 = row
# 1 = colum
# 2 = box
def check(axis, index, number):
    if axis == 0:
        for i in len(board):
            if board[i][index] == number:
                return True
    if axis == 1:
        for i in len(board[index]):
            if board[index][i] == number:
                return True
    if axis == 2:
        section = board[0:3][0:3] # Split
        for i in len(section):
            for j in len(section[j]):
                if section[i][j] == number:
                    return False
    return False
        
    
generate_board()