from random import randint, choice
from copy import deepcopy


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def check_winner(board, color):
    # Check rows
    for row in board:
        for i in range(len(row) - 5):
            if all(row[i + j] == color for j in range(5)):
                return True

    # Check columns
    for col in range(len(board[0])):
        for i in range(len(board) - 5):
            if all(board[i + j][col] == color for j in range(5)):
                return True

    # Check diagonals (top-left to bottom-right)
    for start_row in range(len(board) - 5):
        for start_col in range(len(board[0]) - 5):
            if all(board[start_row + i][start_col + i] == color for i in range(5)):
                return True

    # Check diagonals (top-right to bottom-left)
    for start_row in range(len(board) - 5):
        for start_col in range(5, len(board[0])):
            if all(board[start_row + i][start_col - i] == color for i in range(5)):
                return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)


def detect_rows(board, player, length):
    size = len(board)
    open_count = 0
    semi_open_count = 0

    def is_valid_window(window):
        return window.count(player) == length - 1 and ' ' in window

    # Check rows
    for row in board:
        seq = "".join(row)
        for start in range(size - length):
            end = start + length
            open_states = 0

            if seq[start:end] != player * length:
                continue

            if seq[start - 1] == player or seq[end] == player:
                continue

            if start == 0:
                if seq[end] == ' ':
                    semi_open_count += 1
                    continue

            if end == size:
                if seq[start - 1] == ' ':
                    semi_open_count += 1
                    continue

            if seq[end] == ' ':
                open_states += 1
            if seq[start - 1] == ' ':
                open_states += 1

            if open_states == 1:
                semi_open_count += 1
            elif open_states == 2:
                open_count += 1



    # Check columns
    for col in range(size):
        seq = ""
        for row in range(size):
            seq += board[row][col]


        for start in range(size - length):
            end = start + length
            open_states = 0

            if seq[start:end] != player * length:
                continue

            if seq[start - 1] == player or seq[end] == player:
                continue

            if start == 0:
                if seq[end] == ' ':
                    semi_open_count += 1
                    continue

            if end == size:
                if seq[start - 1] == ' ':
                    semi_open_count += 1
                    continue

            if seq[end] == ' ':
                open_states += 1
            if seq[start - 1] == ' ':
                open_states += 1

            if open_states == 1:
                semi_open_count += 1
            elif open_states == 2:
                open_count += 1

    # Check diagonals (from top-left to bottom-right)
    dx = 1
    dy = 1
    for row in range(size - length + 1):
        start_x = row
        start_y = 0
        sz = size - start_x
        seq = ""
        for i in range(sz):
            seq += board[start_x + dx * i][start_y + dy * i]


        for start in range(sz - length):
            end = start + length
            open_states = 0

            if seq[start:end] != player * length:
                continue

            if seq[start - 1] == player or seq[end] == player:
                continue

            if start == 0:
                if seq[end] == ' ':
                    semi_open_count += 1
                    continue

            if end == sz:
                if seq[start - 1] == ' ':
                    semi_open_count += 1
                    continue

            if seq[end] == ' ':
                open_states += 1
            if seq[start - 1] == ' ':
                open_states += 1

            if open_states == 1:
                semi_open_count += 1
            elif open_states == 2:
                open_count += 1

    for row in range(1, size - length + 1):
        start_x = 0
        start_y = row
        sz = size - start_y
        seq = ""
        for i in range(sz):
            seq += board[start_x + dx * i][start_y + dy * i]

        for start in range(sz - length):
            end = start + length
            open_states = 0

            if seq[start:end] != player * length:
                continue

            if seq[start - 1] == player or seq[end] == player:
                continue

            if start == 0:
                if seq[end] == ' ':
                    semi_open_count += 1
                    continue

            if end == sz:
                if seq[start - 1] == ' ':
                    semi_open_count += 1
                    continue

            if seq[end] == ' ':
                open_states += 1
            if seq[start - 1] == ' ':
                open_states += 1

            if open_states == 1:
                semi_open_count += 1
            elif open_states == 2:
                open_count += 1

    # Check diagonals (from top-right to bottom-left)
    dx = 1
    dy = -1
    for row in range(1, size - length + 1):
        start_x = row
        start_y = size - 1
        sz = size - start_x
        seq = ""
        for i in range(sz):
            seq += board[start_y + dy * i][start_x + dx * i]

        for start in range(sz - length):
            end = start + length
            open_states = 0

            if seq[start:end] != player * length:
                continue

            if seq[start - 1] == player or seq[end] == player:
                continue

            if start == 0:
                if seq[end] == ' ':
                    semi_open_count += 1
                    continue

            if end == sz:
                if seq[start - 1] == ' ':
                    semi_open_count += 1
                    continue

            if seq[end] == ' ':
                open_states += 1
            if seq[start - 1] == ' ':
                open_states += 1

            if open_states == 1:
                semi_open_count += 1
            elif open_states == 2:
                open_count += 1

    for row in range(1, size - length + 1):
        start_x = 0
        start_y = size - row
        sz = start_y + 1
        seq = ""
        for i in range(sz):
            seq += board[start_y + dy * i][start_x + dx * i]

        for start in range(sz - length):
            end = start + length
            open_states = 0

            if seq[start:end] != player * length:
                continue

            if seq[start - 1] == player or seq[end] == player:
                continue

            if start == 0:
                if seq[end] == ' ':
                    semi_open_count += 1
                    continue

            if end == sz:
                if seq[start - 1] == ' ':
                    semi_open_count += 1
                    continue

            if seq[end] == ' ':
                open_states += 1
            if seq[start - 1] == ' ':
                open_states += 1

            if open_states == 1:
                semi_open_count += 1
            elif open_states == 2:
                open_count += 1

    return open_count, semi_open_count

def analyze_board(board, player):
    open = []
    semi_open = []
    for length in range(2, 6):
        open_count, semi_open_count = detect_rows(board, player, length)
        open.append(open_count)
        semi_open.append(semi_open_count)

    return open, semi_open


def get_valid_moves(board):
    size = len(board)
    valid_moves = []

    for i in range(size):
        for j in range(size):
            if board[i][j] == " ":
                valid_moves.append((i, j))

    return valid_moves

def get_data():
    data = open("data", "r")
    pref = data.readlines()
    m1 = int(pref[0])
    m2 = int(pref[1])
    m3 = int(pref[2])
    m4 = int(pref[3])
    m5 = int(pref[4])
    m6 = int(pref[5])
    m7 = int(pref[6])
    m8 = int(pref[7])
    return m1, m2, m3, m4, m5, m6, m7, m8

def random_data():
    return (randint(0, 10000) for i in range(8))

def get_score(board, player):
    m1, m2, m3, m4, m5, m6, m7, m8 = get_data()

    player_open, player_semi_open = analyze_board(board, player)
    score = 0

    score += player_open[0] * m1 + player_open[1] * m2 + player_open[2] * m3 + player_open[3] * m4
    score += player_semi_open[0] * m5 + player_semi_open[1] * m6 + player_semi_open[2] * m7 + player_semi_open[3] * m8

    return score

def get_random_score(board, player):
    m1, m2, m3, m4, m5, m6, m7, m8 = random_data()

    player_open, player_semi_open = analyze_board(board, player)
    score = 0

    score += player_open[0] * m1 + player_open[1] * m2 + player_open[2] * m3 + player_open[3] * m4
    score += player_semi_open[0] * m5 + player_semi_open[1] * m6 + player_semi_open[2] * m7 + player_semi_open[3] * m8

    return score

def get_move(board, player):
    best_moves = []
    valid_moves = get_valid_moves(board)
    max_score = -100001

    opponent = ''
    if player == "w":
        opponent = "b"
    else:
        opponent = "w"

    for move in valid_moves:
        b = deepcopy(board)
        b[move[0]][move[1]] = player
        original_player_score = get_score(board, player)
        player_score = get_score(b, player)

        b[move[0]][move[1]] = opponent
        original_oppoonent_score = get_score(board, opponent)
        opponent_score = get_score(b, opponent)

        play_score = player_score - original_player_score + (opponent_score - original_oppoonent_score)

        if play_score > max_score:
            max_score = play_score
            best_moves.clear()
            best_moves.append(move)
        elif play_score == max_score:
            best_moves.append(move)

    return choice(best_moves)

def gomoku(board_size):
    board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
    current_player = 'b'
    player_move = 1

    while True:
        print_board(board)

        # Player move
        while True:
            try:
                if player_move == 1:
                    row = int(input(f"Enter row (1-{board_size}): "))
                    col = int(input(f"Enter column (1-{board_size}): "))
                else:
                    row, col = get_move(board, current_player)

                if 0 <= row < board_size and 0 <= col < board_size and board[row][col] == ' ':
                    board[row][col] = current_player
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        player_move *= -1

        # Analyze the board for the current player
        black = analyze_board(board, "b")
        white = analyze_board(board, "w")
        print("Black:")
        for i in range(4):
            print(f"Open rows of length {i + 2}: ", black[0][i])
            print(f"Semi-open rows of length {i + 2}: ", black[1][i])
        print("White:")
        for i in range(4):
            print(f"Open rows of length {i + 2}: ", white[0][i])
            print(f"Semi-open rows of length {i + 2}: ", white[1][i])

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = 'w' if current_player == 'b' else 'b'


if __name__ == "__main__":
    size = int(input("Enter the board size: "))
    gomoku(size)