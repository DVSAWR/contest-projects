"""
Вам даны три списка чисел. Найдите все числа, которые встречаются хотя бы в двух из трёх списков.

Формат ввода
Во входных данных описывается три списка чисел. Первая строка каждого описания списка состоит из длины
списка n (1 ≤ n ≤ 1000). Вторая строка описания содержит список натуральных чисел, записанных через пробел.

Формат вывода
Выведите все числа, которые содержатся хотя бы в двух списках из трёх, в порядке возрастания. Обратите внимание,
что каждое число необходимо выводить только один раз.

Пример 1
2
3 1
2
1 3
2
1 2

1 3
"""

print('---------answer----------')

n1 = int(input())
set1 = set(map(int, input().split()))
n2 = int(input())
set2 = set(map(int, input().split()))
n3 = int(input())
set3 = set(map(int, input().split()))

sets = [set1, set2, set3]
d = {}

for i in sets:
    for j in i:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1

answer = []

for k, v in d.items():
    if v >= 2:
        answer.append(k)

print(*sorted(answer))

print('---------yandex----------')

l1 = int(input())
s1 = set(map(int, input().split()))
l2 = int(input())
s2 = set(map(int, input().split()))
l3 = int(input())
s3 = set(map(int, input().split()))
ans = s1 & s2
merged12 = s1.union(s2)
ans = ans.union(merged12 & s3)
print(*sorted(ans))
