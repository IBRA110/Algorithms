"""
Множество с запросами суммы на отрезке
Реализуйте структуру данных для хранения множества целых чисел,
поддерживающую запросы добавления, удаления, поиска, а также суммы на отрезке. 
На вход в данной задаче будет дана последовательность таких запросов. 
Чтобы гарантировать, что ваша программа обрабатывает каждый запрос по мере 
поступления (то есть онлайн), каждый запрос будет зависеть от результата 
выполнения одного изпредыдущих запросов. Если бы такой зависимости не было, 
задачу можно было бы решить оффлайн: сначала прочитать весь вход и сохранить 
все запросы в каком-нибудь виде, а потом прочитать входещё раз, 
параллельно отвечая на запросы.
Формат входа.
Изначально множество пусто. Первая строка содержит число запросов n. 
Каждая из n следующих строк содержит запрос в одном из следующих четырёх 
форматов:•+ i: добавить числоf(i)в множество (если оно уже есть,проигнорировать запрос);
•- i: удалить числоf(i)из множества (если его нет, про-игнорировать запрос);
•? i: проверить принадлежность числаf(i)множеству;
•s l r: посчитать сумму всех элементов множества, попадающих в отрезок[f(l), 
f(r)].Функция f определяется следующим образом. Пусть s — результат 
последнего запроса суммы на отрезке (если таких запросов ещё не было, то s= 0). 
Тогдаf(x) = (x+s) mod 1 000 000 001.
Формат выхода.
Для каждого запроса типа ? i выведите «Found» или «Not found». 
Для каждого запроса суммы выведите сумму всех элементов множества, 
попадающих в отрезок[f(l), f(r)]. 
Гарантируется, что во всех тестах f(l)≤f(r).
Ограничения.1≤n≤105;0≤i≤109.

Simple input:
15
? 1
+ 1
? 1
+ 2
s 1 2
+ 1000000000
? 1000000000
- 1000000000
? 1000000000
s 999999999 1000000000
- 2
? 2
- 0
+ 9
s 0 9

Simple output:
Not found 
Found 
3
Found
Not found
1
Not found
10

Для первых пяти запросов s = 0, для следующих пяти — s = 3, 
для следующих пяти — s = 1. Заданные запросы разворачиваются в следующие: 
find(1), add(1), find(1), add(2), sum(1,2)→3,add(2), find(2)→Found, del(2), 
find(2)→Not found, sum(1,2)→1,del(3), find(3)→Not found, del(1), add(10), 
sum(1,10)→10. 
Добавление элемента дважды не изменяет множество, как и попытки удалить элемент, 
которого в множестве нет.

Simple input:
5
? 0
+ 0
? 0
- 0
? 0

Simple output:
Not found
Found
Not found

Simple input:
5
+ 491572259
? 491572259
? 899375874
s 310971296 877523306
+ 352411209

Sumple output:
Found
Not found
491572259
"""

# Решение

class TreeAvl:
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1
        self.parent = parent
        self.size = 1
        self.sum = self.key

    def insert(self, key):
        if self.key is None:
            self.key = key
            self.sum = key
            return
        if self.key == key:
            return
        if key < self.key: # insert key in left suptree
            if self.left:
                self.left.insert(key)
            else:
                self.left = TreeAvl(key, self.key)
        else: # insert key in right suptree
            if self.right:
                self.right.insert(key)
            else:
                self.right = TreeAvl(key, self.key)
        self._balance_insert(key)
        self.size = self._update_size()
        self.sum = self._update_sum()

    def search(self, x):
        if self.key == x:
            return "Found"
        if self.key == None:
            return "Not found"
        if x < self.key: # x might be in left subtree
            if self.left:
                return self.left.search(x)
            else:
                return "Not found"
        if x > self.key: # x might be in right subtree
            if self.right:
                return self.right.search(x)
            else:
                return "Not found"

    def delete(self, x):
        if self.parent is None and self.left and self.right is None and x == self.key:
            self.key, self.left, self.right = self.left.key, self.left.left, self.left.right
        elif self.parent is None and self.right and self.left is None and x == self.key:
            self.key, self.left, self.right = self.right.key, self.right.left, self.right.right
        else:
            if x < self.key:
                if self.left:
                    self.left = self.left.delete(x)
            elif x > self.key:
                if self.right:
                    self.right = self.right.delete(x)
            else:
                if self.left is None and self.right is None:
                    self.key = None
                    return
                elif self.left is None:
                    return self.right
                elif self.right is None:
                    return self.left
                if self.right.height > self.left.height:
                    min_val = self.right.find_min()
                    self.key = min_val
                    self.right = self.right.delete(min_val)
                elif self.right.height < self.left.height:
                    max_val = self.left.find_max()
                    self.key = max_val
                    self.left = self.left.delete(max_val)
                else:
                    min_val = self.right.find_min()
                    self.key = min_val
                    self.right = self.right.delete(min_val)
        self._balance_delete(x)
        self.size = self._update_size()
        self.sum = self._update_sum()
        return self

    def in_order(self):
        elements = []
        if self.left: # visit left tree
            elements += self.left.in_order()
        elements.append(self.key) # visit base node
        if self.right: # visit right tree
            elements += self.right.in_order()
        return elements

    def pre_order(self):
        elements = []
        elements.append(self.key) # visit base node
        if self.left: # visit left tree
            elements += self.left.in_order()
        if self.right: # visit right tree
            elements += self.right.in_order()
        return elements

    def post_order(self):
        elements = []
        if self.left: # visit left tree
            elements += self.left.in_order()
        if self.right: # visit right tree
            elements += self.right.in_order()
        elements.append(self.key) # visit base node
        return elements

    def find_max(self):
        if self.right is None:
            return self.key
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.key
        return self.left.find_min()

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def index_search(self, k):
        leftsize = self.left.size 
        if k == leftsize + 1:
            return self.key
        if k < leftsize + 1:
            return self.left.order_statistics(k)
        else:
            return self.right.order_statistics(k - leftsize - 1)

    def sum_section(self, a, b):
        if a <= self.key <= b:
            return self._in_order_section(a, b)
        if a > self.key < b and self.right is not None:
            return self.right.sum_section(a, b)
        if a < self.key > b and self.left is not None:
            return self.left.sum_section(a, b)
        else:
            return 0

    def _in_order_section(self, a, b):
        elements = self.key
        if self.left: 
            elements += self.left._left_count(a)
        if self.right: 
            elements += self.right._right_count(b)
        return elements

    def _left_count(self, a):
        left_elements = 0
        if self.key == a:
            left_elements += self.key
            if self.right:
                left_elements += self.right.sum
        elif self.key < a:
            if self.right:
                left_elements += self.right._left_count(a)
        else:
            if self.right:
                left_elements += self.right.sum + self.key
            else:
                left_elements += self.key
            if self.left:
                left_elements += self.left._left_count(a)
        return left_elements

    def _right_count(self, b):
        right_elements = 0
        if self.key == b:
            right_elements += self.key
            if self.left:
                right_elements += self.left.sum
        elif self.key > b:
            if self.left:
                right_elements += self.left._right_count(b)
        else:
            if self.left:
                right_elements += self.left.sum + self.key
            else:
                right_elements += self.key
            if self.right:
                right_elements += self.right._right_count(b)
        return right_elements

    def _update_sum(self):
        left_sum = 0 # Work out the hieght of the current node after the insertion
        right_sum = 0
        if self.left:
            left_sum = self.left.sum
        if self.right:
            right_sum = self.right.sum
        return left_sum + right_sum + self.key

    def _update_size(self):
        left_size = 0 # Work out the hieght of the current node after the insertion
        right_size = 0
        if self.left:
            left_size = self.left.size
        if self.right:
            right_size = self.right.size
        return left_size + right_size + 1

    def _balance_insert(self, key):
        self.height = self._height_meter()
        left_height = 0
        right_height = 0
        if self.right:
            right_height = self.right.height
        if self.left:
            left_height = self.left.height
        balance = left_height - right_height
        if balance > 1 and key < self.left.key:
            return self._turn_right()
        if balance < -1 and key > self.right.key:
            return self._turn_left()
        if balance > 1 and key < self.left.key:
            return self._turn_left_right()
        if balance < -1 and key > self.right.key:
            return self._turn_right_left()

    def _balance_delete(self, key):
        self.height = self._height_meter()
        left_height = 0
        right_height = 0
        if self.right:
            right_height = self.right.height
        if self.left:
            left_height = self.left.height
        balance = left_height - right_height
        if balance > 1 and key > self.left.key:
            return self._turn_right()
        if balance < -1 and key < self.right.key:
            return self._turn_left()
        if balance > 1 and key > self.left.key:
            return self._turn_left_right()
        if balance < -1 and key < self.right.key:
            return self._turn_right_left()

    def _turn_left(self):
        new = TreeAvl(self.key, self.parent, self.left, self.right)
        new.right = self.right.left
        self.key, self.right, self.left = self.right.key, self.right.right, new
        self.left.parent = self.key
        self.left.height = self.left._height_meter()
        self.left.size = self.left._update_size()
        self.left.sum = self.left._update_sum()
        self.height = self._height_meter()
        self.size = self._update_size()
        self.sum = self._update_sum()

    def _turn_right(self):
        new = TreeAvl(self.key, self.parent, self.left, self.right)
        new.left = self.left.right
        self.key, self.left, self.right = self.left.key, self.left.left, new
        self.right.parent = self.key
        self.right.height = self.right._height_meter()
        self.right.size = self.right._update_size()
        self.right.sum = self.right._update_sum()
        self.height = self._height_meter()
        self.size = self._update_size()
        self.sum = self._update_sum()

    def _turn_left_right(self):
        self.left._turn_left()
        self._turn_right()

    def _turn_right_left(self):
        self.right._turn_right()
        self._turn_left()

    def _height_meter(self):
        left_child_height = 0 # Work out the hieght of the current node after the insertion
        right_child_height = 0
        if self.left:
            left_child_height = self.left.height
        if self.right:
            right_child_height = self.right.height
        return max(left_child_height, right_child_height) + 1 # Calculate the height after the recursive call is made

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def f(x, s):
    return (x + s) % 1000000001

def main():
    avl_tree = TreeAvl()
    s = 0
    for i in range(int(input())):
        i = [i for i in input().split()]
        if i[0] == "+":
            avl_tree.insert(f(int(i[1]), s))
        elif i[0] == "-":
            if avl_tree.key is not None:
                avl_tree.delete(f(int(i[1]), s))
        elif i[0] == "?":
            print(avl_tree.search(f(int(i[1]), s)))
        elif i[0] == "s":
            if avl_tree.key is not None:
                s = avl_tree.sum_section(f(int(i[1]), s), f(int(i[2]), s))
                print(s)
            else:
                s = 0
                print(s)
        else:
            print("incorrect input")
            break

if __name__ == '__main__':
    main()
