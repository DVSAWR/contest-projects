"""
На шахматной доске стоят слоны и ладьи, необходимо посчитать, сколько клеток не бьется ни одной из фигур.

Шахматная доска имеет размеры 8 на 8. Ладья бьет все клетки горизонтали и вертикали, проходящих через клетку, где она
стоит, до первой встретившейся фигуры. Слон бьет все клетки обеих диагоналей, проходящих через клетку, где он стоит,
до первой встретившейся фигуры.

Формат ввода
В первых восьми строках ввода описывается шахматная доска. Первые восемь символов каждой из этих строк описывают
состояние соответствующей горизонтали: символ B (заглавная латинская буква) означает, что в клетке стоит слон,
символ R — ладья, символ * — что клетка пуста. После описания горизонтали в строке могут идти пробелы, однако
длина каждой строки не превышает 250 символов. После описания доски в файле могут быть пустые строки.

Формат вывода
Выведите количество пустых клеток, которые не бьются ни одной из фигур.

Пример 1
Ввод
********
********
*R******
********
********
********
********
********

49

Пример 2
********
********
******B*
********
********
********
********
********

54

Пример 3
********
*R******
********
*****B**
********
********
********
********

40
"""

print('---------answer----------')

vline = input()[0:8], input()[0:8], input()[0:8], input()[0:8], input()[0:8], input()[0:8], input()[0:8], input()[0:8]

BOARD = []

for i in vline:
    BOARD.append({k: v for k, v in zip(range(len(i)), i)})

position_lst = [i for i in range(8)]
rposition_lst = position_lst.copy()
rposition_lst.reverse()

for l, d in enumerate(BOARD):
    for k, v in d.items():
        if v == 'R':

            left = position_lst[:k]
            right = position_lst[k + 1:]
            top = position_lst[:l]
            bottom = position_lst[l + 1:]

            left.reverse()
            top.reverse()

            if len(left) != 0:
                for q in left:
                    if d[q] == 'R' or d[q] == 'B':
                        break
                    else:
                        d[q] = '■'

            if len(right) != 0:
                for q in right:
                    if d[q] == 'R' or d[q] == 'B':
                        break
                    else:
                        d[q] = '■'

            if len(top) != 0:
                for q in top:
                    if BOARD[q][k] == 'R' or BOARD[q][k] == 'B':
                        break
                    else:
                        BOARD[q][k] = '■'

            if len(bottom) != 0:
                for q in bottom:
                    if BOARD[q][k] == 'R' or BOARD[q][k] == 'B':
                        break
                    else:
                        BOARD[q][k] = '■'

        if v == 'B':

            lefttop = []
            leftbottom = []
            righttop = []
            rightbottom = []

            if k != 0 and l != 0:
                lefttop = [[z, x] for z, x in zip(rposition_lst[-l:], rposition_lst[-k:])]

            if k != 0:
                leftbottom = [[z, x] for z, x in zip(position_lst[l + 1:], rposition_lst[-k:])]

            if l != 0:
                righttop = [[z, x] for z, x in zip(rposition_lst[-l:], position_lst[k + 1:])]

            rightbottom = [[z, x] for z, x in zip(position_lst[l + 1:], position_lst[k + 1:])]

            if len(lefttop) != 0:
                for q in lefttop:
                    if BOARD[q[0]][q[1]] == 'R' or BOARD[q[0]][q[1]] == 'B':
                        break
                    else:
                        BOARD[q[0]][q[1]] = '■'

            if len(leftbottom) != 0:
                for q in leftbottom:
                    if BOARD[q[0]][q[1]] == 'R' or BOARD[q[0]][q[1]] == 'B':
                        break
                    else:
                        BOARD[q[0]][q[1]] = '■'

            if len(righttop) != 0:
                for q in righttop:
                    if BOARD[q[0]][q[1]] == 'R' or BOARD[q[0]][q[1]] == 'B':
                        break
                    else:
                        BOARD[q[0]][q[1]] = '■'

            if len(rightbottom) != 0:
                for q in rightbottom:
                    if BOARD[q[0]][q[1]] == 'R' or BOARD[q[0]][q[1]] == 'B':
                        break
                    else:
                        BOARD[q[0]][q[1]] = '■'

empty_cells = 0

for d in BOARD:
    for k, v in d.items():
        if v == '*':
            empty_cells += 1

print(empty_cells)
