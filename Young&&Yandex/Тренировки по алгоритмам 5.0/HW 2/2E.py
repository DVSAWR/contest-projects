"""
Домашний питомец мальчика Васи — улитка Петя. Петя обитает на бесконечном в обе стороны вертикальном столбе,
который для удобства можно представить как числовую прямую. Изначально Петя находится в точке 0.
Вася кормит Петю ягодами. У него есть n ягод, каждая в единственном экземпляре. Вася знает, что если утром он
даст Пете ягоду с номером i, то поев и набравшись сил, за остаток дня Петя поднимется на ai единиц вверх по столбу,
но при этом за ночь, потяжелев, съедет на bi единиц вниз. Параметры различных ягод могут совпадать.
Пете стало интересно, а как оно там, наверху, и Вася взялся ему в этом помочь. Ближайшие n дней он будет кормить
Петю ягодами из своего запаса таким образом, чтобы максимальная высота, на которой побывал Петя за эти n дней была
максимальной. К сожалению, Вася не умеет программировать, поэтому он попросил вас о помощи. Найдите, максимальную
высоту, на которой Петя сможет побывать за эти n дней и в каком порядке Вася должен давать Пете ягоды,
чтобы Петя смог её достичь!

Формат ввода
В первой строке входных данных дано число n (1≤n) — количество ягод у Васи. В последующих n строках описываются
параметры каждой ягоды. В i+1 строке дано два числа ai и bi — то, насколько поднимется улитка за день
после того, как съест i ягоду и насколько  опуститься за ночь.

Формат вывода
В первой строке выходных данных выведите единственное число — максимальную высоту, которую сможет достичь Петя,
если Вася будет его кормить оптимальным образом. В следующей строке выведите n различных целых
чисел от 1 до n — порядок, в котором Вася должен кормить Петю (i число в строке соответствует номеру ягоды,
которую Вася должен дать Пете в i день чтобы Петя смог достичь максимальной высоты).

Пример 1
3
1 5
8 2
4 4
10

2 3 1

Пример 2
2
7 6
7 4
10

2 1
"""

print('---------answer----------')

n = int(input())

left = []
right = []
nleft = 0
nright = 0

for i in range(n):
    position = i + 1
    b, d = map(int, input().split())
    value = b - d
    if value > 0:
        left.append((position, b, d, value))
        nleft += 1
    else:
        right.append((position, b, d, value))
        nright += 1

sorted_left = sorted(left, key=lambda item: item[2])
sorted_right = sorted(right, key=lambda item: item[1], reverse=True)

maximum_position = 0
current_position = 0
berry_seq = []

for i in range(nleft):
    current_position += sorted_left[i][1]
    if current_position > maximum_position:
        maximum_position = current_position
    current_position -= sorted_left[i][2]
    berry_seq.append(sorted_left[i][0])

if nright != 0:
    if maximum_position < current_position + sorted_right[0][1]:
        maximum_position = current_position + sorted_right[0][1]
    for i in sorted_right:
        berry_seq.append(i[0])

print(maximum_position)
print(' '.join(map(str, berry_seq)))

print('---------yandex----------')

n = int(input())
maxgoodi = -1
maxbadi = -1
a = []
b = []
used = [False] * (n + 1)
for i in range(n):
    ta, tb = map(int, input().split())
    a.append(ta)
    b.append(tb)
    if ta >= tb and (maxgoodi == -1 or tb > b[maxgoodi]):
        maxgoodi = i
    if ta < tb and (maxbadi == -1 or ta > a[maxbadi]):
        maxbadi = i
ans = []
maxh = 0
for i in range(n):
    if a[i] > b[i] and i != maxgoodi:
        ans.append(i + 1)
        used[i + 1] = True
        maxh += a[i] - b[i]
if maxgoodi != -1 and (maxbadi != -1 and a[maxgoodi] > a[maxgoodi] - b[maxgoodi] + a[maxbadi]) or (maxbadi == -1):
    maxh += a[maxgoodi]
    ans.append(maxgoodi + 1)
    used[maxgoodi + 1] = True
else:
    if maxbadi != -1:
        if maxgoodi != -1:
            maxh += a[maxgoodi] - b[maxgoodi]
            ans.append(maxgoodi + 1)
            used[maxgoodi + 1] = True
        maxh += a[maxbadi]
        ans.append(maxbadi + 1)
        used[maxbadi + 1] = True
print(maxh)
for i in range(1, n + 1):
    if not used[i]:
        ans.append(i)
print(*ans)
