"""
Задача на программирование: лестница
Даны число 1≤n≤102 1 \le n \le 10^2 1≤n≤102 
ступенек лестницы и целые числа 
−104≤a1,…,an≤104 -10^4 \le a_1, \ldots, a_n \le 10^4 −104≤a1​,…,an​≤104, 
которыми помечены ступеньки. Найдите максимальную сумму, 
которую можно получить, идя по лестнице снизу вверх 
(от нулевой до n n n-й ступеньки), 
каждый раз поднимаясь на одну или две ступеньки.

Sample Input 1:
2
1 2

Sample Output 1:
3

Sample Input 2:
2
2 -1

Sample Output 2:
1

Sample Input 3:
3
-1 2 1

Sample Output 3:
3
"""

def stairs(m, n):
    st = [0 for i in range(n + 1)]
    st[1] = m[0]
    for i in range(1, n):
        st[i + 1] = max(st[i - 1], st[i]) + m[i]
    return st[-1]


def main():
    n = int(input())
    m = [int(i) for i in input().split()]
    assert n == len(m)
    print(stairs(m, n))

if __name__ == '__main__':
    main()