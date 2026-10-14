from math import gcd


def CRT(x: list[tuple[int, int]]) -> int:
    """
    要素の個数をN, modの最大値をMとしたときO(N log M) \n
    x = [(mod0, val0), (mod1, val1), ...] としたとき、\n
    r %% mod0 = val0, r %% mod1 = val1, ... となる最小のrを返す
    """
    r, m = 0, 1

    for mod, val in x:
        if mod <= 0:
            raise ValueError("mod must be positive")

        val %= mod
        g = gcd(m, mod)
        diff = val - r

        # 解が存在しない
        if diff % g != 0:
            return -1

        m1 = m // g
        mod1 = mod // g

        # r + m * t ≡ val (mod mod)
        if mod1 == 1:
            t = 0
        else:
            t = (diff // g * pow(m1, -1, mod1)) % mod1

        m *= mod1
        r = (r + (m // mod1) * t) % m

    return r
