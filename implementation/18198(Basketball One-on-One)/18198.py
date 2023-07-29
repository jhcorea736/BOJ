data = input()
a = b = 0

for i in range(len(data)):
    if data[i] == "A":
        a += int(data[i + 1])
    elif data[i] == "B":
        b += int(data[i + 1])

print("A" if a > b else "B")