import sys
input = sys.stdin.readline

n = int(input())

if n < 3:
    data = []

    for _ in range(n):
        data.append(int(input()))
    
    print(sum(data))
    
else:
    data = [0] * n

    for i in range(n):
        data[i] = int(input())

    memo = [0] * n
    memo[0] = data[0]
    memo[1] = data[0] + data[1]

    for i in range(2, n):
        memo[i] = max(memo[i - 2] + data[i], memo[i - 3] + data[i - 1] + data[i])

    print(memo[n - 1])