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
        letters = []
        for cell in row:
            if cell and cell[0] != "N":
                if cell[0] == "Y":
                    letters.append('\033[92mY\033[0m')
                elif cell[0] == "O":
                    letters.append("\033[94mO\033[0m")
            else:
                letters.append("N")
        row_str = ' '.join(letters)
        print(row_str)

def fill_game_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not board[i][j]:
                board[i][j].append("N")
            else:
                board[i][j][0]='Y'


fill_game_board(board)
