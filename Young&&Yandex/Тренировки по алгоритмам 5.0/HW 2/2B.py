"""
Вася решил заняться торговлей рыбой. С помощью методов машинного обучения он предсказал цены на рыбу на N дней вперёд.
Он решил, что в один день он купит рыбу, а в один из следующих дней — продаст (то есть совершит или ровно одну покупку
и продажу или вообще не совершит покупок и продаж, если это не принесёт ему прибыли). К сожалению, рыба — товар
скоропортящийся и разница между номером дня продажи и номером дня покупки не должна превышать K.
Определите, какую максимальную прибыль получит Вася.

Формат ввода
В первой строке входных данных задаются числа N и K (1 ≤ N ≤ 10000, 1 ≤ K ≤ 100).
Во второй строке задаются цены на рыбу в каждый из N дней. Цена — целое число, которое
может находится в пределах от 1 до 10**9.

Формат вывода
Выведите одно число — максимальную прибыль, которую получит Вася.

Пример 1
5 2
1 2 3 4 5

2

Пример 2
5 2
5 4 3 2 1

0
"""

print('---------answer----------')

n, k = map(int, input().split())
prices = list(map(int, input().split()))

prices.reverse()

value = 0
max_value = 0

for i in range(n):
    price_slice = prices[i:i + k + 1]
    right_price = max(price_slice)
    right_price_index = price_slice.index(right_price)
    left_price = min(price_slice[right_price_index:])

    value = right_price - left_price

    if value > max_value:
        max_value = value

print(max_value)

print('---------yandex----------')

n, k = map(int, input().split())
a = list(map(int, input().split()))
maxinc = 0
for i in range(n):
    for j in range(k + 1):
        if i + j < n:
            maxinc = max(maxinc, a[i + j] - a[i])

print(maxinc)
