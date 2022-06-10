def lis_bottom_up(A, n):
    D, prev =  [0] * (n), [0] * (n)
    for i in range(n):
        D[i], prev[i] = 1, -1
        for j in range(i):
            if A[i] > A[j] and D[j] + 1 > D[i]:
                D[i], prev[i] = D[j] + 1, j
    ans, k = max(D), 1
    L = [0] * ans
    j = ans - 1
    for i in range(2, n):
        if D[i] > D[k]:
            k = i
    while k > 0:
        L[j] = k + 1
        j = j - 1
        k = prev[k]
    return L

"""
Задача на программирование: наибольшая последовательнократная подпоследовательность

Дано целое число 1≤n≤103 1 \le n \le 10^3 1≤n≤103 и массив A[1…n] A[1\ldots n] A[1…n] 
натуральных чисел, не превосходящих 2⋅109 2 \cdot 10^9 2⋅109. 
Выведите максимальное 1≤k≤n 1 \le k \le n 1≤k≤n, для которого найдётся 
подпоследовательность 1≤i1<i2<…<ik≤n 1 \le i_1 \lt i_2 \lt \ldots \lt i_k \le n 
1≤i1​<i2​<…<ik​≤n длины k k k, в которой каждый элемент делится на предыдущий 
(формально: для  всех 1≤j<k 1 \le j \lt k 1≤j<k, A[ij] ∣ A[ij+1] A[i_j]\, | \,A[i_{j+1}] A[ij​]∣A[ij+1​]).

Sample Input:
4
3 6 7 12

Sample Output:
3
"""

# Решение

def lis_bottom_up_module(A, n):
    D =  [0] * (n)
    for i in range(n):
        D[i] = 1
        for j in range(i):
            if A[i] % A[j] == 0 and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    return max(D)

"""
Задача на программирование повышенной сложности: 
наибольшая невозрастающая подпоследовательность

Дано целое число 1≤n≤105 1 \le n \le 10^5 1≤n≤105и массив A[1…n] A[1 \ldots n] A[1…n], 
содержащий неотрицательные целые числа, не превосходящие 109 10^9 109. Найдите 
наибольшую невозрастающую подпоследовательность в A A A. В первой строке выведите 
её длину k k k, во второй — её индексы 1≤i1<i2<…<ik≤n 1\le i_1 \lt i_2\lt \ldots 
\lt i_k \le n 1≤i1​<i2​<…<ik​≤n (таким образом, A[i1]≥A[i2]≥…≥A[in] A[i_1] \ge A[i_2] 
\ge \ldots \ge A[i_n] A[i1​]≥A[i2​]≥…≥A[in​]).

Sample Input:
5
5 3 4 4 2

Sample Output:
4
1 3 4 5 
"""

# Решение

def lis_bottom_down(A, n):
    prev = []
    INF = 10 ** 10
    F = [-INF] * (len(A) + 1)
    F[0] = INF
    for i in range(len(A)):
        left = 0
        right = len(A)
        while right - left > 1:
            middle = (left + right) // 2
            if F[middle] < A[i]:
                right = middle
            else: 
                left = middle 
        F[right] = A[i]
        prev.append([right, i, A[i]])
    x = 0
    j = len(prev) - 1
    for i in F:
        if i != INF and i != -INF:
            x += 1
    D = []
    for i in range(len(prev) - 1, -1, -1):
        if x == prev[i][0]:
            D.append(prev[i][1] + 1)
            x -= 1
    print(len(D))
    for i in D[::-1]:
        print(i, end=' ')


def main():
    n = int(input())
    lis = [int(i) for i in input().split()]
    assert len(lis) == n
    return lis_bottom_up(lis, n), lis_bottom_up_module(lis, n), lis_bottom_down(lis, n)

if __name__ == '__main__':
    print(main())