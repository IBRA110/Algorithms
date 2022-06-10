"""
Кривая Коха -- это простой геометрический фрактал. 
"""



def koch_curve(n):
    if n == 0:
        return
    else:
        koch_curve(n - 1)
        print('turn 60')
        koch_curve(n - 1)
        print('turn -120')
        koch_curve(n - 1)
        print('turn 60')
        koch_curve(n - 1)
 
 
koch_curve(int(input()))