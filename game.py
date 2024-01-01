# Game Board
board = [
    [[],[],[],[],[],[],[],[],[],["Y"]],
    [[],[],[],[],[],[],[],[],[],["Y"]],
    [[],[],[],[],[],[],[],["Y"],[],["Y"]],
    [["Y"],["Y"],["Y"],["Y"],[],["Y"],[],[],[],[]],
    [[],[],[],[],[],[],[],[],["Y"],["Y"]],
    [[],[],[],[],["Y"],["Y"],[],[],[],[]],
    [["Y"],["Y"],["Y"],[],[],[],[],[],["Y"],[]],
    [[],[],[],[],[],[],[],[],["Y"],[]],
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],["Y"],[],["Y"],[],[],[],[]],
]


# board visualization
def visualize_game(board):
    for row in board:
        row_str = ' '.join(['N' if not cell else str(cell[0]) for cell in row])
        print(row_str)

def fill_game_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not board[i][j]:
                board[i][j].append("N")
            else:
                board[i][j][0]='Y'


fill_game_board(board)
