def max3(a, b, c):
    """a, b, cの最大値を求めて返却"""
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum

print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')
print(f'max3(3, 2, 2) = {max3(3, 2, 2)}')
print(f'max3(1, 2, 3) = {max3(1, 2, 3)}')