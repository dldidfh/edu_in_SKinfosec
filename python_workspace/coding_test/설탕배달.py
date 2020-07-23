def calc(N):
    A = int(N/5)
    B = (N%5)/3
    if B == float:
        return -1
    i = A + B
    return i

print(calc(19))