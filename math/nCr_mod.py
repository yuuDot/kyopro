mod = 998244353
_K = 1  # 必要な階乗の上限

_fact = [1] * (_K + 1)
for i in range(_K):
    _fact[i + 1] = _fact[i] * (i + 1) % mod
_ifact = [1] * (_K + 1)
_ifact[_K] = pow(_fact[_K], -1, mod)
for i in range(_K, 0, -1):
    _ifact[i - 1] = _ifact[i] * i % mod


def c(n: int, r: int) -> int:
    if n < r or n < 0 or r < 0:
        return 0
    return _fact[n] * _ifact[r] % mod * _ifact[n - r] % mod


# nが巨大で、rとなる数字がそこそこのとき
a = 10**5
b = 10**5
n = 10**9
com = [1] * (max(a, b) + 1)
for _K in range(1, max(a, b) + 1):
    com[_K] = (com[_K - 1] * (n - _K + 1) * pow(_K, -1, mod)) % mod
