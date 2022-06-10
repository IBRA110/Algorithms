"""
Задача на программирование: различные слагаемые

По данному числу 1≤n≤109 1 \le n \le 10^9 1≤n≤109 
найдите максимальное число k k k, для которого n n n 
можно представить как сумму k k k различных натуральных слагаемых. 
Выведите в первой строке число k k k, во второй — k k k слагаемых.

Sample Input 1:
4

Sample Output 1:
2
1 3 

Sample Input 2:
6

Sample Output 2:
3
1 2 3 
"""

# Решение
import math
n = int(input())
x, s = 1, 1
if n == 1 or n == 2:
    print(1)
    print(n)
else:
    print(math.floor((math.sqrt(1 + 8 * n) - 1) / 2))
    while True:
        print(s, end=" ")
        if x + (s + 1) + (s + 2) > n:
            while x + s != n:
                s += 1
            print(s, end=" ")
            break
        s += 1
        x += s

