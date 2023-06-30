import sys

def custom_round(n):
    return int(n + 0.5) if n >= 0 else int(n - 0.5)

input = sys.stdin.readline
n = int(input())
data = []

if n == 0:
    print(0)
else:
    for _ in range(n):
        data.append(int(input()))

    data = sorted(data)
    i = custom_round(n * 0.15)
    data = data[i:n - i]

    print(custom_round(sum(data) / len(data)))