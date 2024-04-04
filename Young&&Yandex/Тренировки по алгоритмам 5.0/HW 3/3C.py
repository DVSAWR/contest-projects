"""
Дан массив a из n чисел. Найдите минимальное количество чисел, после удаления которых попарная разность оставшихся
чисел по модулю не будет превышать 1, то есть после удаления ни одно число не должно отличаться от какого-либо
другого более чем на 1.

Формат ввода
Первая строка содержит одно целое число n — количество элементов массива a
Вторая строка содержит n целых чисел a1, a2, …, an — элементы массива a.

Формат вывода
Выведите одно число — ответ на задачу.

Пример 1
5
1 2 3 4 5

3

Пример 2
10
1 1 2 3 5 5 2 2 1 5

4
"""

print('---------answer----------')

n = int(input())
a = list(map(int, input().split()))
d = {}

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

nums = sorted(d.keys())
n_nums = len(nums)
answer = 0

if n_nums < 2:
    print(0)
else:
    for i in range(len(nums) - 1):
        if abs(nums[i] - nums[i + 1]) <= 1:
            answer = max(d[nums[i]] + d[nums[i + 1]], answer)
            print(max(d[nums[i]] + d[nums[i + 1]], answer))
    print('\nANSWER:')
    print(n - answer)

# n = 10
# a = [1, 1, 2, 3, 5, 5, 2, 2, 1, 5]

# n = 5
# a = [1, 2, 3, 4, 5]

# n = 10
# a = [1, 1, 2, 2, 2, 1, 2, 2, 1, 3]

# n = 1
# a = [33292]

print('---------yandex----------')

n = int(input())
a = list(map(int, input().split()))
cnt = {}

for now in a:
    cnt[now] = cnt.get(now, 0) + 1
ans = 0
for key in cnt:
    now = cnt[key] + max(cnt.get(key - 1, 0), cnt.get(key + 1, 0))
    ans = max(ans, now)
print(n - ans)
