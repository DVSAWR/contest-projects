"""
На клетчатой плоскости закрашено K клеток. Требуется найти минимальный по площади прямоугольник,
со сторонами, параллельными линиям сетки, покрывающий все закрашенные клетки.

Формат ввода
Во входном файле, на первой строке, находится число K (1 ≤ K ≤ 100). На следующих K строках находятся
пары чисел Xi и Yi — координаты закрашенных клеток.

Формат вывода
Выведите в выходной файл координаты левого нижнего и правого верхнего углов прямоугольника.

Пример
4
1 3
3 1
3 5
6 3

1 1 6 5
"""

print('---------answer----------')

K = int(input())
coords = []

for i in range(K):
    coords.append(tuple(map(int, input().split())))

minx = coords[0][0]
miny = coords[0][1]
maxx = coords[0][0]
maxy = coords[0][1]

for i in coords:
    if i[0] < minx:
        minx = i[0]
    if i[0] > maxx:
        maxx = i[0]
    if i[1] < miny:
        miny = i[1]
    if i[1] > maxy:
        maxy = i[1]

# print(f'X Y MIN: {minx} {miny}\nX Y MAX: {maxx} {maxy}')
print(minx, miny, maxx, maxy)

print('---------yandex----------')

k = int(input())
minx, miny = map(int, input().split())
maxx, maxy = minx, miny
for i in range(k - 1):
    x, y = map(int, input().split())
    minx = min(minx, x)
    maxx = max(maxx, x)
    miny = min(miny, y)
    maxy = max(maxy, y)
print(minx, miny, maxx, maxy)
