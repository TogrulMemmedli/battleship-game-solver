from game import board as solved_board
from game import visualize_game, fill_game_board


def board_info(title, game_board):
    print(f"{title} Board:")
    visualize_game(game_board)
    print("\n" + "-" * 40 + "\n")

def round_info():
    print(f"Round: {round_count}\nBoard Finished at: {solve_round}\n")

round_count = 0  
solve_round = 0

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
fill_game_board(game_board)

# brute force search algorithm
def brute_force_search():
    global round_count
    global solve_round

    for x in range(len(game_board)):
        for y in range(len(game_board[x])):
            round_count += 1
            if solved_board[x][y][0]=="Y":
                solve_round=round_count
                game_board[x][y][0]="Y"

print("\n")
board_info("Solved", solved_board)
board_info("Before Algorithm Game", game_board)
brute_force_search()
board_info("After Algorithm Game", game_board)

round_info()