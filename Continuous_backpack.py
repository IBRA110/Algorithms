"""
Первая строка содержит количество предметов 1≤n≤103 1 \le n \le 10^3 1≤n≤103 и 
вместимость рюкзака 0≤W≤2⋅106 0 \le W \le 2 \cdot 10^6 0≤W≤2⋅106. Каждая из 
следующих n n n строк задаёт стоимость 0≤ci≤2⋅106 0 \le c_i \le 2\cdot 10^6 0≤ci​≤2⋅106 и 
объём 0<wi≤2⋅106 0 \lt w_i \le 2\cdot 10^6 0<wi​≤2⋅106 предмета (n n n, W W W, ci c_i ci​, 
wi w_i wi​ — целые числа). Выведите максимальную стоимость частей предметов 
(от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), 
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

Sample Input:
3 50
60 20
100 50
120 30

Sample Output:
180.000
"""

# Решение
import sys
import heapq

def fractional_knapsack(capacity, values_and_weights):
    order = [(-v / w, w) for v, w in values_and_weights]
    heapq.heapify(order)
    acc = 0
    while order and capacity:
        v_per_w, w = heapq.heappop(order)
        can_take = min(w, capacity)
        acc -= v_per_w * can_take
        capacity -= can_take
    return acc


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, capacity = next(reader)
    values_and_weights = list(reader)
    assert len(values_and_weights) == n
    opt_value = fractional_knapsack(capacity, values_and_weights)
    print('{:.3f}'.format(opt_value))


if __name__ == '__main__':
    main()