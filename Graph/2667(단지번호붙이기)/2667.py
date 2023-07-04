import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
data = []
result = 0
cnt = 0

def dfs(x, y):
    if 0 <= x < n and 0 <= y < n and graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            dfs(nx, ny)
        return True
    
    return False

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

for x in range(n):
    for y in range(n):
        if dfs(x, y) == True:
            data.append(cnt)
            result += 1
            cnt = 0

data.sort()
print(result)
for datum in data:
    print(datum)