def print_matr(print_cells):
    matrix = [[0] * 9 for i in range(5)]
    for i in range(5):
        for j in range(9):
            if i == 0 or i == 4:
                matrix[i][j] = "-"
            elif j == 0 or j == 8:
                matrix[i][j] = "|"
            elif j % 2 == 0:
                matrix[i][j] = print_cells[int(3 * (i - 1) + (j * 0.5)) - 1]
            else:
                matrix[i][j] = " "
            print(matrix[i][j], end="")
        print()


def check_difference(st):
    return abs(st.count('X') - st.count('O'))


def check_win_for_symbol(st, symb):
    for i in range(0, 3):
        if st[0 + 3 * i] == st[1 + 3 * i] == st[2 + 3 * i] == symb:
            return True
            break
        if st[0 + i] == st[3 + i] == st[6 + i] == symb:
            return True
            break
        if st[0] == st[4] == st[8] == symb or st[2] == st[4] == st[6] == symb:
            return True
            break
    return False


def check_empty(st):
    return ' ' in st


def ask_coords(st, symb):
    correct_input = False
    while not correct_input:
        x, y = input("Enter the coordinates: ").split()
        if not x.isdigit() or not y.isdigit():
            print("You should enter numbers!")
            continue
        x = int(x)
        y = int(y)
        if x < 1 or x > 3 or y > 3 or x < 1:
            print("Coordinates should be from 1 to 3!")
        elif st[x - 3 * y + 8] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            st
            st = list(st)
            st[x - 3 * y + 8] = symb
            "".join(st)
            return st


cells = "         "
print(len(cells))
print_matr(cells)
game_not_finish = True
symbols = ["X", "O"]
turn = 0
while game_not_finish:
    cells = ask_coords(cells, symbols[turn % 2])
    print_matr(cells)
    turn += 1
    if check_difference(cells) >= 2:
        print('Impossible')
        game_not_finish = False
    elif check_win_for_symbol(cells, 'X') and check_win_for_symbol(cells, 'O'):
        print('Impossible')
        game_not_finish = False
    elif check_win_for_symbol(cells, 'X'):
        print('X wins')
        game_not_finish = False
    elif check_win_for_symbol(cells, 'O'):
        print('O wins')
        game_not_finish = False
    elif not check_empty(cells):
        print('Draw')
        game_not_finish = False
