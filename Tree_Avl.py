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

class AVLTree:
    class Node:
        __slots__ = ("key", "left", "right", "height", "size", "sum")

        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.height = 1
            self.size = 1
            self.sum = key

    def __init__(self):
        self.root = None
        self.s = 0
        self.MOD = 1000000001

    # ----------------- helpers -----------------
    def _h(self, n):
        return n.height if n else 0

    def _sz(self, n):
        return n.size if n else 0

    def _sm(self, n):
        return n.sum if n else 0

    def _update(self, n):
        n.height = max(self._h(n.left), self._h(n.right)) + 1
        n.size = self._sz(n.left) + self._sz(n.right) + 1
        n.sum = self._sm(n.left) + self._sm(n.right) + n.key

    def _bf(self, n):
        return self._h(n.left) - self._h(n.right)

    # ----------------- rotations -----------------
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update(y)
        self._update(x)
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update(x)
        self._update(y)
        return y

    # ----------------- iterative insert -----------------
    def insert(self, key):
        if not self.root:
            self.root = self.Node(key)
            return

        stack = []
        cur = self.root

        # BST insert
        while True:
            stack.append(cur)
            if key == cur.key:
                return
            elif key < cur.key:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = self.Node(key)
                    stack.append(cur.left)
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = self.Node(key)
                    stack.append(cur.right)
                    break

        # rebalance bottom-up
        for i in range(len(stack) - 1, -1, -1):
            node = stack[i]
            self._update(node)
            bf = self._bf(node)

            # Left heavy
            if bf > 1:
                if key < node.left.key:
                    new = self._rotate_right(node)
                else:
                    node.left = self._rotate_left(node.left)
                    new = self._rotate_right(node)
            # Right heavy
            elif bf < -1:
                if key > node.right.key:
                    new = self._rotate_left(node)
                else:
                    node.right = self._rotate_right(node.right)
                    new = self._rotate_left(node)
            else:
                continue

            if i == 0:
                self.root = new
            else:
                parent = stack[i - 1]
                if parent.left is node:
                    parent.left = new
                else:
                    parent.right = new

    # ----------------- iterative search -----------------
    def search(self, key):
        cur = self.root
        while cur:
            if key == cur.key:
                return True
            cur = cur.left if key < cur.key else cur.right
        return False

    # ----------------- iterative delete -----------------
    def delete(self, key):
        if not self.root:
            return

        stack = []
        cur = self.root

        # find node
        while cur and cur.key != key:
            stack.append(cur)
            cur = cur.left if key < cur.key else cur.right

        if not cur:
            return

        # case: two children → replace with successor
        if cur.left and cur.right:
            succ = cur.right
            stack.append(cur)
            while succ.left:
                stack.append(succ)
                succ = succ.left
            cur.key = succ.key
            cur = succ

        # now cur has ≤1 child
        child = cur.left if cur.left else cur.right

        if not stack:
            self.root = child
        else:
            parent = stack[-1]
            if parent.left is cur:
                parent.left = child
            else:
                parent.right = child

        # rebalance bottom-up
        for i in range(len(stack) - 1, -1, -1):
            node = stack[i]
            self._update(node)
            bf = self._bf(node)

            if bf > 1:
                if self._bf(node.left) >= 0:
                    new = self._rotate_right(node)
                else:
                    node.left = self._rotate_left(node.left)
                    new = self._rotate_right(node)
            elif bf < -1:
                if self._bf(node.right) <= 0:
                    new = self._rotate_left(node)
                else:
                    node.right = self._rotate_right(node.right)
                    new = self._rotate_left(node)
            else:
                continue

            if i == 0:
                self.root = new
            else:
                parent = stack[i - 1]
                if parent.left is node:
                    parent.left = new
                else:
                    parent.right = new

    # ----------------- O(log n) range sum using subtree sums -----------------
    def range_sum(self, L, R):
        total = 0
        cur = self.root

        while cur:
            if cur.key < L:
                cur = cur.right
            elif cur.key > R:
                cur = cur.left
            else:
                # include this node
                total += cur.key

                # include left subtree if fully inside
                if cur.left:
                    # if max(left subtree) >= L
                    left = cur.left
                    while left.right:
                        left = left.right
                    if left.key >= L:
                        total += self._sm(cur.left)

                # include right subtree if fully inside
                if cur.right:
                    # if min(right subtree) <= R
                    right = cur.right
                    while right.left:
                        right = right.left
                    if right.key <= R:
                        total += self._sm(cur.right)

                # break because we counted everything
                break

        return total

    # ----------------- f(x, s) -----------------
    def f(self, x):
        return (x + self.s) % self.MOD

    # ----------------- main loop -----------------
    def run(self):
        n = int(input())
        for _ in range(n):
            parts = input().split()
            op = parts[0]

            if op == "+":
                x = self.f(int(parts[1]))
                self.insert(x)

            elif op == "-":
                x = self.f(int(parts[1]))
                self.delete(x)

            elif op == "?":
                x = self.f(int(parts[1]))
                print("Found" if self.search(x) else "Not found")

            else:  # sum
                l = self.f(int(parts[1]))
                r = self.f(int(parts[2]))
                self.s = self.range_sum(l, r)
                print(self.s)


if __name__ == "__main__":
    tree = AVLTree()

    print("Manual AVLTree console. Commands:")
    print("+ x      → insert x")
    print("- x      → delete x")
    print("? x      → search x")
    print("sum l r  → range sum [l, r]")
    print("print    → debug print (in‑order)")
    print("exit     → quit")

    while True:
        cmd = input(">>> ").strip().split()

        if not cmd:
            continue

        op = cmd[0]

        if op == "exit":
            break

        elif op == "+" and len(cmd) == 2:
            tree.insert(int(cmd[1]))

        elif op == "-" and len(cmd) == 2:
            tree.delete(int(cmd[1]))

        elif op == "?" and len(cmd) == 2:
            print("Found" if tree.search(int(cmd[1])) else "Not found")

        elif op == "sum" and len(cmd) == 3:
            l = int(cmd[1])
            r = int(cmd[2])
            print(tree.range_sum(l, r))

        elif op == "print":
            # simple in‑order traversal
            stack = []
            cur = tree.root
            out = []
            while stack or cur:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                out.append(cur.key)
                cur = cur.right
            print(out)

        else:
            print("Unknown command")

