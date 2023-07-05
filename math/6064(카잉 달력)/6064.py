import sys
input = sys.stdin.readline

def find(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    print(find(n, m, x, y))