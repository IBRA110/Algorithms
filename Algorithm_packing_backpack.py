"""
Задача на программирование: рюкзак
Первая строка входа содержит целые числа 
1≤W≤104 1 \le W \le 10^4 1≤W≤104 и 1≤n≤300 1 \le n \le 300 1≤n≤300
 — вместимость рюкзака и число золотых слитков. 
Следующая строка содержит n n n целых чисел 
0≤w1,…,wn≤105 0 \le w_1, \ldots, w_n \le 10^5 0≤w1​,…,wn​≤105, 
задающих веса слитков. Найдите максимальный вес золота, 
который можно унести в рюкзаке.

Sample Input:
10 3
1 4 8

Sample Output:
9
"""

# Решение

def kapsnack(w, m):
    F = [1] + [0] * w
    for j in range(len(m)):
        for i in range(w, m[j] - 1, - 1):
            if F[i - m[j]] == 1:
                F[i] = 1
    i = w
    while F[i] == 0:
        i -= 1
    return i


def main():
    w, n = map(int, input().split())
    m = [int(i) for i in input().split()]
    assert len(m) == n
    print(kapsnack(w, m))

if __name__ == '__main__':
    main()
