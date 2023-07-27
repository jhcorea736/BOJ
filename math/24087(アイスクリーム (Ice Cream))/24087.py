s = int(input())
a = int(input())
b = int(input())
result = 250

if s > a:
    result += ((s - a) // b) * 100
    if (s - a) % b != 0:
        result += 100

print(result)