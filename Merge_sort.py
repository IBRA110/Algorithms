"""

Задача на программирование: число инверсий
Первая строка содержит число 1≤n≤105 1 \le n \le 10^5 1≤n≤105, 
вторая — массив A[1…n] A[1\ldots n] A[1…n], 
содержащий натуральные числа, 
не превосходящие 109 10^9 109. Необходимо посчитать 
число пар индексов 1≤i<j≤n 1 \le i \lt j \le n 1≤i<j≤n, 
для которых A[i]>A[j] A[i] \gt A[j] A[i]>A[j]. 
(Такая пара элементов называется инверсией массива. 
Количество инверсий в массиве является в некотором 
смысле его мерой неупорядоченности: например, в упорядоченном по 
неубыванию массиве инверсий нет вообще, а в массиве, 
упорядоченном по убыванию, инверсию образуют каждые два элемента.)

Sample Input:
5
2 3 9 2 9

Sample Output:
2
"""

# Решение

g = 0
def merge(A, B):
    global g
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    len_A, len_B = len(A), len(B)
    while i < len_A and k < len_B:
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            g += len_A - i
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C

def number_of_inversions(m_list):
    if len(m_list) <= 1:
        return
    middle = len(m_list) // 2
    left = [m_list[i] for i in range(middle)]
    right = [m_list[i] for i in range(middle, len(m_list))]
    number_of_inversions(left)
    number_of_inversions(right)
    C = merge(left, right)
    for i in range(len(m_list)):
        m_list[i] = C[i]
    return m_list

def main():
    n = int(input())
    m_list = [int(i) for i in input().split()]
    assert n == len(m_list)
    number = number_of_inversions(m_list)
    print(g)

if __name__ == '__main__':
    main()