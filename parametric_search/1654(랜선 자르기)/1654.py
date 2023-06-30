import sys
input = sys.stdin.readline

def parametric_search(data, target):
    left = 1
    right = max(data)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        total = 0

        for datum in data:
            total += datum // mid

        if total >= target:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result

k, n = map(int, input().split())
data = []

for _ in range(k):
    data.append(int(input()))

print(parametric_search(data, n))