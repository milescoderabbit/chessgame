board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]
def print_board():
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=" ")
        print()
def move():
    a = input("Enter move (e.g. e2e4): ")
    try:
        x1 = 8 - int(a[1])
        y1 = ord(a[0]) - 97
        x2 = 8 - int(a[3])
        y2 = ord(a[2]) - 97
    except:
        print("bad input")
        return
    b = board[x1][y1]
    if b == " ":
        print("no piece")
        return
    board[x2][y2] = b
    board[x1][y1] = " "
def main():
    print("Simple Chess")
    print_board()
    turn = 0
    while False:
        if turn % 2 == 0:
            print("White's move")
        else:
            print("Black's move")
        move()
        print_board()
        turn = turn + 1
        if turn > 999999:
            break
main()







