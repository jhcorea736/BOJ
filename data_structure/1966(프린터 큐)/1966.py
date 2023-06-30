from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    data_queue = deque(list(map(int, input().split())))
    index_queue = deque([i for i in range(n)])
    cnt = 0

    while True:
        if data_queue[0] == max(data_queue):
            cnt += 1

            if index_queue[0] == m:
                print(cnt)
                break
            else:
                data_queue.popleft()
                index_queue.popleft()
                
        else:
            data_queue.append(data_queue.popleft())
            index_queue.append(index_queue.popleft())