import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = {}

for index in range(1, n + 1):
    name = input().rstrip()
    data[index] = name
    data[name] = index

for _ in range(m):
    target = input().rstrip()
    print(data[int(target)]) if target.isdigit() else print(data[target])