"""
Задача на программирование: кодирование Хаффмана
По данной непустой строке s s s длины не более 104 10^4 104, 
состоящей из строчных букв латинского алфавита, 
постройте оптимальный беспрефиксный код. В первой строке выведите 
количество различных букв k k k, встречающихся в строке, и 
размер получившейся закодированной строки. В следующих k k k 
строках запишите коды букв в формате "letter: code". 
В последней строке выведите закодированную строку.
Sample Input 1:
a

Sample Output 1:
1 1
a: 0
0

Sample Input 2:
abacabad

Sample Output 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111

Задача на программирование: декодирование Хаффмана
Восстановите строку по её коду и беспрефиксному коду символов. 
В первой строке входного файла заданы два целых числа k k k и l l l 
через пробел — количество различных букв, встречающихся в строке, 
и размер получившейся закодированной строки, соответственно. 
В следующих k k k строках записаны коды букв в формате "letter: 
code". Ни один код не является префиксом другого. Буквы могут быть 
перечислены в любом порядке. В качестве букв могут встречаться лишь 
строчные буквы латинского алфавита; каждая из этих букв 
встречается в строке хотя бы один раз. 
Наконец, в последней строке записана закодированная строка. 
Исходная строка и коды всех букв непусты. 
Заданный код таков, что закодированная строка имеет минимальный возможный размер.

В первой строке выходного файла выведите строку s s s. 
Она должна состоять из строчных букв латинского алфавита. 
Гарантируется, что длина правильного ответа не превосходит 104 10^4 104 символов.

Sample Input 1:
1 1
a: 0
0

Sample Output 1:
a

Sample Input 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111

Sample Output 2:
abacabad
"""
# Решение

import heapq
from collections import Counter, namedtuple

class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')

class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count1, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')
    return code

def huffman_decode(encoded, code):
    code1 = {i: j for j, i in code.items()}
    x, s, j = 0, '', ''
    while x != len(encoded):
        s += encoded[x]
        if s in code1:
            j += code1[s]
            s = ''
        x += 1
    return j

def main():
    s = input()
    code = huffman_encode(s)
    encoded = ''.join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print('{}: {}'.format(ch, code[ch]))
    print(encoded)
    c = huffman_decode(encoded, code)
    print(c)

    
def test(n_iter=100):
    import random
    import string

    for i in range(n_iter):
        lenght = random.randint(0, 30)
        s = ''.join(random.choice(string.ascii_letters)for _ in range(lenght))
        code = huffman_encode(s)
        encoded = ''.join(code[ch] for ch in s)
        assert huffman_decode(encoded, code) == s

if __name__ == "__main__":
    main()
    test()