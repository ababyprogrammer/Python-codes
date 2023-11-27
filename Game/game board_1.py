def initialize_board():
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            if (i + j) % 2 == 0:
                row.append(" ")
            else:
                if i < 2:
                    row.append("p")
                elif i > 5:
                    row.append("P")
                else:
                    row.append(" ")
        board.append(row)
    return board


def main():
    board = initialize_board()
    print_board(board)
