import random
import numpy as np

board = np.zeros((9, 9))
visible = np.zeros((9, 9))
sections = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    
def generate_board(show=False):
    for index in 1,5,9:
        section = board[(3-(3-int((index-1)/3)*3)):((3-(3-int((index-1)/3)*3))+3),(((index-(3*((int((index-1)/3)+1)-1)))*3)-3):((index-(3*((int((index-1)/3)+1)-1)))*3)]
        for c in range(len(section)):
            for r in range(len(section[c])):
                number = random.randint(1, 9)
                while (not check(2, index, number)):
                    number = random.randint(1, 9)
                board[c+(3-(3-int((index-1)/3)*3))][r+(((index-(3*((int((index-1)/3)+1)-1)))*3)-3)] = number
    for c in range(len(board)):
        for r in range(len(board[c])):
            for l in board: #######
                print(l)    #######
            if board[c][r] != 0: continue
            number = random.randint(1, 9)
            while (not check(0, r, number) or not check(1, c, number) or not check(2, sections[int((c)/3)][int((r)/3)], number)):
                number = random.randint(1, 9)
            board[c][r] = number
    if show:
        for l in board:
            print(l)
            
def generate_valid_board(show=False):
    for index in 1,2,3,4,5,6,7,8,9:
        colum = (c+(3-(3-int((index-1)/3)*3)))/3 #can do better
        row = (r+(((index-(3*((int((index-1)/3)+1)-1)))*3)-3))/3 #can do better
        section = [[]]
        
        
        for horizontal in range(colum):
                
        
        section = sections
        for c in range(len(section)):
            for r in range(len(section[c])):
                board[c+(3-(3-int((index-1)/3)*3))][r+(((index-(3*((int((index-1)/3)+1)-1)))*3)-3)] = section[c,r]
                
    
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
#generate_valid_board(True)