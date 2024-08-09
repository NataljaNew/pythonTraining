def create_darts_board(side):
    board = [[0 for _ in range(side)] for _ in range(side)]
    for i in range(side):
        for j in range(side):
            if i <= j and i <= (side - 1 - j):
                board[i][j] = i + 1
            elif j >= i >= (side - 1 - j):
                board[i][j] = side - j
            elif j < i > (side - 1 - j):
                board[i][j] = side - i
            elif j < i <= (side - 1 - j):
                board[i][j] = j + 1

    for row in board:
        print(' '.join(map(str, row)))


side = int(input())
create_darts_board(side)
