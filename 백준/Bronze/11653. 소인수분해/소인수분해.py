N=int(input())
def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            print(i)
            n = n / i
        else:
            i = i + 1
prime_factors(N)