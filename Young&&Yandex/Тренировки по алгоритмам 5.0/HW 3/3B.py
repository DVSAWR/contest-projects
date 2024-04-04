"""
Задано две строки, нужно проверить, является ли одна анаграммой другой. Анаграммой называется строка,
полученная из другой перестановкой букв.

Формат ввода
Строки состоят из строчных латинских букв, их длина не превосходит 100000. Каждая записана в отдельной строке.

Формат вывода
Выведите "YES" если одна из строк является анаграммой другой и "NO" в противном случае.

Пример 1
dusty
study

YES

Пример 2
rat
bat

NO
"""

print('---------answer----------')

first, second = input(), input()
if sorted(list(first)) == sorted(list(second)):
    print('YES')
else:
    print('NO')

# dusty
# study
# rat
# bat
# zirkanrlepcmvyjbpgpizexomgzmymouadzywuitkhicnqtrszvrwukcvoknymyiqfdvkdubisfvzidwplywyzjssymazynkubqv
# lcegwwmrebgvtbggnztiaayfatbpiphwwwlkhdahnsxnafiglugnukuxhjxguywtizxbsfqjedtzovtyxbhyzzhzmyrzeydpfosv

print('---------yandex----------')


def make_counter(s):
    ans = {}
    for c in s:
        ans[c] = ans.get(c, 0) + 1
    return ans


dct1 = make_counter(input())
dct2 = make_counter(input())
flag = True

for char in dct1:
    if not (char in dct2 and dct1[char] == dct2[char]):
        flag = False
if len(dct1) == len(dct2) and flag:
    print('YES')
else:
    print('NO')
