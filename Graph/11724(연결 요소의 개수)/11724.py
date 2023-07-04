import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    if visited[i] == False:
        dfs(i)
        cnt += 1
        
print(cnt)