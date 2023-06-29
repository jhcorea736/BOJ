from itertools import permutations
import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
result = 0

for datum in permutations(data, 3):
    if m >= sum(datum):
        result =  max(result, sum(datum))

print(result)