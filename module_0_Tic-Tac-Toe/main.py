# This is a Tic-Tac-Toe script

def display_board(game_board):
    # отображение игрового поля с разделителями табуляция и вертикальная строка
    print()
    print("Текущее поле игры")
    print("\t\t0\t|\t1\t|\t2\t|")
    print("_" * 29)
    for i in range(3):
        print(i, end="\t|\t")
        for j in range(3):
            print(game_board[i][j], end="\t|\t")
        print()
        print("_" * 29)
    return


def enter_line_col(line_col_txt):
    # функция с рекурсивным вызовом для ввода координат - строки и столбца
    inp_line_col = input(line_col_txt + " (0-2): ")
    if inp_line_col.isdigit():  # проверка, что вводится цифровое значение
        inp_line_col = int(inp_line_col)
        if not 0 <= inp_line_col <= 2:  # проверка, что вводится цифра из диапазона
            print("Некорректный ввод")
            inp_line_col = enter_line_col(line_col_txt)  # рекурсивный вызов в случае ошибочного ввода
    else:
        print("Некорректный ввод")
        inp_line_col = enter_line_col(line_col_txt)  # рекурсивный вызов в случае ошибочного ввода
    return inp_line_col


def check_victory(who, board):
    # функция проверки на победу, поражение или ничью
    # статус 1 - победа X, статус 2 - победа 0, статус 3 - ничья, статус 0 - продолжаем играть
    victory_status = 0
    # проверим строки
    for i in range(3):
        # если вся строка заполнена идентичными символами
        if board[i][0] == who and board[i][1] == who and board[i][2] == who:
            # возвращаем статус в зависимости от того, кто победил
            victory_status = 1 if who == 'X' else 2
            return victory_status
    # проверим столбцы
    for i in range(3):
        # если весь столбец заполнен идентичными символами
        if board[0][i] == who and board[1][i] == who and board[2][i] == who:
            # возвращаем статус в зависимости от того, кто победил
            victory_status = 1 if who == 'X' else 2
            return victory_status
    # проверим диагонали
    if (board[0][0] == who and board[1][1] == who and board[2][2] == who) or (
    (board[0][2] == who and board[1][1] == who and board[2][0] == who)):
        # возвращаем статус в зависимости от того, кто победил
        victory_status = 1 if who == 'X' else 2
        return victory_status
    # так как здесь и далее статус 'не победа', то проверка на ничью
    count_non_empty_cells = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                # если хоть одна ячейка не заполнена, то продолжаем играть
                victory_status = 0
                return victory_status
            else:
                count_non_empty_cells += 1
    # если все значения заполнены и никто не победил, то ничья
    if count_non_empty_cells == 9:
        victory_status = 3

    return victory_status


def next_comp_move(board, who):
    # ход компьютера
    # если в переменной who - X, то в переменой opponent - 0 и наоборот
    opponent = "X" if who == "0" else "0"

    # проверим возможность победы - если две ячейки уже заполнены компьютером, то захватываем третью и побеждаем
    # по строкам
    for i in range(3):
        count_X = 0
        for j in range(3):
            if board[i][j] == opponent:
                count_X += 1
            else:
                empty_line = i
                empty_col = j

        if count_X == 2 and board[empty_line][empty_col] != who:
            board[empty_line][empty_col] = opponent
            return

    # проверим возможность победы - если две ячейки уже заполнены компьютером, то захватываем третью и побеждаем
    # по столбцам
    for j in range(3):
        count_X = 0
        for i in range(3):
            if board[i][j] == opponent:
                count_X += 1
            else:
                empty_line = i
                empty_col = j

        if count_X == 2 and board[empty_line][empty_col] != who:
            board[empty_line][empty_col] = opponent
            return

    # проверим возможность победы - если две ячейки уже заполнены компьютером, то захватываем третью и побеждаем
    # по диагонали
    count_X = 0
    for i in range(3):
        if board[i][i] == opponent:
            count_X += 1
        else:
            empty_line = i

    if count_X == 2 and board[empty_line][empty_line] != who:
        board[empty_line][empty_line] = opponent
        return

    # проверим угрозы со стороны человека
    # по строкам
    for i in range(3):
        count_X = 0
        for j in range(3):
            if board[i][j] == who:
                count_X += 1
            else:
                empty_line = i
                empty_col = j

        if count_X == 2 and board[empty_line][empty_col] != opponent:
            board[empty_line][empty_col] = opponent
            return

    # проверим угрозы со стороны человека
    # по столбцам
    for j in range(3):
        count_X = 0
        for i in range(3):
            if board[i][j] == who:
                count_X += 1
            else:
                empty_line = i
                empty_col = j

        if count_X == 2 and board[empty_line][empty_col] != opponent:
            board[empty_line][empty_col] = opponent
            return

    # проверим угрозы со стороны человека
    # по диагонали
    count_X = 0
    for i in range(3):
        if board[i][i] == who:
            count_X += 1
        else:
            empty_line = i

    if count_X == 2 and board[empty_line][empty_line] != opponent:
        board[empty_line][empty_line] = opponent
        return

    # проверка и захват углов по возможности
    if board[1][1] == '':
        board[1][1] = opponent
    elif board[0][0] == '':
        board[0][0] = opponent
    elif board[0][2] == '':
        board[0][2] = opponent
    elif board[2][0] == '':
        board[2][0] = opponent
    else:
        # иначе ставим в любое свободное поле, обходя матрицу двумя циклами
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = opponent
                    return
    return


def playing_side():
    # узнаем, за кого играет человек? с помощью рекурсивной фугкции в случае ошибки ввода
    side = input("Выберите, за кого играете ==> (X) или (0) ? ")
    if not (side == "X" or side == "0"):
        print("Неправильный выбор!")
        side = playing_side()
    return side


# основное тело программы
# инициализация массива - игрового поля
board = []
for i in range(3):
    board.append(['', '', ''])
# первоначальное отображение игрового поля
display_board(board)
# делаем выбор, за кого играть
human_plays = playing_side()  # в этой переменной храним, за кого играет человек

if human_plays == "0":  # если человк играет ноликами, то первый ход за компьютером
    next_comp_move(board, human_plays)
    display_board(board)
    comp_plays = "X"  # в этой переменной храним, за кого играет компьютер
else:
    comp_plays = "0"  # в этой переменной храним, за кого играет компьютер

# начинаем основной "бесконечный цикл" игры
while True:
    # Ход человека
    print("Введите следущий ход ==>")
    # запуск рекурсивной функции для ввода строи и столбца хода человека
    line = enter_line_col("Строка")
    column = enter_line_col("Столбец")
    # проверям, не занята ли уже выбранная ячейка
    if board[line][column] != '':
        print("Ячейка " + str(line) + " " + str(column) + " уже занята")
        continue
    # заполняем элемент массива-ячейку и отображаем обновленное поле игры
    board[line][column] = "X" if human_plays == "X" else "0"
    display_board(board)
    # проверим статус - победа/поражение/ничья/продолжение игры
    is_victory = check_victory(human_plays, board)
    if is_victory == 1:
        print("Поздравляю, выиграли X")
        break
    elif is_victory == 2:
        print("Поздравляю, выиграли 0")
        break
    elif is_victory == 3:
        print("Игра окончена, Ничья")
        break
    # ход компьютера
    next_comp_move(board, human_plays)
    display_board(board)
    # проверим статус - победа/поражение/ничья/продолжение игры
    is_victory = check_victory(comp_plays, board)
    if is_victory == 1:
        print("Поздравляю, выиграли X")
        break
    elif is_victory == 2:
        print("Поздравляю, выиграли 0")
        break
    elif is_victory == 3:
        print("Игра окончена, Ничья")
        break
