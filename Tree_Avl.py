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

    # ---------- helpers ----------
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

    # ---------- rotations ----------
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

    # ---------- iterative insert ----------
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

            new = node

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

            if new is not node:
                if i == 0:
                    self.root = new
                else:
                    parent = stack[i - 1]
                    if parent.left is node:
                        parent.left = new
                    else:
                        parent.right = new

    # ---------- iterative search ----------
    def search(self, key):
        cur = self.root
        while cur:
            if key == cur.key:
                return True
            cur = cur.left if key < cur.key else cur.right
        return False

    # ---------- iterative delete ----------
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

            new = node

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

            if new is not node:
                if i == 0:
                    self.root = new
                else:
                    parent = stack[i - 1]
                    if parent.left is node:
                        parent.left = new
                    else:
                        parent.right = new

    # ---------- safe range sum (iterative in-order) ----------
    def range_sum(self, L, R):
        total = 0
        cur = self.root
        stack = []

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            if cur.key > R:
                break

            if L <= cur.key <= R:
                total += cur.key

            cur = cur.right

        return total

    # ---------- f(x, s) ----------
    def f(self, x):
        return (x + self.s) % self.MOD

    # ---------- main loop for problem ----------
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

            else:  # "s"
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
    print("print    → in-order")
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
            print(tree.range_sum(int(cmd[1]), int(cmd[2])))
        elif op == "print":
            st, cur, out = [], tree.root, []
            while st or cur:
                while cur:
                    st.append(cur)
                    cur = cur.left
                cur = st.pop()
                out.append(cur.key)
                cur = cur.right
            print(out)
        else:
            print("Unknown command")
