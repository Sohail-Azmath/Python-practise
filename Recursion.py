
a, b = map(int, input().split())

res = 0
for _ in range(b):
    res += a

print(res)


def multiply(a, b):
    res = 0
    for i in range(b):
        res += a
    return res

print(multiply(5, 3))