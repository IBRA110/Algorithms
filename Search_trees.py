"""
Обход двоичного дерева
Построить in-order, pre-order и post-order обходы данного двоичного де-рева.
Вход.
Двоичное дерево.
Выход.
Все его вершины в трёх разных порядках: in-order, pre-order и post-order.
In-order обход соответствует следующей рекурсивной процедуре,
получающей на вход корень v текущего поддерева: произвести рекурсивный вызов 
для v.left, напечатать v.key, произвести рекурсивный вызов для v.right. 
Pre-order обход: напечатать v.key, произвести рекурсивный вызов для v.left, 
произвести рекурсивный вызов для v.right. 
Post-order: произвести рекурсивный вызов для v.left, 
произве-сти рекурсивный вызов для v.right, напечатать v.key.
Формат входа.
Первая строка содержит число вершин n. 
Вершины дерева пронумерованы числами от 0 до n−1. Вершина 0 является корнем. 
Каждая из следующих n строк содержит информацию овершинах 0,1, . . . , n−1:
i-я строка задаёт числа key i, left i и right i,где key i — ключ вершины i,
left i — индекс левого сына вершины i, а right i— индекс правого сына вершины i. 
Если у вершины i нет одного или обоих сыновей, соответствующее значение равно −1.
Формат выхода.
Три строки: in-order, pre-order и post-order обходы.
Ограничения.
1≤n≤105;0≤keyi≤109;−1≤lefti,righti≤n−1.
Гарантируется, что вход задаёт корректное двоичное дерево: вчастности, 
если lefti = −1 и righti = −1, то lefti = righti; никакая вершина не является 
сыном двух вершин; каждая вершинаявляется потомком корня.

Sample Input:
10
0 7 2
10 -1 -1
20 -1 6
30 8 9
40 3 -1
50 -1 -1
60 1 -1
70 5 4
80 -1 -1
90 -1 -1

Sample Output:
50 70 80 30 90 40 0 20 10 60
0 70 50 40 30 80 90 20 60 10
50 80 90 30 40 70 10 60 20 0
"""

# Решение

class Tree:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def in_order(tree, x):
    if x.left == None and x.right == None:
        return
    in_order(tree, tree[x.left])
    print(x.key, end=" ")
    in_order(tree, tree[x.right])

def pre_order(tree, x):
    if x.left == None and x.right == None:
        return
    print(x.key, end=" ")
    pre_order(tree, tree[x.left])
    pre_order(tree, tree[x.right])

def post_order(tree, x):
    if x.left == None and x.right == None:
        return
    post_order(tree, tree[x.left])
    post_order(tree, tree[x.right])
    print(x.key, end=" ")

def main():
    n = int(input())
    t = []
    for i in range(n):
        a, b, c = map(int, input().split())
        x = Tree(a, b, c)
        t.append(x)
    x = Tree(-5, None, None)
    t.append(x)
    in_order(t, t[0])
    print()
    pre_order(t, t[0])
    print()
    post_order(t, t[0])
    print()

if __name__ == "__main__":
    main()


"""
Проверка свойства дерева поиска
Проверить, является ли данное двоичное дерево деревом поиска.
Вход.
Двоичное дерево.
Выход.
Проверить, является ли оно корректным деревом поиска: верно ли, 
что для любой вершины дерева её ключ больше всех ключей в левом поддереве 
данной вершины именьше всех ключей в правом поддереве.
Вы тестируете реализацию двоичного дерева поиска. 
У вас уже написан код, который ищет, добавляет и удаляет ключи, а также выводит 
внутреннее состояние структуры данных после каждой операции.
Вам осталось проверить, что в каждый момент дерево остаётся корректным деревом 
поиска. Другими словами, вы хотите проверить, что для дерева корректно работает 
поиск, если ключ есть в дереве,то процедура поиска его обязательно найдёт, 
если ключа нет — то ненайдёт.
Формат входа.
Первая строка содержит число вершин n. 
Вершины дерева пронумерованы числами от 0 до n−1. 
Вершина 0 является корнем. Каждая из следующихnстрок содержит информацию 
о вершинах 0,1, . . . , n−1:i-я строка задаёт числа keyi, lefti и righti,
где keyi — ключ вершиныi, lefti— индекс левого сына вершины i, а right i— 
индекс правого сына вершины i. 
Если у вершины i нет одного или обоих сыновей, соответствующее значениеравно−1.
Формат выхода.
Выведите «CORRECT», если дерево является корректным деревом поиска, 
и «INCORRECT» в противном случае.
Ограничения.
0≤n≤105;−231<keyi<231−1;−1≤lefti,righti≤n−1. 
Гарантируется, что вход задаёт корректное двоичное де-рево: в частности, 
если lefti6=−1 и righti6=−1, то lefti6=righti;
никакая вершина не является сыном двух вершин; 
каждая вершина является потомком корня.

Sample Input:
3
2 1 2
1 -1 -1
3 -1 -1

Sample Output:
CORRECT
"""

# Решение

import math

class Tree:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

def helper(t, root, min, max):
    if root.left != None and root.right != None:
        if min < root.key and root.key < max:
            return helper(t, t[root.left], min, root.key) and helper(t, t[root.right], root.key, max)
        return False
    return True

def main():
    n = int(input())
    t = []
    for i in range(n):
        a, b, c = map(int, input().split())
        x = Tree(a, b, c)
        t.append(x)
    x = Tree(-5, None, None)
    t.append(x)
    print("CORRECT" if helper(t, t[0], -math.inf, math.inf) else "INCORRECT")

if __name__ == "__main__":
    main()

"""
Проверка более общего свойства дерева поиска
Данная задача полностью аналогична предыдущей, 
но проверять теперь нужно более общее свойство. 
Дереву разрешается содержать равные ключи, но они всегда должны находиться 
в правом поддереве.
Формально, двоичное дерево называется деревом поиска, 
если длялюбой вершины её ключ больше всех ключей из её левого 
поддерева и не меньше всех ключей из правого поддерева.
Ограничения. 0≤n≤105;−231≤keyi≤231−1 (таким образом, в качестве ключей 
допустимы минимальное и максимальное значение 32-битного целого типа, 
будьте осторожны с переполне-нием);−1≤lefti,righti≤n−1. 
Гарантируется, что вход задаёт корректное двоичное дерево: 
в частности, если lefti =− 1 и righti =− 1, то lefti = righti; 
никакая вершина не является сыном двух вершин; 
каждая вершина является потомком корня.
"""

# Решение

import math

class Tree:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

def helper(t, root, min, max):
    if root.left != None and root.right != None:
        if min <= root.key and root.key < max:
            return helper(t, t[root.left], min, root.key) and helper(t, t[root.right], root.key, max)
        return False
    return True

def main():
    n = int(input())
    t = []
    for i in range(n):
        a, b, c = map(int, input().split())
        x = Tree(a, b, c)
        t.append(x)
    x = Tree(-5, None, None)
    t.append(x)
    print("CORRECT" if helper(t, t[0], -math.inf, math.inf) else "INCORRECT")

if __name__ == "__main__":
    main()