t, s = map(int, input().split())

if t <= 11:
    result = 280
elif 12 <= t <= 16:
    if s == 0:
        result = 320
    else:
        result = 280
else:
    result = 280

print(result)