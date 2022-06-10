"""
Максимум в скользящем окне
Найти максимум в каждом окне размераmданного массива чиселA[1. . . n].
Вход.
Массив чиселA[1. . . n]и число1≤m≤n.
Выход.
Максимум подмассиваA[i . . . i+m−1]для всех1≤i≤n−m+ 1.25627481
Наивный  способ  решитьданную задачу — честно про-сканировать каждое окнои 
найти в нём максимум. Время работы  такого  алгоритма  —O(nm). 
Ваша задача — реализовать алгоритм со временем работы O(n).
Формат входа.
Первая строка входа содержит числоn, вторая — мас-сивA[1. . . n], третья — число m.
Формат выхода.
n − m + 1 максимумов, разделённых пробелами.
Ограничения.1≤n≤105,1≤m≤n,0≤A[i]≤105для всех1≤i≤n.


Sample Input 1:
3
2 1 5
1

Sample Output 1:
2 1 5

Sample Input 2:
8
2 7 3 1 5 2 6 2
4

Sample Output 2:
7 7 5 6 6
"""

# Решение

from collections import deque

def main(l, n, wind):
    max_wind = deque()
    for i in range(wind):
        while max_wind and l[i] >= l[max_wind[-1]]:
            max_wind.pop()
        max_wind.append(i)
    for i in range(wind, n):
        print(str(l[max_wind[0]]) + " ", end = "")
        while max_wind and max_wind[0] <= i - wind:
            max_wind.popleft() 
        while max_wind and l[i] >= l[max_wind[-1]] :
            max_wind.pop()
        max_wind.append(i)
    print(str(l[max_wind[0]]))


if __name__=="__main__":
    n = int(input())
    l = [int(i) for i in input().split()]
    wind = int(input())
    main(l, n, wind)