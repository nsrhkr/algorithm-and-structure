def med3(a, b, c):
    """a, b, cの中央値を求めて返却"""
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print(f'med3(1,2,3) = {med3(1,2,3)}')