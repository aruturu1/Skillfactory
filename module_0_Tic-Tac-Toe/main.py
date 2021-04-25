# This is a Tic-Tac-Toe script.

def display_board(board):
    print()
    print("Текущее поле игры")
    print("\t\t0\t|\t1\t|\t2\t|")
    print("__________________________")
    for i in range(3):
        print(i, end="\t|\t")
        for j in range(3):
            print(board[i][j], end="\t|\t")
        print()
        print("__________________________")
    return


def enter_line_col(line_col_txt):
    inp_line_col = input(line_col_txt + " (0-2): ")
    if inp_line_col.isdigit():
        inp_line_col = int(inp_line_col)
        if not 0 <= inp_line_col <= 2:
            print("Некорректный ввод")
            inp_line_col=enter_line_col(line_col_txt)
    else:
        print("Некорректный ввод")
        inp_line_col=enter_line_col(line_col_txt)
    return inp_line_col


def check_victory(who, board):
    victory_status=0
    # проверим строки
    for i in range(3):
        if board[i][0] == who and board[i][1] == who and board[i][2] == who:
            victory_status = 1 if who=='X' else 2
            return victory_status
    # проверим столбцы
    for i in range(3):
        if board[0][i] == who and board[1][i] == who and board[2][i] == who:
            victory_status = 1 if who=='X' else 2
            return victory_status
    # проверим диагонали
    if (board[0][0] == who and board[1][1] == who and board[2][2] == who) or ((board[0][2] == who and board[1][1] == who and board[2][0] == who)):
            victory_status = 1 if who=='X' else 2
            return victory_status
    # проверка на ничью - если все значения заполнены
    count_non_empty_cells = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                victory_status=0
                return victory_status
            else:
                count_non_empty_cells += 1

    if count_non_empty_cells == 9:
        victory_status = 3

    return victory_status


def next_comp_move(board):
    for i in range(3):
        count_X = 0
        for j in range(3):
            if board[i][j] == 'X':
                count_X += 1
            else:
                empty_line = i
                empty_col = j

            if count_X == 2 and board[empty_line][empty_col] != "O":
                board[empty_line][empty_col] = "O"
                return

    for j in range(3):
        count_X = 0
        for i in range(3):
            if board[i][j] == 'X':
                count_X += 1
            else:
                empty_line = i
                empty_col = j

            if count_X == 2 and board[empty_line][empty_col] != "O":
                board[empty_line][empty_col] = "O"
                return

    count_X = 0
    for i in range(3):
        if board[i][i] == 'X':
            count_X += 1
        else:
            empty_line = i

        if count_X == 2 and board[empty_line][empty_line] != "O":
            board[empty_line][empty_line] = "O"
            return

    if board[1][1] == '':
        board[1][1]='O'
    elif board[0][0] == '':
        board[0][0] = 'O'
    elif board[0][2] == '':
        board[0][2] = 'O'
    elif board[2][0] == '':
        board[2][0] = 'O'
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    return
    return


board = []
# инициализация массива - игрового поля
for i in range(3):
    board.append(['', '', ''])

display_board(board)

while True:
    # Ход человека крестиками
    print("Введите следущий ход ==>")
    # заполнение элемента массива
    line=enter_line_col("Строка")
    column=enter_line_col("Столбец")
    if board[line][column] != '':
        print("Ячейка "+str(line)+" "+str(column)+" уже занята")
        continue
    board[line][column] = "X"

    display_board(board)
    is_victory = check_victory("X", board)
    if is_victory == 1:
        print("Поздравляю, Вы выиграли")
        break
    elif is_victory == 3:
        print("Игра окончена, Ничья")
        break

    next_comp_move(board)
    display_board(board)
    is_victory = check_victory("O", board)
    if is_victory == 2:
        print("К сожалению, Вы проиграли")
        break
    elif is_victory == 3:
        print("Игра окончена, Ничья")
        break
