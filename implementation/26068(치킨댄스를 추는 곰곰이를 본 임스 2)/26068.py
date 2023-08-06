cnt = 0

for _ in range(int(input())):
    x = input()
    if int(x[2:]) <= 90:
        cnt += 1

print(cnt)