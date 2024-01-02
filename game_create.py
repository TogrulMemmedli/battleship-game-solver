import random
from game import visualize_game, fill_game_board

game_board = [
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
]

def game_board_possibility(a, b, str):
    game_board[a][b] = [str]
    if [a, b] in possibilities:
        possibilities.remove([a, b])



possibilities = []
for i in range(10):
    for j in range(10):
        possibilities.append([i, j])
print("Before:", len(possibilities))

def ship_placement(ship_length):
    ship_cells = random.choice(possibilities)
    game_board_possibility(ship_cells[0], ship_cells[1], 'Y')

    is_vertical = True if random.randint(0, 1) == 1 else False
    if is_vertical:
        y_u, y_d, x = ship_cells[0], ship_cells[0], ship_cells[1]
        for i in range(ship_length-1):
            is_up = True if (random.randint(0, 1) == 1) else False
            if y_u==0:
                is_up=False
            elif y_d==9:
                is_up=True

            if is_up:
                y_u = y_u-1
                game_board_possibility(y_u, x, "Y")
            else:
                y_d = y_d+1
                game_board_possibility(y_d, x, "Y")


        if y_u != 0:
            game_board_possibility(y_u-1, x, "O")

            if x!=0:
                game_board_possibility(y_u-1, x-1, "O")
            if x!=9:
                game_board_possibility(y_u-1, x+1, "O")


        if y_d != 9:
            game_board_possibility(y_d+1, x, "O")
            if x!=0:
                game_board_possibility(y_d+1, x-1, "O")
            if x!=9:
                game_board_possibility(y_d+1, x+1, "O")

        if x!=0:
            for l in range(y_u, y_d+1):
                game_board_possibility(l, x-1, "O")
        if x!=9:
            for l in range(y_u, y_d+1):
                game_board_possibility(l, x+1, "O")


    else:
        y, x_l, x_r = ship_cells[0], ship_cells[1], ship_cells[1]
        for i in range(ship_length-1):
            is_right = True if (random.randint(0, 1) == 1) else False
            if x_r==9:
                is_right=False
            if x_l==0:
                is_right=True

            if is_right:
                x_r = x_r+1
                game_board_possibility(y, x_r, "Y")
            else:
                x_l = x_l-1
                game_board_possibility(y, x_l, "Y")

        if x_r != 9:
            game_board_possibility(y, x_r+1, "O")

            if y!=0:
                game_board_possibility(y-1, x_r+1, "O")

            if y!=9:
                game_board_possibility(y+1, x_r+1, "O")

        if x_l != 0:
            game_board_possibility(y, x_l-1, "O")
            if y!=0:
                game_board_possibility(y-1, x_l-1, "O")

            if y!=9:
                game_board_possibility(y+1, x_l-1, "O")

        if y!=0:
            for l in range(x_l, x_r+1):
                game_board_possibility(y-1, l, "O")

        if y!=9:
            for l in range(x_l, x_r+1):
                game_board_possibility(y+1, l, "O")


ship_placement(4)
print("After:", len(possibilities))
visualize_game(board=game_board)
