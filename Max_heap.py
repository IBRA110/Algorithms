"""
Задача на программирование: очередь с приоритетами

Первая строка входа содержит число операций 1≤n≤105 1 \le n \le 10^5 1≤n≤105. 
Каждая из последующих n n n строк задают операцию одного из следующих двух 
типов:

Insert {\tt Insert} Insert x {\tt x} x, где 0≤x≤109 0 \le x \le 10^9 0≤x≤109 — 
целое число;
ExtractMax {\tt ExtractMax} ExtractMax.

Первая операция добавляет число x x x в очередь с приоритетами, 
вторая — извлекает максимальное число и выводит его.

Sample Input:
6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax

Sample Output:
200
500
"""

# Решение

class Heap(list):
    def insert(self, zahl):
        self.append(zahl)
        i = len(self) - 1
        while self[i] > self[(i - 1) // 2] and (i - 1) // 2 >= 0:
            self[i], self[(i - 1) // 2] = self[(i - 1) // 2], self[i]
            i = (i - 1) // 2
        
    def extract_max(self):
        max = self[0]
        print(max)
        self[0] = self[-1]
        self.pop()
        i = 0
        while 2 * i + 1 < len(self):
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if right < len(self) and self[right] > self[left]:
                j = right
            if self[i] >= self[j]:
                break
            self[i], self[j] = self[j], self[i]
            i = j

def main():
    x = Heap()
    for i in range(int(input())):
        schreib = input().split()
        assert schreib[0] == 'Insert' or schreib[0] == 'ExtractMax'
        if schreib[0] == 'Insert':
            x.insert(int(schreib[1]))
        elif schreib[0] == 'ExtractMax':
            x.extract_max()

if __name__ == "__main__":
    main()

