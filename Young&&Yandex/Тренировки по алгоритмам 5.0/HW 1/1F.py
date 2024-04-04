"""
k друзей организовали стартап по производству укулеле для кошек. На сегодняшний день прибыль составила n рублей.
Вы, как главный бухгалтер компании, хотите в каждый из ближайших d дней приписывать по одной цифре в конец числа,
выражающего прибыль. При этом в каждый из дней прибыль должна делиться на k.

Формат ввода
В единственной строке входных данных через пробел записаны три числа: n, k, d — изначальная прибыль,
количество учредителей компании и количество дней, которое вы собираетесь следить за прибылью
(1≤n,k≤10**9, 1≤d≤10**5). НЕ гарантируется, что n делится на k.

Формат вывода
Выведите одно целое число x — прибыль компании через d дней. Первые цифры числа x должны совпадать с числом n.
Все префиксы числа x, которые длиннее числа n на 1, 2, …, d цифр, должны делиться на k. Если возможных ответов
несколько, выведите любой из них. Если ответа не существует, выведите −1.

Пример 1
21 108 1

216
"""

print('---------answer----------')

n = int(input())
nums = input()

d = list(map(int, nums.split()))
answer = ''
odd_count = d[0] % 2

for i in range(n - 1):
    if d[i] % 2 == 0:  # EVEN
        if d[i + 1] % 2 == 0:
            answer += 'x'
        if d[i + 1] % 2 != 0:
            answer += '+'
            odd_count += 1
    elif d[i] % 2 != 0:  # ODD
        if d[i + 1] % 2 == 0:
            answer += '+'
        if d[i + 1] % 2 != 0:
            answer += 'x'

if odd_count % 2 != 0:
    print(answer)
else:
    char_index = answer.find('+')
    final_answer = answer[:char_index] + 'x' + answer[char_index + 1:]
    print(final_answer)

print('---------yandex----------')

n = int(input())
nums = list(map(int, nums.split()))
state = 'no_odd_summand'
ans = []
for num in nums:
    if state == 'no_odd_summand':
        if num % 2 == 0:
            ans.append('+')
        else:
            state = 'last_odd'
    elif state == 'last_odd':
        if num % 2 == 0:
            ans.append('+')
            state = 'multiply_even'
        else:
            ans.append('x')
    elif state == 'multiply_even':
        ans.append('x')
print(''.join(ans))
