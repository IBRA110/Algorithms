"""
Задача на программирование: наибольший общий делитель

По данным двум числам 1≤a,b≤2⋅109 1 \le a, b \le 2 \cdot 10^9 1≤a,b≤2⋅109 
найдите их наибольший общий делитель.

Sample Input 1:
18 35

Sample Output 1:
1

Sample Input 2:
14159572 63967072

Sample Output 2:
4
"""

# Решение
def gcd(a, b):
    assert a >= 0 and b >= 0
    return a if b == 0 else gcd(b, a % b)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()