import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
            graph[ny][nx] = 0
            dfs(nx, ny)

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for __ in range(n)]
    cnt = 0
    
    for __ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1:
                dfs(x, y)
                cnt += 1

    print(cnt)