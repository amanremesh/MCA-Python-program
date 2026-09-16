import math
for i in range(1000, 10000):
    root = math.isqrt(i)
    if root * root == i and all(int(digit) % 2 == 0 for digit in str(i)):
        print(i)
