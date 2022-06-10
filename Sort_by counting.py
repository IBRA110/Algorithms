"""
Первая строка содержит число 1≤n≤104 1 \le n \le 10^4 1≤n≤104, вторая — n n n натуральных чисел, не превышающих 10. 
Выведите упорядоченную по неубыванию последовательность этих чисел.
"""

# Решение

def sort_zahlen(a):
    lib_zahl = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for i in a:
        lib_zahl[i] += 1
    for i in lib_zahl:
        if lib_zahl[i] != 0:
            for j in range(lib_zahl[i]):
                print(i, end=' ')

def main():
    a = int(input())
    b = [int(i) for i in input().split()]
    assert len(b) == a
    sort_zahlen(b)
    
if __name__ == '__main__':
    main()