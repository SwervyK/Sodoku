import random
import numpy as np

board = np.zeros((9, 9))
visible = np.zeros((9, 9))
sections = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    
def generate_board(show=False):
    for c in range(len(board)):
        for r in range(len(board[c])):
            condition = True
            number = 0
            while condition:
                for l in board:
                    print(l)
                number = random.randint(1, 9)
                if check(0, c, number) and check(1, r, number) and check(2, sections[int((c)/3)][int((r)/3)], number):
                    condition = False
            board[c][r] = number
    if show:
        for l in board:
            print(l)
                
            
# 0 = row
# 1 = colum
# 2 = box
def check(axis, index, number):
    if axis == 0:
        for i in range(len(board[index])):
            if board[index][i] == number:
                return False
    if axis == 1:
        for i in range(len(board)):
            if board[i][index] == number:
                return False
    if axis == 2:
        section = board[(3-(3-int((index-1)/3)*3)):((3-(3-int((index-1)/3)*3))+3),(((index-(3*((int((index-1)/3)+1)-1)))*3)-3):((index-(3*((int((index-1)/3)+1)-1)))*3)]
        for i in range(len(section)):
            for j in range(len(section[i])):
                if section[i][j] == number:
                    return False
    return True
        
generate_board(True)