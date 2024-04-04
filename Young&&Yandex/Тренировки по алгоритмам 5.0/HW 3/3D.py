"""
Вам дана последовательность измерений некоторой величины. Требуется определить, повторялась ли какое-либо число,
причём расстояние между повторами не превосходило k.

Формат ввода
В первой строке задаются два числа n и k.

Во второй строке задаются n чисел, по модулю.

Формат вывода
Выведите 'YES', если найдется повторяющееся число и расстояние между повторами не превосходит k и 'NO'
в противном случае.

Пример 1
4 2
1 2 3 1

NO

Пример 2
4 1
1 0 1 1

YES

Пример 3
6 2
1 2 3 1 2 3

NO
"""

print('---------answer----------')

n, k = map(int, input().split())
lst = list(map(int, input().split()))

answer = False
d = {}

if n > 1 and lst[0] == lst[1]:
    answer = True
else:
    for i, v in enumerate(lst):
        if v in d:
            if i - d[v] <= k:
                answer = True
                break
        d[v] = i

if answer:
    print('YES')
else:
    print('NO')

# n, k = 4, 2
# lst = [1, 2, 3, 1]
# NO

# n, k = 4, 1
# lst = [1, 0, 1, 1]
# YES

# 6 2
# 1 2 3 1 2 3
# NO

print('---------yandex----------')


def sol(nums, k):
    lastk = set()
    for i in range(len(nums)):
        if nums[i] in lastk:
            return True
        lastk.add(nums[i])
        if i >= k:
            lastk.remove(nums[i - k])
    return False


n, k = map(int, input().split())
nums = list(map(int, input().split()))

if sol(nums, k):
    print('YES')
else:
    print('NO')
