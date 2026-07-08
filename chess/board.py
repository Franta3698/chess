import pieces

def setup_board():
    board = [[0]*8,
             [0]*8,
             [0]*8,
             [0]*8,
             [0]*8,
             [0]*8,
             [0]*8,
             [0]*8]
    return board

def print_board(board):
    for arr in board:
        print(arr)

def piece_finder(board, id):
    found = 0
    for row in board:
        for col in row:
            if int(id) == int(col):
                found += 1
                print("nalezen")
    return found







if __name__ == "__main__":
    board = setup_board()

    for i in range(8):
        board[6][i] = pieces.bPawns[i].id


    choose = input("Zadej pozici figurky: ")

    if piece_finder(board, choose):
        print("je to tak")


    print_board(board)