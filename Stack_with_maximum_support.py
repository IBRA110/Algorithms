"""
Стек с поддержкой максимума
Реализовать стек с поддержкой операций push, pop и max.
Вход.
Последовательность запросов push, pop и max.
Выход.
Для каждого запроса max вывести максимальноечисло, 
находящее на стеке. push pop Стек — абстрактная структура данных,
поддерживающая операции push и pop.
Несложно реализовать стек так, чтобы обе эти операции работали за константное время. 
В данной задача ваша цель — рас-шить интерфейс стека так, 
чтобы он до-полнительно поддерживал операциюmaxи при этом чтобы время работы всех 
опе-раций по-прежнему было константным.
Формата входа.
Первая строка содержит число запросов q. 
Каждая из последующихqстрок задаёт запрос в одном из следующихформатов:
push v, pop, or max.
Формат выхода.
Для каждого запросаmaxвыведите (в отдельнойстроке) текущий максимум на стеке.
Ограничения.1≤q≤400 000,0≤v≤100 000.

Sample Input 1:
5
push 2
push 1
max
pop
max

Sample Output 1:
2
2

Sample Input 2:
5
push 1
push 2
max
pop
max

Sample Output 2:
2
1

Sample Input 3:
10
push 2
push 3
push 9
push 7
push 2
max
max
max
pop
max

Sample Output 3:
9
9
9
9
"""

# Решение

def main():
    n = int(input())
    maximus = [[0, 0]]
    for i in range(n):
        x = [input().split()]
        if x[0][0] == 'push':
            if maximus[-1][1] < int(x[0][1]):
                maximus.append([int(x[0][1]), int(x[0][1])])
            else:
                maximus.append([int(x[0][1]), maximus[-1][1]])
        elif x[0][0] == 'max':
            if maximus:
                print(maximus[-1][1])
            else:
                print(0)
        elif x[0][0] == 'pop':
            maximus.pop()


if __name__ == '__main__':
    main()