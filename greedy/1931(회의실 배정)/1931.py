import sys
input = sys.stdin.readline

data = []
cnt = 0
last = 0

for _ in range(int(input())):
    data.append(list(map(int, input().split())))

data = sorted(data, key=lambda x: (x[1], x[0]))

for start_time, end_time in data:
    if start_time >= last:
        cnt += 1
        last = end_time

print(cnt)