"""
Телефонная книга
Реализовать структуру данных, эффективно обрабатывающую запро-сы вида 
add number name, del number и find number.
Вход.
Последовательность запросов вида add number name, del number и find number, где
number — телефонный номер, содержащий не более семи знаков, а name — короткая строка.
Выход.
Для каждого запроса
find number выведите соответствующее имя или сообщите, что такой записи нет.
Цель в данной задаче — реализовать простую телефонную книгу, 
поддерживающую три следующихтипа запросов. С указанными ограничениями данная задача 
может быть решена с использованием таблицы с прямой адресацией. 
add number name: добавить запись с именем name и телефонным номером number. 
Если запись с таким телефонным номером уже есть, нужно заменить в ней имя на name.
del number: удалить запись с соответствующим телефонным номером. 
Если такой записи нет, ничего не делать.
find number: найти имя записи с телефонным номером number. 
Если запись с таким номером есть, вывести имя. В противном случае вывести «not found» (без кавычек).
Формат входа.
Первая строка содержит число запросов n. Каждая из следующих n строк задаёт 
запрос в одном из трёх описанных выше форматов.
Формат выхода.
Для каждого запроса
find выведите в отдельной строке либо имя, либо «not found».
Ограничения.1≤n≤105. Телефонные номера содержат не более семи цифр и не 
содержат ведущих нулей. Имена содержат только буквы латинского алфавита, 
не являются пустыми строками иимеют длину не больше 15. 
Гарантируется, что среди имён невстречается строка «not found».

Sample Input 1:
12
add 911 police
add 76213 Mom
add 17239 Bob
find 76213
find 910
find 911
del 910
del 911
find 911
find 76213
add 76213 daddy
find 76213

Sample Output 1:
Mom
not found
police
not found
Mom
daddy

Sample Input 2:
8
find 3839442
add 123456 me
add 0 granny
find 0
find 123456
del 0
del 0
find 0

Sample Output 2:
not found
granny
me
not found
"""

# Решение

class Phone_book(dict):
    def add(self, number, name):
        self[number] = name
    
    def find(self, number):
        if number in self:
            return self[number]
        return "not found"
        
    def del_number(self, number):
        if number in self:
            del self[number]

def main():
    n = int(input())
    pb = Phone_book()
    for i in range(n):
        a = [i for i in input().split()]
        assert a[0] == "add" or a[0] == "find" or a[0] == "del"
        if a[0] == "add":
            pb.add(a[1], a[2])
        elif a[0] == "find":
            print(pb.find(a[1]))
        else:
            pb.del_number(a[1])

if __name__ == "__main__":
    main()
