"""
В первой строке задано два целых числа 1≤n≤50000 1 \le n \le 50000 1≤n≤50000 и 1≤m≤50000 
1 \le m \le 50000 1≤m≤50000 — количество отрезков и точек на прямой, соответственно. 
Следующие n n n строк содержат по два целых числа ai a_i ai​ и bi b_i bi​ (ai≤bi a_i \le b_i ai​≤bi​) — 
координаты концов отрезков. Последняя строка содержит m m m целых чисел — координаты точек. 
Все координаты не превышают 108 10^8 108 по модулю. Точка считается принадлежащей отрезку, 
если она находится внутри него или на границе. Для каждой точки в порядке появления во 
вводе выведите, скольким отрезкам она принадлежит.

Sample Input:
2 3
0 5
7 10
1 6 11

Sample Output:
1 0 0
"""


# Решение

import random 

def hoar(sektion):
    if len(sektion) <= 1:
        return
    barrier = random.choice(sektion)
    left, middle, right = [], [], []
    for i in sektion:
        if i < barrier:
            left.append(i)
        elif i == barrier:
            middle.append(i)
        else:
            right.append(i)
    hoar(left)
    hoar(right)
    k = 0
    for i in left + middle + right:
        sektion[k] = i
        k += 1
    return sektion

def binary_search_right(sort_list, key):
    left = - 1
    right = len(sort_list)
    while right - left > 1:
        middle = (left + right) // 2
        if sort_list[middle] <= key:
            left = middle
        else:
            right = middle
    return left + 1

def binary_search_left(sort_list, key):
    left = - 1
    right = len(sort_list)
    while right - left > 1:
        middle = (left + right) // 2
        if sort_list[middle] < key:
            left = middle
        else:
            right = middle
    return right + 1
    
def main():
    start, end, = [], []
    n, m = map(int, input().split())
    for i in range(n):
        startIn, endIn = map(int,input().split())
        start.append(startIn)
        end.append(endIn)
    points = [int(i) for i in input().split()]
    assert len(points) == m
    point = set(points)
    start += point
    end += point
    hoar(start)
    hoar(end)
    for i in points:
        print(binary_search_right(start, i)- binary_search_left(end, i), end=' ')
    
        

if __name__ == '__main__':
    main()