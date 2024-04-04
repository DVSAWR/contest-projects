"""
С целью экономии чернил в картридже принтера было принято решение укоротить некоторые слова в тексте.
Для этого был составлен словарь слов, до которых можно сокращать более длинные слова. Слово из текста можно
сократить, если в словаре найдется слово, являющееся началом слова из текста. Например, если в списке есть
слово "лом", то слова из текста "ломбард", "ломоносов" и другие слова, начинающиеся на "лом", можно сократить до "лом".

Если слово из текста можно сократить до нескольких слов из словаря, то следует сокращать его до самого короткого слова.

Формат ввода
В первой строке через пробел вводятся слова из словаря, слова состоят из маленьких латинских букв.
Гарантируется, что словарь не пуст и количество слов в словаре не превышет 1000, а длина слов — 100 символов.

Во второй строке через пробел вводятся слова текста (они также состоят только из маленьких латинских букв).

Формат вывода
Выведите текст, в котором осуществлены замены.

Пример 1
a b
abdafb basrt casds dsasa a

a b casds dsasa a

Пример 2
aa bc aaa
a aa aaa bcd abcd

a aa aa bc abcd
"""

print('---------answer----------')

from collections import defaultdict

reduct_dict = input().split()
text = input().split()
answer = []


def def_dict():
    return defaultdict(def_dict)


reduct_def_dict = def_dict()
sub = ''

for reduction in reduct_dict:
    subd = reduct_def_dict
    for symbol in reduction:
        subd = subd[symbol]
    subd[sub] = reduction

for word in text:
    subd = reduct_def_dict
    found = False

    for symbol in word:
        if symbol not in subd:
            answer.append(word)
            found = True
            break

        subd = subd[symbol]

        if sub in subd:
            answer.append(subd[sub])
            found = True
            break

    if not found:
        answer.append(word)

print(*answer)

# a b
# abdafb basrt casds dsasa a
# a b casds dsasa a

# aa bc aaa
# a aa aaa bcd abcd
# a aa aa bc abcd

print('---------yandex----------')

dictset = set(input().split())
ans = []
for word in input().split():
    for i in range(1, min(101, len(word))):
        part = word[:i]
        if part in dictset:
            ans.append(part)
            break
    else:
        ans.append(word)
print(' '.join(ans))
