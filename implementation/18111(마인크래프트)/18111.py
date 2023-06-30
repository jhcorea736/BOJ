import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
data = []

for _ in range(n):
    data.extend(list(map(int, input().split())))

result_time = float('inf')
result_height = 0

for height in range(max(data) + 1):
    time = 0
    inventory = b

    for datum in data:
        if datum < height:
            time += (height - datum)
            inventory -= (height - datum)
        elif datum > height:
            time += 2 * (datum - height)
            inventory += (datum - height)

    if inventory >= 0 and time <= result_time:
        result_time = time
        result_height = height

print(result_time, result_height)