import sys
input = sys.stdin.readline

def fibo(n):
    memo_zero = [1, 0, 1]
    memo_one = [0, 1, 1]
    length = len(memo_zero)

    if length <= n:
        for i in range(length, n + 1):
            memo_zero.append(memo_zero[i - 1] + memo_zero[i - 2])
            memo_one.append(memo_one[i - 1] + memo_one[i - 2])

    return memo_zero[n], memo_one[n]

for _ in range(int(input())):
    print(*fibo(int(input())))