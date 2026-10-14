def prime_factorize(n: int) -> dict:  # 試し割法。計算量はルートn
    a = {}
    while n % 2 == 0:
        if 2 not in a:
            a[2] = 0
        a[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            if f not in a:
                a[f] = 0
            a[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        if n in a:
            a[n] += 1
        else:
            a[n] = 1

    return a
