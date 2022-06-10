"""
Автоматический анализ программ
При автоматическом анализе программ возникает такая задача.
Система равенств и неравенств
Проверить, можно ли присвоить переменным целые значения, чтобы выполнить заданные 
равенства вида xi = xj и неравенства вида xp 6 = xq.
Вход.
Число переменных n, а также список равенств вида xi = xj и неравенства вида xp 6 = xq.
Выход.
Проверить, выполнима ли данная система.
Формат входа.
Первая строка содержит числа n, e, d. Каждая из сле-дующих e строк содержит два 
числа i и j и задаёт равенство xi = xj. Каждая из следующих d строк содержит два 
числа i и j изадаёт неравенство xi 6 = xj. 
Переменные индексируются с 1:x1, . . . , xn.
Формат выхода.
Выведите1, если переменнымx1, . . . , x n можно присвоить целые значения, 
чтобы все равенства и неравенства выполнились. 
В противном случае выведите 0.
Ограничения.1≤n≤105;0≤e, d;e+d≤2·105;1≤i, j≤n.

Sample Input 1:
4 6 0
1 2
1 3
1 4
2 3
2 4
3 4

Sample Output 1:
1

Sample Input 2:
4 6 1
1 2
1 3
1 4
2 3
2 4
3 4
1 2

Sample Output 2:
0

Sample Input 3:
4 0 6
1 2
1 3
1 4
2 3
2 4
3 4

Sample Output 3:
1
"""

# Решение

class Disjointset():
    def __init__(self, i):
        self.i = i
        self.parent = self
        self.rank = 1

def find(i):
    if i is not i.parent:
        i.parent = find(i.parent)
    return i.parent

def union(i, j):
    di, dj = find(i), find(j)
    if di == dj:
        return
    if di.rank > dj.rank:
        dj.parent = di
    else:
        di.parent = dj
        if di.rank == dj.rank:
            dj.rank += 1

def main():
    n, e, d = map(int, input().split())
    s_e_t = [int(i) for i in range(n)]
    get_prog = 1
    for i in range(n):
        s_e_t[i] = Disjointset(s_e_t[i])
    for i in range(e):
        a, b = map(int, input().split())
        union(s_e_t[a - 1], s_e_t[b - 1])
    for i in range(d):
        a, b = map(int, input().split())
        if find(s_e_t[a - 1]) == find(s_e_t[b - 1]):
            get_prog = 0

    print(get_prog)


if __name__ == "__main__":
    main()