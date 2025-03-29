from algebra import binary_exponentiation
import time

n, m = map(int, input().split())

s = 0

x = time.time()
for i in range(1, n + 1):
    s += binary_exponentiation(n // i, m, 1000000007)

print(s)
print(time.time() - x)