"""
Дан массив из N целых чисел.
Нужно уметь отвечать на запросы вида “Cколько чисел имеют значения от L до R?”.

Формат ввода
Число N. Далее N целых чисел. Затем число запросов K. Далее K пар чисел L, R  — собственно запросы.

Формат вывода
Выведите K чисел — ответы на запросы.

Пример
5
10 1 10 3 4
4
1 10
2 9
3 4
2 2

5 2 2 0
"""

print('---------answer----------')

from bisect import bisect_left, bisect_right
from collections import Counter

n = int(input())
array = list(map(int, input().split()))
array.sort()

counter = Counter(array)

k = int(input())
answer = []

for _ in range(k):
    l, r = map(int, input().split())
    left_index = bisect_left(array, l)
    right_index = bisect_right(array, r)
    count = right_index - left_index
    answer.append(count)

print(*answer)

print('---------yandex----------')


def binsearch(a, val):
    l = 0
    r = len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] >= val:
            r = m
        else:
            l = m + 1
    return l


n = int(input())
a = list(map(int, input().split()))
a.sort()
a.append(10 ** 9 + 1)
k = int(input())
ans = []
for i in range(k):
    mn, mx = map(int, input().split())
    posmn = binsearch(a, mn)
    posmx = binsearch(a, mx + 1)
    ans.append(posmx - posmn)
print(*ans)
