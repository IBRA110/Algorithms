"""
Хеширование цепочками — один из наи-более популярных методов 
реализации хеш-таблиц на практике. Ваша цель в данной задаче — 
реализовать такую схему, используя таблицу с m ячейками и 
полино-миальной хеш-функцией на строка х h(S) =|S|−1∑i=0S[i] 
xi mod p  mod m ,где S[i]— ASCII-код i-го символа строки S,
p = 1 000 000 007 простое число, а x = 263. 
Ваша программа должна поддерживать следующиетипы запросов:
add string: добавить строку string в таблицу. Если такая строка уже 
есть, проигнорировать запрос;
del string: удалить строку string из таблицы. Если такой строки нет, 
проигнорировать запрос;
find string: вывести «yes» или «no» в зависимости от того,
есть в таблице строка string или нет;
check i: вывести i-й список (используя пробел в качестве раз-делителя); 
если i-й список пуст, вывести пустую строку.
При добавлении строки в цепочку, строка должна добавляться в 
на-чалоцепочки.
Формат входа.
Первая строка размер хеш-таблицы m. Следующая строка содержит 
количество запросовn. Каждая из последую-щих n строк содержит запрос 
одного из перечисленных выше четырёх типов.
Формат выхода.
Для каждого из запросов типа
find и check выведите результат в отдельной строке.
Ограничения.1≤n≤105;n5≤m≤n. Все строки имеют длину от одного до 
пятнадцати и содержат только буквы латинскогоалфавита.
Пример.

Sample Input 1:
5
12
add world
add HellO
check 4
find World
find world
del world
check 4
del HellO
add luck
add GooD
check 2
del good

Sample Output 1:
HellO world
no
yes
HellO
GooD luck

Sample Input 2:
4
8
add test
add test
find test
del test
find test
find Test
add Test
find Test

Sample Output 2:
yes
no
no
yes
"""

# Решение

def hash_t(b, m):
    if len(b) < 2:
        k = ord(b[0])
    else:
        k, o = ord(b[0]) + ord(b[1]) * 263, 2
        for j in b[2:]:
            k += ord(j) * 263 ** o % 1000000007
            o += 1
    return (k % 1000000007) % m

def find(hash_table, b, m):
    fi = hash_t(b, m)
    if fi in hash_table:
        if b in hash_table[fi]:
            return True
    return False

def main():
    m = int(input())
    hash_table = {}
    comm = int(input())
    for i in range(comm):
        a, b = map(str, input().split())
        if a == "add":
            bomp = hash_t(b, m)
            if bomp not in hash_table:
                hash_table[bomp] = [b]
            else:
                if find(hash_table, b, m):
                    continue
                hash_table[bomp] = [b] + hash_table[bomp] 
        elif a == "check":
            if int(b) in hash_table:
                for i in hash_table[int(b)]:
                    if i == None:
                        continue
                    print(i, end=" ")
                print()
        elif a == "find":
            print("yes" if find(hash_table, b, m) else "no")
        elif a == "del":
            de = hash_t(b, m)
            if de in hash_table:
                for i in range(len(hash_table[de])):
                    if hash_table[de][i] == b:
                        hash_table[de][i] = None

if __name__ == "__main__":
    main()