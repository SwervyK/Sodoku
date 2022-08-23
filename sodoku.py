import random
import numpy as np

main_board = np.zeros((9, 9))
sections = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    
def generate_board(show=False):
    for index in 1,5,9:
        section = main_board[(3-(3-int((index-1)/3)*3)):((3-(3-int((index-1)/3)*3))+3),(((index-(3*((int((index-1)/3)+1)-1)))*3)-3):((index-(3*((int((index-1)/3)+1)-1)))*3)]
        for c in range(len(section)):
            for r in range(len(section[c])):
                number = random.randint(1, 9)
                while (not check(2, index, number, main_board)):
                    number = random.randint(1, 9)
                main_board[c+(3-(3-int((index-1)/3)*3))][r+(((index-(3*((int((index-1)/3)+1)-1)))*3)-3)] = number
    for c in range(len(main_board)):
        for r in range(len(main_board[c])):
            for l in main_board: #######
                print(l)    #######
            if main_board[c][r] != 0: continue
            number = random.randint(1, 9)
            while (not check(0, r, number, main_board) or not check(1, c, number, main_board) or not check(2, sections[int(c/3)][int(r/3)], number, main_board)):
                number = random.randint(1, 9)
            main_board[c][r] = number
    if show:
        for l in main_board:
            print(l)
            
def generate_valid_board(num_random, show=False):
    for index in range(1, 10):
        colum = (index - (int((index-1)/3))*3)-1
        row = (int((index-1)/3))
        section = np.array(sections.copy())
        
        section = np.roll(section, colum*3)

        for vertical in range(row):
            temp = section[:, len(section[0])-1].copy()
            for r in range(len(section[0])):
                section[:,len(section)-r-1] = section[:,len(section)-r-2]
            section[:,0] = temp
        
        for c in range(len(section)):
            for r in range(len(section[c])):
                main_board[c+(3-(3-int((index-1)/3)*3))][r+(((index-(3*((int((index-1)/3)+1)-1)))*3)-3)] = section[c,r].copy()
    if print:
        for l in main_board: print(l)

def randomize_board(board):
    board = np.array(board)
    horizontal = random.randint(0,1)
    vertical = random.randint(0,1)
    rotation = random.randint(0,3)
    if horizontal == 1:
        np.flip(board, axis=0)
    if vertical == 1:
        np.flip(board, axis=1)
    np.rot90(board, rotation, axes=(1,0))
    for i in range(1,10):
        number = random.randint(1,9)
        while number != i:
            number = random.randint(1,9)
        board = np.where(board == i, 0, board)
        board = np.where(board == number, i, board)
        board = np.where(board == 0, number, board)
                
    
# 0 = row
# 1 = colum
# 2 = box
def check(axis, index, number, board_to_check):
    if axis == 0:
        for i in range(len(board_to_check[index])):
            if board_to_check[index][i] == number:
                return False
    if axis == 1:
        for i in range(len(board_to_check)):
            if board_to_check[i][index] == number:
                return False
    if axis == 2:
        section = board_to_check[(3-(3-int((index-1)/3)*3)):((3-(3-int((index-1)/3)*3))+3),(((index-(3*((int((index-1)/3)+1)-1)))*3)-3):((index-(3*((int((index-1)/3)+1)-1)))*3)]
        for i in range(len(section)):
            for j in range(len(section[i])):
                if section[i][j] == number:
                    return False
    return True
        
#generate_board(True)
generate_valid_board(100, True)