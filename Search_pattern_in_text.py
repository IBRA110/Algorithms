"""
Поиск образца в тексте
Найти все вхождения строки Pattern в строку Text.
Вход.
Строки Pattern и Text.
Выход.
Все индексы i строки Text, начиная с которых строка Pattern входит 
в Text:Text[i..i+|Pattern|−1] = Pattern.
Реализуйте алгоритм Карпа–Рабина.
Формат входа.
Образец Pattern и текст Text.
Формат выхода.
Индексы вхождений строки Pattern в строку Text в возрастающем порядке, 
используя индексацию с нуля.
Ограничения.
1≤ |Pattern| ≤ |Text| ≤5·105.
Суммарная длина всех вхождений образ-ца в текста не превосходит 108. 
Обе строки содержат буквы латинского алфавита.

Sample Input 1:
aba
abacaba

Sample Output 1:
0 4

Sample Input 2:
Test
testTesttesT

Sample Output 2:
4

Sample Input 3:
aaaaa
baaaaaaa

Sample Output 3:
1 2 3
"""

# Решение

def hash_pattem(pattem, alph, len_pattem):
    p = 0
    for i in pattem:
        p += ord(i) * pow(alph, len_pattem, 1000000007)
        len_pattem -= 1
    return p % 1000000007

def rabin_karp_hash(text, p, alph, len_pattem):
    t = hash_pattem(text[0:len_pattem + 1], alph, len_pattem)
    if p == t:
        print(0, end=" ")
        print()
    i_start, i_end = 0, len_pattem
    while i_end < len(text) - 1:
        i_end += 1
        t = (t - ord(text[i_start]) * pow(alph, len_pattem,1000000007)) * alph % 1000000007 + ord(text[i_end]) * pow(alph, 0,1000000007)
        i_start += 1
        if p == t:
            print(i_start, end=" ")
            print()

def main():
    pattem = input()
    text = input()
    if len(pattem) > len(text):
        return
    alph, len_pattem = 26, len(pattem) - 1
    p = hash_pattem(pattem, alph, len_pattem)
    rabin_karp_hash(text, p, alph, len_pattem)

if __name__ == "__main__":
    main()