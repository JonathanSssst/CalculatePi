import math
import time

def sin(d):
    return math.sin(math.radians(d))

def tan(d):
    return math.tan(math.radians(d))

def inscribe(n:int):
    return 2 * n * sin(180 / n)

def circumscribe(n:int):
    return 2 * n * tan(180 / n)

def pi(n:int):
    i = inscribe(n)
    c = circumscribe(n)
    return (i + c) / 4

n = 1000000 ** 10

# 记录总程序开始时间
total_start_time = time.time()

print(f'{n}: {pi(n)}\tError={abs(pi(n) - math.pi):.12f}')

# 计算总运行时间
total_run_time = time.time() - total_start_time

print(f'\n\nTotal run time: {total_run_time:.2f} seconds')

input()
