n = int(input())
a, b, c = map(int, input().split())
result = min(n, a) + min(n, b) + min(n, c)

print(result)