"""
В первой строке даны целое число 1≤n≤105 1 \le n \le 10^5 1≤n≤105
и массив A[1…n] A[1 \ldots n] A[1…n] из n n n различных натуральных чисел, 
не превышающих 109 10^9 109, в порядке возрастания, 
во второй — целое число 1≤k≤105 1 \le k \le 10^5 1≤k≤105 и k k k
натуральных чисел b1,…,bk b_1, \ldots, b_k b1​,…,bk​, 
не превышающих 109 10^9 109. 
Для каждого i i i от 1 до k k k 
необходимо вывести индекс 1≤j≤n 1 \le j \le n 1≤j≤n,
для которого A[j]=bi A[j]=b_i A[j]=bi​, или −1 -1 −1, если такого j j j нет.

Sample Input:
5 1 5 8 12 13
5 8 1 23 1 11

Sample Output:
3 1 -1 1 -1
"""

# Решение

def binary_search(sort_list, k):
    left = 0
    right = len(sort_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if sort_list[middle] == k:
            return middle + 1
        elif sort_list[middle] > k:
            right = middle - 1
        else:
            left = middle + 1
    return -1

def main():
    n, *a = map(int, input().split())
    assert n == len(a)
    a = sorted(a)
    m, *b = map(int, input().split())
    assert m == len(b)
    for i in b:
        print(binary_search(a, i), end=' ')




if __name__ == '__main__':
    main()