import sys
n, m = map(int, sys.stdin.readline().split())
data = []
result = []

for _ in range(n):
    data.append(sys.stdin.readline().rstrip())

for i in range(n - 7):
    for j in range(m - 7):
        result1 = result2 = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if data[a][b] == 'W':
                        result1 += 1
                    if data[a][b] == 'B':
                        result2 += 1
                else:
                    if data[a][b] == 'B':
                        result1 += 1
                    if data[a][b] == 'W':
                        result2 += 1
        
        result.append(min(result1, result2))

print(min(result))