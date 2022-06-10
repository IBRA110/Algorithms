"""
Поиск кратчайшего расстояния
Требование: положительные веса
Цель: Поиск кратчайшего пути от одной точки до другой
"""


from collections import deque

def main():
    G = read_graph()
    start = input('С какой вершины начать? ')
    while start not in G:
        start = input('Такой вершины в графе нет. С какой вершины начать? ')
    shortest_distances = dijkstra(G, start)
    finish = input('К какой вершине построить путь? ')
    while finish not in G:
        finish = input('Такой вершины в графе нет. К какой вершине построить путь? ')
    shortest_path = reveal_shortest_path(G, start, finish, shortest_distances)


def read_graph():
    M = int(input()) # Количество рёбер, далее - строки "А Б вес"
    G = {}
    for i in range(M):
        a, b, weight = input().split()
        weigt = float(weight)
        add_edge(G, a, b, weigt)
        add_edge(G, b, a, weigt)
    return G

def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight


def dijkstra(G, start):
    Q = deque()
    s = {}
    s[start] = 0
    Q.append(start)
    while Q:
        v = Q.pop()
        for u in G[v]:
            if u not in s or s[v] + G[v][u] < s[u]:
                s[u] = s[v] + G[v][u]
                Q.append(u)
    return s

def reveal_shortest_path(G, start, end, S):     # S - словарь кратчайших расстояний до всех вершин графа, возвращаемый из функции gejkstra()
    Q = deque()
    v = end
    Q.append(v)                                # Добавляем в очередь последнюю вершину.
    while v is not start:                      # Пока текущая вершина не является стартовой,
        for n in G[v]:                         # вычисляем для каждой из её соседей,
            if S[v] == S[n] + G[v][n]:         # совпадает ли сумма (кратч.расст. соседки + величина
                Q.appendleft(n)                # ребра) с кратч.расст. текущей вершины. Если да, то
                v = n                          # соседка принадлежит одному из кратч.путей.
                break                          # Все кратч.пути искать не нужно, поэтому выходим из цикла
    return Q                                    # и продолжаем операции уже с соседней вершиной.




if __name__ == '__main__':
    main()