"""
Задача на программирование: расстояние редактирования
Вычислите расстояние редактирования двух данных непустых 
строк длины не более 102 10^2 102, содержащих строчные 
буквы латинского алфавита.

Sample Input 1:
ab
ab

Sample Output 1:
0

Sample Input 2:
short
ports

Sample Output 2:
3
"""

# Решение

def levenstein(A, B):
    F = [[(i + j) if i * j == 0 else 0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1]
            else:
                F[i][j] = min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1]) + 1
    return F[len(A)][len(B)]


def main():
    A = input()
    B = input()
    print(levenstein(A, B))

if __name__ == '__main__':
    main()
