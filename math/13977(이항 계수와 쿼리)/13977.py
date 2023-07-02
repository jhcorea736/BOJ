import sys
input = sys.stdin.readline

mod = 1000000007
max_num = 4000000
fact = [1] * (max_num + 1)

def mod_mul(x, y):
    return (x * y) % mod

def mod_pow(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        n = mod_pow(base, exp // 2)
        return mod_mul(n, n)
    else:
        return mod_mul(base, mod_pow(base, exp - 1))
    
def binomial_coefficient(n, k):
    x = fact[n]
    y = mod_mul(fact[k], fact[n - k])

    return 1 if k == 0 or k == n else mod_mul(x, mod_pow(y, mod - 2))

for i in range(1, max_num + 1):
    fact[i] = mod_mul(fact[i - 1], i)

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(binomial_coefficient(n, k))
