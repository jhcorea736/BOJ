n = int(input())
data = input()
result = cnt = 0

for datum in data:
    result += (ord(datum) - 96) * (31 ** cnt)
    cnt += 1

print(result % 1234567891)