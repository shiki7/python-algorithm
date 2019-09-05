import fractions

def lcm(a):
    x = a[0]
    for i in range(1, len(a)):
        x = x * a[i] // fractions.gcd(x, a[i])
        return x

a = list(map(int, input().split()))
print(lcm(a))