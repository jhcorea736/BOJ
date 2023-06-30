for _ in range(int(input())):
    k = int(input())
    n = int(input())

    data = [i for i in range(1, n + 1)]

    for _ in range(1, k + 1):
        memorization = [0] * n

        for i in range(n):
            memorization[i] = sum(data[:i + 1])

        data = memorization

    print(data[n - 1])