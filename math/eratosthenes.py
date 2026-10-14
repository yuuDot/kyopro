def eratosthenes(mx: int) -> list:  # 計算量は N log log N 程度
    is_prime = [True] * (mx + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(mx**0.5) + 1):
        if is_prime[i]:
            for j in range(i**2, mx + 1, i):
                is_prime[j] = False

    prime_num = [i for i in range(mx + 1) if is_prime[i]]

    return prime_num
