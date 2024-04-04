"""
Из шахматной доски по границам клеток выпилили связную (не распадающуюся на части) фигуру без дыр.
Требуется определить ее периметр.

Формат ввода
Сначала вводится число N (1 ≤ N ≤ 64) – количество выпиленных клеток. В следующих N строках вводятся координаты
выпиленных клеток, разделенные пробелом (номер строки и столбца – числа от 1 до 8). Каждая выпиленная
клетка указывается один раз.

Формат вывода
Выведите одно число – периметр выпиленной фигуры (сторона клетки равна единице).

Пример 1
3
1 1
1 2
2 1

8

Пример 2
1
8 8

4
"""

print('---------answer----------')

n = int(input())
coords = []
for i in range(n):
    coords.append(tuple(map(int, input().split())))

board = []
line_board = 'o ' * 8
for i in range(8):
    board.append(line_board.split())

for i in coords:
    board[i[1] - 1][i[0] - 1] = 4

for line in range(8):
    for cell in range(8):
        if cell != 7 and type(board[line][cell]) == int and type(board[line][cell + 1]) == int:  # RIGHT
            board[line][cell] -= 1
            board[line][cell + 1] -= 1
        if line != 7 and type(board[line][cell]) == int and type(board[line + 1][cell]) == int:  # TOP
            board[line][cell] -= 1
            board[line + 1][cell] -= 1

cells_count = 0
for line in board:
    for v in line:
        if type(v) == int:
            cells_count += v

print(cells_count)

print('---------yandex----------')

n = int(input())
field = [[0] * 10 for _ in range(10)]
for _ in range(n):
    i, j = map(int, input().split())
    field[i][j] = 1
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += field[i][j - 1] != field[i][j]
        ans += field[i - 1][j] != field[i][j]
print(ans)
