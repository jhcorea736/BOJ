for _ in range(int(input())):
    h, w, n = map(int, input().split())
    floor = n % h

    if floor == 0:
        floor = h

    room = (n - 1) // h + 1

    print(floor * 100 + room)