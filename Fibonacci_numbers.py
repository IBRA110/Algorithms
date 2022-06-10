"""
Задача на программирование: небольшое число Фибоначчи
Дано целое число 1≤n≤40 1 \le n \le 40 1≤n≤40, необходимо вычислить n n n-е число 
Фибоначчи (напомним, что F0=0 F_0=0 F0​=0, F1=1 F_1=1 F1​=1 и Fn=Fn−1+Fn−2 F_n=F_{n-1}+F_{n-2} Fn​=Fn−1​+Fn−2​ при n≥2 n \ge 2 n≥2).

Sample Input:
3

Sample Output:
2
"""

# Решение
def fib(n):
    fib = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[-1]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()

"""
Дано число 1≤n≤107 1 \le n \le 10^7 1≤n≤107, необходимо найти 
последнюю цифру n n n-го числа Фибоначчи.

Как мы помним, числа Фибоначчи растут очень быстро, поэтому 
при их вычислении нужно быть аккуратным с переполнением. 
В данной задаче, впрочем, этой проблемы можно избежать, 
поскольку нас интересует только последняя цифра числа 
Фибоначчи: если 0≤a,b≤9 0 \le a,b \le 9 0≤a,b≤9 — последние 
цифры чисел Fi F_i Fi​ и Fi+1 F_{i+1} Fi+1​ соответственно, 
то (a+b) mod 10 (a+b) \bmod{10} (a+b)mod10 — последняя 
цифра числа Fi+2 F_{i+2} Fi+2​.

Sample Input:
102277

Sample Output:
7
"""

# Решение

def fib(n):
    F1, F2 = 0, 1
    for i in range(n - 1):
        F1, F2 = F2, F1 + F2 % 10
    return F2 % 10

def main():
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()

"""

Задача на программирование повышенной сложности: огромное число Фибоначчи по модулю

Даны целые числа 1≤n≤1018 1 \le n \le 10^{18} 1≤n≤1018 и 2≤m≤105 2 \le m \le 10^5 2≤m≤105, 
необходимо найти остаток от деления n n n-го числа Фибоначчи на m m m.



Sample Input:
10 2

Sample Output:
1
"""

# Решение
def fib_mod(n, m):
    F1, F2 = 0, 1
    G = [0, 1]
    for i in range(1, 6 * m + 2):
        F1, F2 = F2, (F1 + F2) % m
        if F1 == 0 and F2 == 1:
            G.pop()
            return G[n % len(G)]
        else:
            G.append(F2)
    
    


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()